import pygame

class Background():
    def load_background(self,level):
        if level==0:
            self.background = pygame.image.load("data/background2.png")
        self.background = pygame.Surface.convert_alpha(self.background)
        self.position_x = 0
        self.position_y = 0
        self.speed = 3
    def bliting(self):
        screen.blit(self.background, (self.position_x, self.position_y))

class Person():
    def load_person(self,person):
        if person ==0:
            self.person = pygame.image.load("data/person.png")
            self.person = pygame.Surface.convert_alpha(self.person)
            self.person_look_left = pygame.transform.flip(self.person,True,False)
            self.weapon = pygame.image.load("data/sword.png")
            self.weapon = pygame.Surface.convert_alpha(self.weapon)
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
                a = pygame.Surface.convert_alpha(a)
                self.walk_right_animation.append(a)
                a = pygame.transform.flip(a,True,False)
                a = pygame.Surface.convert_alpha(a)
                self.walk_left_animation.append(a)
            self.tics = fps // len(self.walk_right_animation)//2
            self.counter_tics = 0

            self.person_normal_weapon_punch_right_animation = []
            self.person_normal_weapon_punch_left_animation = []
            self.normal_weapon_punch_right_animation = []
            self.normal_weapon_punch_left_animation = []
            for i in range(1,10):
                a = pygame.image.load(f"data/person_sword_punch{i}.png")
                a = pygame.Surface.convert_alpha(a)
                self.person_normal_weapon_punch_right_animation.append(a)
                a = pygame.transform.flip(a, True, False)
                a = pygame.Surface.convert_alpha(a)
                self.person_normal_weapon_punch_left_animation.append(a)
            for i in range(1,10):
                a = pygame.image.load(f"data/sword_punch{i}.png")
                a = pygame.Surface.convert_alpha(a)
                self.normal_weapon_punch_right_animation.append(a)
                a = pygame.transform.flip(a, True, False)
                a = pygame.Surface.convert_alpha(a)
                self.normal_weapon_punch_left_animation.append(a)


        self.position_x = screen_width//2-(self.person.get_width()//2)
        self.position_y = screen_height-self.person.get_height()-10
        self.speed = background.speed

    def ticks_plus(self):
        if self.counter_tics >= self.tics:
            self.counter_tics = 0
            self.now_frame += 1
            if not self.look_right:
                pass
        self.counter_tics += 1
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
                    self.ticks_plus()
                    screen.blit(self.walk_right_animation[self.now_frame%5], (self.position_x, self.position_y))
                    screen.blit(self.weapon, (self.position_x, self.position_y))
                else:
                    self.ticks_plus()

                    screen.blit(self.walk_left_animation[self.now_frame%5], (self.position_x, self.position_y))
                    screen.blit(self.weapon_look_left, (self.position_x-(self.weapon.get_width()-self.person.get_width()), self.position_y))


            elif self.normal_weapon_punch:
                if self.counter_tics==0:
                    # self.tics=fps//len(self.normal_weapon_punch_left_animation)
                    self.position_y -= self.normal_weapon_punch_left_animation[0].get_height() - self.person.get_height()
                    if not self.look_right:
                        self.position_x -= self.normal_weapon_punch_left_animation[0].get_width() - self.person.get_width()
                if self.look_right:
                    self.ticks_plus()

                    screen.blit(self.person_normal_weapon_punch_right_animation[self.now_frame % len(self.person_normal_weapon_punch_right_animation)], (self.position_x, self.position_y))
                    screen.blit(self.normal_weapon_punch_right_animation[self.now_frame%len(self.normal_weapon_punch_right_animation)], (self.position_x, self.position_y))
                else:
                    self.ticks_plus()

                    screen.blit(self.person_normal_weapon_punch_left_animation[self.now_frame % len(self.person_normal_weapon_punch_left_animation)], (self.position_x, self.position_y))
                    screen.blit(self.normal_weapon_punch_left_animation[self.now_frame%len(self.normal_weapon_punch_left_animation)],(self.position_x,self.position_y))
                if self.now_frame==len(self.normal_weapon_punch_left_animation):
                    self.normal_weapon_punch=False
                    self.now_frame=0
                    self.counter_tics=0
                    self.animation_active=False
                    self.position_y += self.normal_weapon_punch_left_animation[0].get_height() - self.person.get_height()
                    # self.tics = fps//len(self.walk_right_animation)
                    if not self.look_right:
                        self.position_x += self.normal_weapon_punch_left_animation[0].get_width() - self.person.get_width()

