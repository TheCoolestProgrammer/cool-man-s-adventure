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
class Level_object(pygame.sprite.Sprite):

    def __init__(self, person,weapon,x = 0,y=0):
        super().__init__(all_sprites)
        self.person = False
        self.weapon = False
        if person:
            if person == 1:
                self.image = pygame.image.load("data/person.png")
                self.image = pygame.Surface.convert_alpha(self.image)
            self.rect = self.image.get_rect()
            self.person=True
            self.walk = False

            self.speed = background.speed
            self.person_number = person
        elif weapon:
            if weapon == 1:
                self.image = pygame.image.load("data/sword.png")
                self.image = pygame.Surface.convert_alpha(self.image)
            self.rect = self.image.get_rect()
            self.weapon=True
            self.person_number = weapon
        self.animation_active = False
        self.rect.x =x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
        self.look_right = True
        self.normal_weapon_punch = False
        self.now_frame = 0
        self.counter_tics = 0
        self.tics = fps // 5 // 2
        self.max_value_anim = 5
        all_sprites.add(self)
    def animation(self):

        if self.counter_tics >= self.tics:
            self.counter_tics = 0
            self.now_frame += 1
            if self.person_number==1:
                if self.person:
                    if self.walk:
                        self.max_value_anim = 5
                        self.image = pygame.image.load(f"data/person_walk_anim{self.now_frame%5+1}.png")
                    elif self.normal_weapon_punch:
                        self.max_value_anim = 9
                        self.image = pygame.image.load(f"data/person_sword_punch{self.now_frame%9+1}.png")
                    if not self.look_right:
                        self.image = pygame.transform.flip(self.image,True,False)
                elif self.weapon:
                    if self.animation_active:
                        if self.normal_weapon_punch:
                            self.max_value_anim = 9
                            self.image= pygame.image.load(f"data/sword_punch{self.now_frame%9+1}.png")
                        if not self.look_right:
                            self.image = pygame.transform.flip(self.image, True, False)



                if self.max_value_anim==self.now_frame:
                    self.now_frame=0
                    self.counter_tics=0
                    if self.normal_weapon_punch:
                        self.animation_active=False
                        self.normal_weapon_punch=False

                    if self.person:
                        self.image = pygame.image.load("data/person.png")
                        if not self.look_right:
                            self.image = pygame.transform.flip(self.image, True, False)
                    elif self.weapon:
                        self.image = pygame.image.load("data/sword.png")
                        if not self.look_right:
                            self.image = pygame.transform.flip(self.image, True, False)

        self.counter_tics += 1

class Level():
    def __init__(self,level):
        if level ==1:
            x = screen_width // 2 - 250
            y = screen_height - 500
            self.person = Level_object(1,False,x,y)
            self.weapon = Level_object(False,1,x,y)


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
while running:
    if game_mode==1:
        all_sprites = pygame.sprite.Group()
        background = Background()
        background.load_background(0)
        level = Level(1)
        while game_mode==1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_mode=-1
                if not level.person.animation_active:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            level.person.normal_weapon_punch = True
                            level.weapon.normal_weapon_punch = True
                            level.person.animation_active = True
                            level.weapon.animation_active = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            level.person.look_right = True
                            level.weapon.look_right = True
                            level.person.walk = True
                            level.person.animation_active = True
                            level.person.image = pygame.image.load("data/person.png")
                            level.weapon.image = pygame.image.load("data/sword.png")
                        elif event.key == pygame.K_LEFT:
                            level.person.look_right = False
                            level.weapon.look_right = False
                            level.person.image = pygame.image.load("data/person.png")
                            level.weapon.image = pygame.image.load("data/sword.png")
                            level.person.image = pygame.transform.flip(level.person.image, True, False)
                            level.weapon.image = pygame.transform.flip(level.weapon.image, True, False)
                            level.person.walk=True
                            level.person.animation_active = True
                elif event.type == pygame.KEYUP:
                    if level.person.walk:
                        level.person.walk = False
                        level.person.animation_active= False
                        level.weapon.animation_active = False
                        level.person.now_frame=0
                        level.person.counter_tics = 0
                        level.weapon.now_frame = 0
                        level.weapon.counter_tics = 0
                        # level.person.image=pygame.image.load("data/person.png")
                        # level.weapon.image = pygame.image.load("data/sword.png")
                        # if not level.person.look_right:
                        #     level.person.image = pygame.transform.flip(level.person.image, True, False)
                        #     level.weapon.image = pygame.transform.flip(level.weapon.image, True, False)
            keys = pygame.key.get_pressed()

            if level.person.animation_active:
                if level.person.walk:
                    if keys[pygame.K_LEFT]:
                        background.position_x += background.speed
                    elif keys[pygame.K_RIGHT]:
                        background.position_x -= background.speed

                level.person.animation()
                level.weapon.animation()
            screen.fill((0, 0, 0))
            background.bliting()
            all_sprites.draw(screen)
            all_sprites.update(screen)
            pygame.display.update((0,0,screen_width,screen_height))
            clock.tick(fps)
            pygame.display.set_caption(str(clock.get_fps()))
    else:
        all_sprites = pygame.sprite.Group()
        menu = Main_menu()
        menu.load_image(0)
        while game_mode == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_mode=-1
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
                                    game_mode=1

            if menu.animation_active:
                menu.animation()
            menu.bliting()
            pygame.display.update((0, 0, screen_width, screen_height))
            clock.tick(fps)
            pygame.display.set_caption(str(clock.get_fps()))
