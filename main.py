import pygame
import copy

class Background():
    def load_background(self,level):
        if level==0:
            self.background = pygame.image.load("data/background2.png")
        self.position_x = 0
        self.position_y = 0
        self.speed = 1
    def bliting(self):
        screen.blit(self.background, (self.position_x, self.position_y))
class Person():
    def load_person(self,person):
        if person ==0:
            self.person = pygame.image.load("data/person.png")
            self.person_look_left = pygame.transform.flip(self.person,True,False)
            self.weapon = pygame.image.load("data/sword.png")
            self.weapon_look_left = pygame.transform.flip(self.weapon,True,False)
            self.look_right = True
            self.walk_right_animation =[]
            self.walk_left_animation = []
            self.walk = False
            self.now_frame= 0
            self.tics = fps//6
            self.counter_tics = 0
            for i in range(1,6):
                a = pygame.image.load(f"data/person_walk_anim{i}.png")
                self.walk_right_animation.append(a)
                a = pygame.transform.flip(a,True,False)
                self.walk_left_animation.append(a)

        self.position_x = screen_width//2-(self.person.get_width()//2)
        self.position_y = screen_height-self.person.get_height()-10
        self.speed = background.speed
    def bliting(self):
        if  not animation_active:
            if  self.look_right:
                screen.blit(self.person, (self.position_x, self.position_y))
                screen.blit(self.weapon, (self.position_x, self.position_y))
            else:
                screen.blit(self.person_look_left, (self.position_x, self.position_y))
                screen.blit(self.weapon_look_left, (self.position_x-(self.weapon.get_width()-self.person.get_width()), self.position_y))
        else:
            if self.look_right:
                if self.counter_tics >=self.tics:
                    self.counter_tics =0
                    self.now_frame += 1
                    if not self.look_right:
                        pass
                self.counter_tics+=1
                screen.blit(self.walk_right_animation[self.now_frame%5], (self.position_x, self.position_y))
                screen.blit(self.weapon, (self.position_x, self.position_y))
            else:
                if self.counter_tics >=self.tics:
                    self.counter_tics =0
                    self.now_frame += 1
                    if not self.look_right:
                        pass
                self.counter_tics+=1
                screen.blit(self.walk_left_animation[self.now_frame%5], (self.position_x, self.position_y))
                screen.blit(self.weapon_look_left, (self.position_x-(self.weapon.get_width()-self.person.get_width()), self.position_y))


# class Border(pygame.sprite.Sprite):
#     def __init__(self,x1,y1,x2,y2):
#         super().__init__(self)


running = True
pygame.init()
pygame.display.set_caption('the cool man adventure')
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
fps = 60
clock = pygame.time.Clock()
# font = pygame.font.SysFont("Times New Roman", 40)
# menu_button_width = 500
# menu_button_height = 100

background = Background()
background.load_background(0)
person = Person()
person.load_person(0)
animation_active = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                person.look_right = True
                person.walk = True
                animation_active = True

            elif event.key == pygame.K_LEFT:
                person.look_right = False
                person.walk=True
                animation_active = True
        if event.type == pygame.KEYUP:
            if person.walk:

                person.walk = False
                animation_active= False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        background.position_x += background.speed
    elif keys[pygame.K_RIGHT]:
        background.position_x -= background.speed


    screen.fill((0, 0, 0))
    background.bliting()
    person.bliting()
    pygame.display.update((0,0,screen_width,screen_height))
    clock.tick(fps)
#я блядь ненавижу эту ебаную хуеты под название гит
# эта хуетень только что мне удалила целую ветку!!!
