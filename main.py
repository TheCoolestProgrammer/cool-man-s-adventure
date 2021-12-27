import pygame
import copy

class Background():
    def load_background(self,level):
        if level==0:
            self.background = pygame.image.load("data/background2.png")
        self.position_x = 0
        self.position_y = 0
        self.speed = 3
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
            self.normal_weapon_punch = False
            self.now_frame= 0

            self.animation_active = False
            for i in range(1,6):
                a = pygame.image.load(f"data/person_walk_anim{i}.png")
                self.walk_right_animation.append(a)
                a = pygame.transform.flip(a,True,False)
                self.walk_left_animation.append(a)
            self.tics = fps // len(self.walk_right_animation)//2
            self.counter_tics = 0

            self.person_normal_weapon_punch_right_animation = []
            self.person_normal_weapon_punch_left_animation = []
            self.normal_weapon_punch_right_animation = []
            self.normal_weapon_punch_left_animation = []
            for i in range(1,10):
                a = pygame.image.load(f"data/person_sword_punch{i}.png")
                self.person_normal_weapon_punch_right_animation.append(a)
                a = pygame.transform.flip(a, True, False)
                self.person_normal_weapon_punch_left_animation.append(a)
            for i in range(1,10):
                a = pygame.image.load(f"data/sword_punch{i}.png")
                self.normal_weapon_punch_right_animation.append(a)
                a = pygame.transform.flip(a, True, False)
                self.normal_weapon_punch_left_animation.append(a)


        self.position_x = screen_width//2-(self.person.get_width()//2)
        self.position_y = screen_height-self.person.get_height()-10
        self.speed = background.speed


    def bliting(self):
        if  not self.animation_active:
            if  self.look_right:
                screen.blit(self.person, (self.position_x, self.position_y))
                screen.blit(self.weapon, (self.position_x, self.position_y))
            else:
                screen.blit(self.person_look_left, (self.position_x, self.position_y))
                screen.blit(self.weapon_look_left, (self.position_x-(self.weapon.get_width()-self.person.get_width()), self.position_y))
        else:
            if self.walk:
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


            elif self.normal_weapon_punch:
                if self.counter_tics==0:
                    self.tics=fps//len(self.normal_weapon_punch_left_animation)
                    self.position_y -= self.normal_weapon_punch_left_animation[0].get_height() - self.person.get_height()
                    if not self.look_right:
                        self.position_x -= self.normal_weapon_punch_left_animation[0].get_width() - self.person.get_width()
                if self.look_right:
                    if self.counter_tics >= self.tics:
                        self.counter_tics = 0
                        self.now_frame += 1
                        if not self.look_right:
                            pass
                    self.counter_tics += 1
                    screen.blit(self.person_normal_weapon_punch_right_animation[self.now_frame % len(self.person_normal_weapon_punch_right_animation)], (self.position_x, self.position_y))
                    screen.blit(self.normal_weapon_punch_right_animation[self.now_frame%len(self.normal_weapon_punch_right_animation)], (self.position_x, self.position_y))
                else:
                    if self.counter_tics >= self.tics:
                        self.counter_tics = 0
                        self.now_frame += 1
                        if not self.look_right:
                            pass
                    self.counter_tics += 1
                    screen.blit(self.person_normal_weapon_punch_left_animation[self.now_frame % len(self.person_normal_weapon_punch_left_animation)], (self.position_x, self.position_y))
                    screen.blit(self.normal_weapon_punch_left_animation[self.now_frame%len(self.normal_weapon_punch_left_animation)],(self.position_x,self.position_y))
                if self.now_frame==len(self.normal_weapon_punch_left_animation):
                    self.normal_weapon_punch=False
                    self.now_frame=0
                    self.counter_tics=0
                    self.animation_active=False
                    self.position_y += self.normal_weapon_punch_left_animation[0].get_height() - self.person.get_height()
                    if not self.look_right:
                        self.position_x += self.normal_weapon_punch_left_animation[0].get_width() - self.person.get_width()


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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not person.animation_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    person.normal_weapon_punch = True
                    person.animation_active = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    person.look_right = True
                    person.walk = True
                    person.animation_active = True

                elif event.key == pygame.K_LEFT:
                    person.look_right = False
                    person.walk=True
                    person.animation_active = True
        elif event.type == pygame.KEYUP:
            if person.walk:
                person.walk = False
                person.animation_active= False
                person.now_frame=0
                person.counter_tics = 0
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
#просто для проверки работоспособности