class Main_menu_object(pygame.sprite.Sprite):
    def __init__(self,value,x=0,y=0):
        super().__init__(all_sprites)

        if value == 0:
            self.image = pygame.image.load("data/menu_button.png")
        elif value == 1:
            self.image = pygame.image.load("data/menu_button_up_down.png")
        elif value == 2:
            self.image = pygame.image.load("data/menu_button_up_down.png")
            self.image = pygame.transform.flip(self.image,False,True)
        elif value == -1:
            self.image = pygame.Surface((1,1))
        self.rect = self.image.get_rect()
        if value == -1:
            self.rect.x = x
            self.rect.y = y
            self.mask = pygame.mask.from_surface(self.image)
        else:
            if value == 0:
                self.rect.x = screen_width // 2 - (self.image.get_width() // 2)
                self.rect.y = 500
            elif value == 1:
                self.rect.x = screen_width // 2 - (self.image.get_width() // 2)
                self.rect.y = 400
            elif value == 2:
                self.rect.x = screen_width // 2 - (self.image.get_width() // 2)
                self.rect.y = 650

            self.mask = pygame.mask.from_surface(self.image)
            all_sprites.add(self)
class Main_menu():
    def load_image(self,slide):
        self.slide = slide
        if self.slide ==0:
            self.background = pygame.image.load("data/menu_background.png")
            self.background = pygame.Surface.convert_alpha(self.background)
            self.button=Main_menu_object(0)

            self.button_up = Main_menu_object(1)
            self.button_down = Main_menu_object(2)
            self.active_button = 0
            self.animation_active = False
            self.now_frame =1
            self.counter_tics = 0
            self.tics = fps/12
    def bliting(self):
        if self.slide==0:
            screen.blit(self.background,(0,0))
            all_sprites.draw(screen)
            all_sprites.update(screen)
            if self.active_button == 0:
                text = font.render("MULTIPLAYER", True, (0, 255, 0))
            elif self.active_button == 1:
                text = font.render("SINGLEPLAYER", True, (0, 255, 0))
            elif self.active_button==2:
                text = font.render("OPTIONS", True, (0, 255, 0))
            elif self.active_button==3:
                text = font.render("EXIT", True, (0, 255, 0))
            screen.blit(text, (screen_width//8*3, 520))
            self.animation_up = False

    def animation(self):
        if self.slide == 0:
            if self.animation_active:
                if self.counter_tics == 0:
                    if self.animation_up:
                        self.now_frame = 11
                        self.max_frames = 1
                        self.speed_animation = -1
                    else:
                        self.now_frame = 1
                        self.max_frames = 12
                        self.speed_animation = 1
                if self.counter_tics >= self.tics:
                    self.counter_tics = 0
                    self.button.image = pygame.image.load(f"data/menu_button_animation{self.now_frame % 12 + self.speed_animation}.png")
                    self.now_frame += self.speed_animation
                self.counter_tics += 1

                if self.now_frame == self.max_frames:
                    self.animation_active = False
                    self.counter_tics = 0
                    self.animation_up=False
running = True
pygame.init()
pygame.display.set_caption('the cool man adventure')
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
fps = 120
clock = pygame.time.Clock()
font = pygame.font.SysFont("Times New Roman", 50)

game_mode = 0

if game_mode==1:
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
        if person.walk:
            if keys[pygame.K_LEFT]:
                background.position_x += background.speed
            elif keys[pygame.K_RIGHT]:
                background.position_x -= background.speed

        screen.fill((0, 0, 0))
        background.bliting()
        person.bliting()
        pygame.display.update((0,0,screen_width,screen_height))
        clock.tick(fps)
        pygame.display.set_caption(str(clock.get_fps()))
else:
    all_sprites = pygame.sprite.Group()
    menu = Main_menu()
    menu.load_image(0)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x,y = pygame.mouse.get_pos()
                    mouse = Main_menu_object(-1,x,y)
                    if menu.slide==0:
                        if not menu.animation_active:
                            if pygame.sprite.collide_mask(menu.button_up,mouse):
                                print("moving up")
                                menu.active_button +=1
                                menu.active_button%= 4
                                menu.animation_active=True
                                menu.animation_up = True
                            elif pygame.sprite.collide_mask(menu.button_down,mouse):
                                print("moving down")
                                menu.active_button -= 1
                                menu.active_button %= 4
                                menu.animation_active = True
                                menu.animation_up=False
                            elif pygame.sprite.collide_mask(menu.button,mouse):
                                print("go to level or sth")
        if menu.animation_active:
            menu.animation()
        menu.bliting()
        pygame.display.update((0, 0, screen_width, screen_height))
        clock.tick(fps)
        pygame.display.set_caption(str(clock.get_fps()))
