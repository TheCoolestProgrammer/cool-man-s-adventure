import pygame


class Background():
    def load_background(self, level):
        if level == 0:
            self.background = pygame.image.load("data/background2.png")
        self.background = pygame.Surface.convert_alpha(self.background)
        self.position_x = 0
        self.position_y = 0
        self.speed = 15

    def bliting(self):
        screen.blit(self.background, (self.position_x, self.position_y))


class LevelObject(pygame.sprite.Sprite):
    def __init__(self, person, weapon, x=0, y=0):
        super().__init__(all_sprites)
        self.person = False
        self.weapon = False
        if person:
            if person == 1:
                self.image = pygame.image.load("data/person1.png").convert_alpha()
            if person == 2:
                self.image = pygame.image.load("data/person2.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.person = True
            self.speed = background.speed
            self.person_number = person
        elif weapon:
            if weapon == 1:
                self.image = pygame.image.load("data/fists1.png").convert_alpha()
            if weapon == 2:
                self.image = pygame.image.load("data/fists2.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.weapon = True
            self.person_number = weapon
        self.walk = False
        self.animation_active = False
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
        self.look_right = True
        self.normal_weapon_punch = False
        self.now_frame = 0
        self.counter_tics = 0
        self.tics = fps // 5 // 2
        self.max_value_anim = 5
        self.super_punch = False
        self.jump = False
        self.v_0 = 15
        self.block= False
        self.sitting = False
        all_sprites.add(self)

    def animation(self):
        if self.counter_tics >= self.tics:
            self.counter_tics = 0
            self.now_frame += 1
            if self.person_number == 1:
                if self.person:
                    if self.walk:
                        self.max_value_anim = 5
                        self.image = pygame.image.load(f"data/person{self.person_number}_walk_anim{self.now_frame % self.max_value_anim + 1}.png")
                    elif self.normal_weapon_punch:
                        self.max_value_anim = 6
                        self.image = pygame.image.load(f"data/person{self.person_number}.png")
                    elif self.super_punch:
                        self.max_value_anim = 9
                        self.image = pygame.image.load(f"data/person{self.person_number}_sword_punch{self.now_frame % self.max_value_anim + 1}.png")
                    elif self.jump:
                        self.max_value_anim=10
                        self.image = pygame.image.load(f"data/jump_person{self.person_number}_{self.now_frame % self.max_value_anim + 1}.png")
                        self.rect.y = self.v_0*self.now_frame - 5*(self.now_frame**2)
                    elif self.block:
                        self.max_value_anim+=1
                        self.image = pygame.image.load(f"data/person{self.person_number}.png")
                    elif self.sitting:
                        self.max_value_anim += 1
                        self.image = pygame.image.load(f"data/sitting_{self.person_number}.png")
                    if not self.look_right:
                        self.image = pygame.transform.flip(self.image, True, False)
                elif self.weapon:

                    if self.walk:
                        self.max_value_anim = 5
                        self.image = pygame.image.load(f"data/fists_{self.person_number}_walk_animation{self.now_frame % self.max_value_anim + 1}.png")
                    elif self.normal_weapon_punch:
                        self.max_value_anim = 6
                        self.image = pygame.image.load(f"data/fists_{self.person_number}_punch{self.now_frame % self.max_value_anim + 1}.png")
                    elif self.super_punch:
                        self.max_value_anim = 9
                        self.image = pygame.image.load(f"data/{self.person_number}sword_punch{self.now_frame % self.max_value_anim + 1}.png")
                    elif self.jump:
                        self.max_value_anim = 10
                        self.image = pygame.image.load(f"data/jump_hands{self.person_number}_{self.now_frame % self.max_value_anim + 1}.png")
                        self.rect.y = self.v_0*self.now_frame - 5*(self.now_frame**2)
                    elif self.block:
                        self.max_value_anim+=1
                        self.image = pygame.image.load(f"data/block{self.person_number}.png")
                    elif self.sitting:
                        self.max_value_anim += 1
                        self.image = pygame.image.load(f"data/sitting_{self.person_number}.png")
                    if not self.look_right:
                        self.image = pygame.transform.flip(self.image, True, False)

                if self.max_value_anim == self.now_frame:
                    if self.normal_weapon_punch:
                        self.normal_weapon_punch = False
                        self.animation_active = False
                    elif self.super_punch:
                        self.super_punch = False
                        self.animation_active = False
                    elif self.jump:
                        self.jump=False
                        self.animation_active=False
                        self.rect.y = screen_height - 500
                    self.back(self.person,self.weapon)
                self.mask = pygame.mask.from_surface(self.image)

        self.counter_tics += 1
    def back(self,person,weapon):
        if self.person:
            if person == 1:
                self.image = pygame.image.load("data/person1.png")
            elif person == 2:
                self.image = pygame.image.load("data/person2.png")
            if not self.look_right:
                self.image = pygame.transform.flip(self.image, True, False)
        elif self.weapon:
            if weapon == 1:
                self.image = pygame.image.load("data/fists1.png")
            elif weapon == 2:
                self.image = pygame.image.load("data/fists2.png")
            if not self.look_right:
                self.image = pygame.transform.flip(self.image, True, False)
        self.now_frame=0
        self.counter_tics=0
        self.max_value_anim=5
class Effect(pygame.sprite.Sprite):
    def __init__(self,effect,x,y):
        super().__init__(effects)
        self.animation_active=False
        if effect == 1:
            self.image = pygame.image.load(f"data/sword_effects1.png")
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.now_frame = 0
            self.counter_tics = 0
            self.tics = fps // 5 // 2
            self.max_value_anim = 9
        self.look_right = True
        effects.add(self)

    def animation(self):
        print(self.now_frame,self.max_value_anim)
        if self.counter_tics >= self.tics:
            self.counter_tics = 0
            self.now_frame += 1
            self.image = pygame.image.load(f"data/sword_effects{self.now_frame % self.max_value_anim + 1}.png")
            if not level.person.look_right:
                self.image = pygame.transform.flip(self.image, True, False)
        if self.now_frame==self.max_value_anim:
            self.animation_active = False
            self.now_frame=0
            self.counter_tics=0
        self.counter_tics+=1
class Lives():
    def __init__(self,x=0, y=0):
        self.image = pygame.image.load(f"data/health_bar.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lives = 100
    def blitting(self,player):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        if player == 1:
            pygame.draw.rect(screen,(255,0,0),(8,8,int(screen_width//2/100*self.lives),34))
        elif player == 2:
            pass
            pygame.draw.rect(screen, (255, 0, 0), (screen_width//2+16, 8, int(screen_width//2/100*self.lives), 34))
class Level():
    def __init__(self, level,player1_person,player2_person):
        if level == 1:
            x = screen_width // 2 - 250
            y = screen_height - 500

            self.person = LevelObject(player1_person, False, x, y)
            self.weapon = LevelObject(False, player1_person, x, y)
            self.sword_effect = Effect(1,x,y)
            self.health_bar_player1 = Lives(0,0)

            self.person2 = LevelObject(player2_person, False, screen_width-x, y)
            self.weapon2= LevelObject(False, player2_person, screen_width-x, y)
            self.health_bar_player1 = Lives(0, 0)
            self.health_bar_player2 = Lives(screen_width//2,0)
class MainMenuObject(pygame.sprite.Sprite):
    def __init__(self, value, x=0, y=0):
        super().__init__(all_sprites)

        if value == 0 or value == 4 or value == 5:
            self.image = pygame.image.load("data/menu_button.png")
        elif value == 1:
            self.image = pygame.image.load("data/menu_button_up_down.png")
        elif value == 2:
            self.image = pygame.image.load("data/menu_button_up_down.png")
            self.image = pygame.transform.flip(self.image, False, True)
        elif value == -1:
            self.image = pygame.Surface((1, 1))
        self.rect = self.image.get_rect()
        if value == -1:
            self.rect.x = x
            self.rect.y = y
            self.mask = pygame.mask.from_surface(self.image)
        else:
            if value == 4:
                self.rect.x = 900
                self.rect.y = 450
            elif value == 5:
                self.rect.x = 900
                self.rect.y = 550
            elif menu.slide == 0:
                if value == 0:
                    self.rect.x = screen_width // 2 - (self.image.get_width() // 2)
                    self.rect.y = 500
                elif value == 1:
                    self.rect.x = screen_width // 2 - (self.image.get_width() // 2)
                    self.rect.y = 400
                elif value == 2:
                    self.rect.x = screen_width // 2 - (self.image.get_width() // 2)
                    self.rect.y = 650
            elif menu.slide == 1:
                if value == 0:
                    self.rect.x = screen_width // 2 - (self.image.get_width() // 2)
                    self.rect.y = screen_height // 2 - (self.image.get_height() // 2)
                elif value == 1:
                    self.rect.x = screen_width // 2 - (self.image.get_width() // 2)
                    self.rect.y = menu.button.rect.y - 20 - self.image.get_height()
                elif value == 2:
                    self.rect.x = screen_width // 2 - (self.image.get_width() // 2)
                    self.rect.y = screen_height//2+(screen_height//2 -menu.button.rect.y) + 20 + self.image.get_height()
            elif menu.slide == 2:

                if value == 1:
                    self.image = pygame.transform.rotate(self.image,90)
                elif value == 2:
                    self.image = pygame.transform.rotate(self.image,90)
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y

            self.mask = pygame.mask.from_surface(self.image)
            all_sprites.add(self)


class Main_menu():
    def load_image(self, slide):
        self.slide = slide
        if self.slide == 0:
            self.background = pygame.image.load("data/menu_background.png")
            self.background = pygame.Surface.convert_alpha(self.background)
            self.button = MainMenuObject(0)
            self.button_up = MainMenuObject(1)
            self.button_down = MainMenuObject(2)
            self.active_button = 0
            self.animation_active = False
            self.now_frame = 1
            self.counter_tics = 0
            self.tics = fps / 12
        elif self.slide == 1:
            self.background = pygame.image.load("data/menu_background2.png")
            self.background = pygame.Surface.convert_alpha(self.background)
            self.button = MainMenuObject(0)
            self.button_up = MainMenuObject(1)
            self.button_down = MainMenuObject(2)
            self.active_button = 0
            self.animation_active = False
            self.now_frame = 1
            self.counter_tics = 0
            self.tics = fps / 12
        elif self.slide == 2:
            self.background = pygame.image.load("data/menu_background2.png")
            self.background = pygame.Surface.convert_alpha(self.background)
            self.button_left_1 = MainMenuObject(1,20,screen_height-150)
            self.button_right_1 = MainMenuObject(2,80, screen_height-150)
            self.button_left_2 = MainMenuObject(1,screen_width-130,screen_height-150)
            self.button_right_2 = MainMenuObject(2,screen_width-70,screen_height-150)
            self.button = MainMenuObject(0,screen_width//2-320,screen_height-100)
            self.active_button = 0
            self.animation_active = False
            self.now_frame = 1
            self.counter_tics = 0
            self.tics = fps / 12
    def bliting(self):

        screen.blit(self.background, (0, 0))
        all_sprites.draw(screen)
        all_sprites.update(screen)
        if self.slide == 0:
            if self.active_button == 0:
                text = font.render("MULTIPLAYER", True, (0, 255, 0))
            elif self.active_button == 1:
                text = font.render("SINGLEPLAYER", True, (0, 255, 0))
            elif self.active_button == 2:
                text = font.render("OPTIONS", True, (0, 255, 0))
            elif self.active_button == 3:
                text = font.render("EXIT", True, (0, 255, 0))
            screen.blit(text, (screen_width // 8 * 3, 520))
        elif self.slide == 1:
            if self.active_button == 0:
                text = font.render("LOCAL", True, (0, 255, 0))
            elif self.active_button == 1:
                text = font.render("ENTERNET", True, (0, 255, 0))
            elif self.active_button == 2:
                text = font.render("EXIT", True, (0, 255, 0))
            screen.blit(text, (menu.button.rect.x+menu.button.rect.x//8*6,menu.button.rect.y))
        else:
            image = pygame.image.load(f"data/shadow.png")
            screen.blit(image, (0, 0))
            screen.blit(image, (screen_width - 400, 0))
            image = pygame.image.load(f"data/person{hero%heroes_list_len+1}.png")
            screen.blit(image,(0,0))

            image=  pygame.image.load(f"data/fists{hero%heroes_list_len+1}.png")
            screen.blit(image,(0,0))

            image = pygame.image.load(f"data/person{hero2 % heroes_list_len + 1}.png")
            image = pygame.transform.flip(image, True, False)
            screen.blit(image, (screen_width-400, 0))

            image = pygame.image.load(f"data/fists{hero2%heroes_list_len+1}.png")
            image = pygame.transform.flip(image,True,False)
            screen.blit(image, (screen_width-400, 0))
            text = font.render("ACCEPT", True, (0, 255, 0))
            screen.blit(text, (menu.button.rect.x+menu.button.rect.x//2, menu.button.rect.y))
        self.animation_up = False

    def animation(self):
        if self.slide == 0 or self.slide==1:
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
                    self.button.image = pygame.image.load(
                        f"data/menu_button_animation{self.now_frame % 12 + self.speed_animation}.png")
                    self.now_frame += self.speed_animation
                self.counter_tics += 1

                if self.now_frame == self.max_frames:
                    self.animation_active = False
                    self.counter_tics = 0
                    self.animation_up = False

class Game_over(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(game_overs)
        self.tics = fps // 5
        self.max_value_anim = 12
        self.now_frame=1
        self.counter_ticks = 0
        self.image = pygame.image.load(f"data/game_over{self.now_frame}.png")

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        game_overs.add(self)
    def animation(self):
        if self.now_frame<self.max_value_anim:
            if self.counter_ticks ==self.tics:
                self.counter_ticks=0
                self.now_frame+=1
                self.image = pygame.image.load(f"data/game_over{self.now_frame}.png")
            self.counter_ticks+=1
running = True
pygame.init()
pygame.display.set_caption('the cool man adventure')
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
fps = 30
clock = pygame.time.Clock()
font = pygame.font.SysFont("Times New Roman", 50)
heroes_list_len = 2
hero = 0
hero2 = 0
game_mode = 0

while running:
    if game_mode == 3:
        all_sprites = pygame.sprite.Group()
        effects = pygame.sprite.Group()
        game_overs = pygame.sprite.Group()
        game_over = Game_over()
        background = Background()
        background.load_background(0)
        level = Level(1,1,2)
        game_runnung = True
        winner = False

        while game_runnung:
            if not winner:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        game_mode = -1
                        game_runnung=False
                    if not level.person2.animation_active or not level.weapon2.animation_active:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_u:
                                level.person2.normal_weapon_punch = True
                                level.weapon2.normal_weapon_punch = True
                                level.person2.animation_active = True
                                level.weapon2.animation_active = True
                            if event.key == pygame.K_h:
                                level.person2.block = True
                                level.weapon2.block = True
                                level.person2.animation_active = True
                                level.weapon2.animation_active = True
                            if event.key == pygame.K_k:
                                level.person2.animation_active = True
                                level.weapon2.animation_active = True
                                level.person2.sitting = True
                                level.weapon2.sitting = True

                            if event.key == pygame.K_i:
                                level.person2.animation_active = True
                                level.weapon2.animation_active = True
                                level.person2.jump = True
                                level.weapon2.jump = True
                            if event.key == pygame.K_o:
                                level.person2.super_punch = True
                                level.weapon2.super_punch = True
                                level.person2.animation_active = True
                                level.weapon2.animation_active = True
                                level.sword_effect.animation_active = True
                            if event.key == pygame.K_l:
                                level.person2.look_right = True
                                level.weapon2.look_right = True
                                level.person2.back(level.person.person, False)
                                level.weapon2.back(False, level.weapon.weapon)
                                level.person2.walk = True
                                level.weapon2.walk = True
                                level.person2.animation_active = True
                                level.weapon2.animation_active = True
                            elif event.key == pygame.K_j:
                                level.person2.look_right = False
                                level.weapon2.look_right = False
                                level.person2.back(level.person.person, False)
                                level.weapon2.back(False, level.weapon.weapon)
                                level.person2.walk = True
                                level.weapon2.walk = True
                                level.person2.animation_active = True
                                level.weapon2.animation_active = True
                    if not level.person.animation_active or not level.weapon.animation_active:

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_e:
                                level.person.normal_weapon_punch = True
                                level.weapon.normal_weapon_punch = True
                                level.person.animation_active = True
                                level.weapon.animation_active = True

                            if event.key == pygame.K_f:
                                level.person.block = True
                                level.weapon.block = True
                                level.person.animation_active = True
                                level.weapon.animation_active = True

                            if event.key == pygame.K_s:
                                level.person.animation_active = True
                                level.weapon.animation_active = True
                                level.person.sitting = True
                                level.weapon.sitting = True

                            if event.key == pygame.K_SPACE:
                                level.person.animation_active = True
                                level.weapon.animation_active = True
                                level.person.jump = True
                                level.weapon.jump = True

                            if event.key == pygame.K_q:
                                level.person.super_punch=True
                                level.weapon.super_punch=True
                                level.person.animation_active = True
                                level.weapon.animation_active = True
                                level.sword_effect.animation_active=True

                            if event.key == pygame.K_d:
                                level.person.look_right = True
                                level.weapon.look_right = True
                                level.person.back(level.person.person, False)
                                level.weapon.back(False, level.weapon.weapon)
                                level.person.walk = True
                                level.weapon.walk = True
                                level.person.animation_active = True
                                level.weapon.animation_active = True

                            elif event.key == pygame.K_a:
                                level.person.look_right = False
                                level.weapon.look_right = False
                                level.person.back(level.person.person, False)
                                level.weapon.back(False, level.weapon.weapon)
                                level.person.walk = True
                                level.weapon.walk = True
                                level.person.animation_active = True
                                level.weapon.animation_active = True
                    if event.type == pygame.KEYUP:
                        if level.person.walk and (event.key == pygame.K_d or event.key == pygame.K_a):
                            level.person.walk = False
                            level.weapon.walk = False
                            level.person.animation_active = False
                            level.weapon.animation_active = False
                            level.person.back(level.person.person, False)
                            level.weapon.back(False, level.weapon.weapon)
                        if level.person2.walk and (event.key == pygame.K_j or event.key == pygame.K_l):
                            level.person2.walk = False
                            level.weapon2.walk = False
                            level.person2.animation_active = False
                            level.weapon2.animation_active = False
                            level.person2.back(level.person2.person, False)
                            level.weapon2.back(False, level.weapon2.weapon)
                        if level.person.sitting and event.key == pygame.K_s:
                            level.person.sitting = False
                            level.weapon.sitting= False
                            level.person.animation_active = False
                            level.weapon.animation_active = False
                            level.person.back(level.person.person, False)
                            level.weapon.back(False, level.weapon.weapon)
                        if level.person2.sitting and event.key == pygame.K_k:
                            level.person2.sitting = False
                            level.weapon2.sitting= False
                            level.person2.animation_active = False
                            level.weapon2.animation_active = False
                            level.person2.back(level.person2.person, False)
                            level.weapon2.back(False, level.weapon2.weapon)
                        if event.key == pygame.K_f and level.person.block:
                            level.person.block = False
                            level.weapon.block = False
                            level.person.animation_active = False
                            level.weapon.animation_active = False
                            level.person.back(level.person.person,False)
                            level.weapon.back(False,level.weapon.weapon)
                        if event.key == pygame.K_h and level.person2.block:
                            level.person2.block = False
                            level.weapon2.block = False
                            level.person2.animation_active = False
                            level.weapon2.animation_active = False
                            level.person2.back(level.person2.person,False)
                            level.weapon2.back(False,level.weapon2.weapon)
                keys = pygame.key.get_pressed()

                if level.person.animation_active:
                    if level.person.walk or level.person.jump:

                        if keys[pygame.K_a]:
                            level.person.rect.x -= level.person.speed
                            level.weapon.rect.x -= level.person.speed
                            level.sword_effect.rect.x -= level.person.speed
                        elif keys[pygame.K_d]:
                            level.person.rect.x += level.person.speed
                            level.weapon.rect.x += level.person.speed
                            level.sword_effect.rect.x +=level.person.speed
                    level.person.animation()
                    level.weapon.animation()
                if level.person2.animation_active:
                    if level.person2.walk or level.person2.jump:
                        if keys[pygame.K_j]:
                            level.person2.rect.x -= level.person.speed
                            level.weapon2.rect.x -= level.person.speed
                            level.sword_effect.rect.x -= level.person.speed
                        elif keys[pygame.K_l]:
                            level.person2.rect.x += level.person.speed
                            level.weapon2.rect.x += level.person.speed
                            level.sword_effect.rect.x += level.person.speed
                    level.person2.animation()
                    level.weapon2.animation()
                if pygame.sprite.collide_mask(level.person, level.weapon2) and level.weapon2.animation_active and not level.person2.walk:
                    level.health_bar_player1.lives-=2
                elif pygame.sprite.collide_mask(level.person2, level.weapon) and level.weapon.animation_active and not level.person.walk:
                    level.health_bar_player2.lives -= 2
                if level.health_bar_player2.lives<=0:
                    winner = "player 1"
                elif level.health_bar_player1.lives<=0:
                    winner = "player 2"
                if winner:
                    all_sprites = pygame.sprite.Group()
                    button1 = MainMenuObject(4)
                    button2 = MainMenuObject(5)
                screen.fill((0, 0, 0))
                background.bliting()
                if level.sword_effect.animation_active:
                    level.sword_effect.animation()
                    effects.draw(screen)
                    effects.update(screen)
                all_sprites.draw(screen)
                all_sprites.update(screen)
                level.health_bar_player1.blitting(1)
                level.health_bar_player2.blitting(2)
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        game_mode = -1
                        game_runnung=False
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        if event.button ==1:
                            x, y = pygame.mouse.get_pos()
                            mouse = MainMenuObject(-1, x, y)
                            if pygame.sprite.collide_mask(button1, mouse):
                                game_mode = 0
                                game_runnung=False
                            if pygame.sprite.collide_mask(button2, mouse):
                                game_mode = 2
                                game_runnung=False
                game_overs.draw(screen)
                game_over.animation()
                if game_over.now_frame >=12:
                    all_sprites.draw(screen)
                    all_sprites.update(screen)
                    text = font.render("escape in menu", True, (0, 255, 0))
                    screen.blit(text, (900, 450))
                    text = font.render("fight again", True, (0, 255, 0))
                    screen.blit(text, (900, 550))
                    text = font.render(f"winner is {winner}", True, (0, 255, 0))
                    screen.blit(text, (900, 250))
                    if winner == "player 1":
                        text = font.render(f"scores: {level.health_bar_player1.lives*100}", True, (0, 255, 0))
                    else:
                        text = font.render(f"scores: {level.health_bar_player2.lives*100}", True, (0, 255, 0))
                    screen.blit(text, (900, 350))
            pygame.display.update((0, 0, screen_width, screen_height))
            clock.tick(fps)
            pygame.display.set_caption(str(clock.get_fps()))
    elif game_mode== 0 or game_mode==1 or game_mode==2:
        all_sprites = pygame.sprite.Group()
        menu = Main_menu()
        menu.load_image(game_mode)
        menu_running = True
        if game_mode == 0:
            buttons_count = 4
        elif game_mode == 1:
            buttons_count=3
        else:
            buttons_count=1
        while menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    menu_running=False
                    game_mode = -1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = pygame.mouse.get_pos()
                        mouse = MainMenuObject(-1, x, y)
                        if game_mode<2:
                            if not menu.animation_active:
                                if pygame.sprite.collide_mask(menu.button_up, mouse):
                                    print("moving up")
                                    menu.active_button -= 1
                                    menu.active_button %= buttons_count
                                    menu.animation_active = True
                                    menu.animation_up = True
                                elif pygame.sprite.collide_mask(menu.button_down, mouse):
                                    print("moving down")
                                    menu.active_button += 1
                                    menu.active_button %= buttons_count
                                    menu.animation_active = True
                                    menu.animation_up = False
                                elif pygame.sprite.collide_mask(menu.button, mouse):
                                    if game_mode==0:
                                        if menu.active_button==0:
                                            game_mode = 1
                                            menu_running= False
                                        elif menu.active_button==3:
                                            game_mode = -1
                                            menu_running= False
                                            running = False
                                    else:
                                        if menu.active_button == 0:
                                            game_mode=2
                                            menu_running=False
                                        if menu.active_button == 2:
                                            game_mode = 0
                                            menu_running = False
                        else:
                            if pygame.sprite.collide_mask(menu.button_left_1, mouse):
                                hero-=1
                            elif pygame.sprite.collide_mask(menu.button_right_1, mouse):
                                hero+=1
                            if pygame.sprite.collide_mask(menu.button_left_2, mouse):
                                hero2-=1
                            elif pygame.sprite.collide_mask(menu.button_right_2, mouse):
                                hero2+=1
                            elif pygame.sprite.collide_mask(menu.button, mouse):
                                menu_running=False
                                game_mode=3
            if menu.animation_active:
                menu.animation()
            menu.bliting()
            pygame.display.update((0, 0, screen_width, screen_height))
            clock.tick(fps)
            pygame.display.set_caption(str(clock.get_fps()))
