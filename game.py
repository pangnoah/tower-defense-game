import pygame
from background import background
from yellow_alien import YellowAlien
from blue_alien import BlueAlien
from green_alien import GreenAlien
from pink_alien import PinkAlien
from gun_tower import GunTower
from machine_gun_tower import MachineGunTower
from double_gun_tower import DoubleGunTower
from button import Button
import os

pygame.font.init()
pygame.display.set_caption('Defend Against Aliens')

image = pygame.image.load(os.path.join("assets", "tileRed_36.png"))
heart = pygame.transform.scale(image, (50, 46))
image1 = pygame.image.load(os.path.join("assets", "coin_16.png"))
coin = pygame.transform.scale(image1, (48, 48))
price_coin = pygame.transform.scale(image1, (24, 24))
image2 = pygame.image.load(os.path.join("assets", "towericon1.png"))
tower_icon1 = pygame.transform.scale(image2, (82, 82))
image3 = pygame.image.load(os.path.join("assets", "towericon2.png"))
tower_icon2 = pygame.transform.scale(image3, (82, 82))
image4 = pygame.image.load(os.path.join("assets", "towericon3.png"))
tower_icon3 = pygame.transform.scale(image4, (82, 82))
image5 = pygame.image.load(os.path.join("assets", "tileBlue_31.png"))
image6 = pygame.transform.rotate(image5, 270)
wave_button = pygame.transform.scale(image6, (50, 50))

enemy_waves = [[0, 0, 0, 0],
[5, 0, 0, 0],
[10, 0, 0, 0],
[5, 1, 0, 0],
[10, 5, 0, 0],
[5, 10, 1, 0],
[10, 10, 5, 0],
[5, 5, 15, 0],
[0, 10, 10, 2],
[0, 5, 10, 6],
[0, 0, 0, 16]]

class Game():
    def __init__(self):
        self.width = 1088
        self.height = 704
        self.window = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.towers = []
        self.hearts = 20
        self.coins = 600
        self.large_font = pygame.font.SysFont("TimesNewRoman", 36)
        self.coin_font = pygame.font.SysFont("TimesNewRoman", 24)
        self.button_font = pygame.font.SysFont("TimesNewRoman", 26)
        self.game_over_font = pygame.font.SysFont("TimesNewRoman", 80)
        self.moving_tower = None
        self.range = 150
        self.wave = 1
        self.current_wave = enemy_waves[self.wave]
        self.time = pygame.time.get_ticks()
        self.next_wave = False

    def run(self):
        run = True
        clock = pygame.time.Clock()
        retry_button = Button((100, 149, 237), 244, 402, 250, 100, 'Play Again')
        quit_button = Button((100, 149, 237), 594, 402, 250, 100, 'Quit Game')
        
        while run:
            clock.tick(300)
            pos = pygame.mouse.get_pos()

            if self.wave > 10:
                self.draw()
                self.game_won()
                retry_button.draw_button(self.window, (0, 0, 0))
                quit_button.draw_button(self.window, (0, 0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEMOTION:
                        if retry_button.on_button(pos):
                            retry_button.color = (50, 205, 50)
                        elif quit_button.on_button(pos):
                            quit_button.color = (50, 205, 50)
                        else:
                            retry_button.color = (100, 149, 237)
                            quit_button.color = (100, 149, 237)
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if retry_button.on_button(pos):
                            self.reset_game()
                        elif quit_button.on_button(pos):
                            run = False

                    if event.type == pygame.QUIT:
                        run = False

            elif self.hearts >= 1:
                if self.next_wave:
                    if pygame.time.get_ticks() - self.time >= 1000:
                        self.time = pygame.time.get_ticks()
                        self.spawn_enemies()

                if self.moving_tower:
                    self.moving_tower.move(pos[0] - 32, pos[1] + 32)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pos[0] >= 963 and pos[0] <= 1045 and pos[1] >= 195 and pos[1] <= 277:
                            if self.coins >= 300:
                                pos = pygame.mouse.get_pos()
                                obj = GunTower(pos[0],pos[1])
                                self.moving_tower = obj
                                self.coins -= 300
                        elif pos[0] >= 963 and pos[0] <= 1045 and pos[1] >= 325 and pos[1] <= 407:
                            if self.coins >= 500:
                                pos = pygame.mouse.get_pos()
                                obj = MachineGunTower(pos[0],pos[1])
                                self.moving_tower = obj
                                self.coins -= 500
                        elif pos[0] >= 963 and pos[0] <= 1045 and pos[1] >= 455 and pos[1] <= 537:
                            if self.coins >= 850:
                                pos = pygame.mouse.get_pos()
                                obj = DoubleGunTower(pos[0],pos[1])
                                self.moving_tower = obj
                                self.coins -= 850
                        elif pos[0] >= 940 and pos[1] >= 590:
                            self.next_wave = True
                            
                        else:
                            if self.moving_tower:
                                self.towers.append(obj)
                                self.moving_tower = None
                        
                for enemy in self.enemies:
                    if enemy.x < -5:
                        self.enemies.remove(enemy)
                        self.hearts -= 1
                    
                for tower in self.towers:
                    self.coins += tower.attack(self.enemies)
                    
                self.draw()
            
            elif self.hearts <= 0:
                self.draw()
                self.game_over()
                retry_button.draw_button(self.window, (0, 0, 0))
                quit_button.draw_button(self.window, (0, 0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEMOTION:
                        if retry_button.on_button(pos):
                            retry_button.color = (50, 205, 50)
                        elif quit_button.on_button(pos):
                            quit_button.color = (50, 205, 50)
                        else:
                            retry_button.color = (100, 149, 237)
                            quit_button.color = (100, 149, 237)
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if retry_button.on_button(pos):
                            self.reset_game()
                        elif quit_button.on_button(pos):
                            run = False

                    if event.type == pygame.QUIT:
                        run = False

            
            
            pygame.display.update()

        pygame.quit()

    def draw(self):
        background()

        for tw in self.towers:
            tw.draw(self.window)

        for en in self.enemies:
            en.draw(self.window)

        self.window.blit(heart, (935, 20))
        self.window.blit(coin, (935, 80))
        heart_text = self.large_font.render(str(self.hearts), 1, (0,0,128))
        self.window.blit(heart_text, (998, 23))
        coins_text = self.large_font.render(str(self.coins), 1, (0,0,128))
        self.window.blit(coins_text, (990, 85))
        wave_text = self.large_font.render("Wave " + str(self.wave), 1, (0,0,128))
        self.window.blit(wave_text, (948, 140))

        self.window.blit(tower_icon1, (963, 195))
        self.window.blit(price_coin, (968, 283))
        price_text = self.coin_font.render("300", 1, (0,0,128))
        self.window.blit(price_text, (998, 282))
        self.window.blit(tower_icon2, (963, 325))
        self.window.blit(price_coin, (968, 413))
        price2_text = self.coin_font.render("500", 1, (0,0,128))
        self.window.blit(price2_text, (998, 412))
        self.window.blit(tower_icon3, (963, 455))
        self.window.blit(price_coin, (968, 543))
        price3_text = self.coin_font.render("850", 1, (0,0,128))
        self.window.blit(price3_text, (998, 542))
        self.window.blit(wave_button, (975, 590))
        button_text = self.button_font.render("Next Wave", 1, (0,0,128))
        self.window.blit(button_text, (940, 645))

        if self.moving_tower and self.hearts >= 1:
            self.moving_tower.draw(self.window)
            self.draw_range()

    def game_over(self):
        surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(surface, (100, 100, 100, 120), (0, 0, self.width, self.height))
        self.window.blit(surface, (0, 0))
        game_over_text = self.game_over_font.render("Game Over", 1, (0,0,128))
        self.window.blit(game_over_text, (357, 185))

    def game_won(self):
        surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(surface, (100, 100, 100, 120), (0, 0, self.width, self.height))
        self.window.blit(surface, (0, 0))
        game_won_text = self.game_over_font.render("You Win!", 1, (0,0,128))
        self.window.blit(game_won_text, (388, 185))

    def draw_range(self):
        x, y = pygame.mouse.get_pos()
        surface = pygame.Surface((self.range*2, self.range*2), pygame.SRCALPHA)
        pygame.draw.circle(surface, (30, 144, 255, 70), (self.range, self.range), self.range)
        self.window.blit(surface, (x - self.range, y - self.range))

    def spawn_enemies(self):
        enemy_types = [YellowAlien(-3, 107), BlueAlien(-3, 107), GreenAlien(-3, 107), PinkAlien(-3, 107)]
        
        if sum(self.current_wave) == 0 and len(self.enemies) == 0:
            self.wave += 1
            if self.wave <= 10:
                self.current_wave = enemy_waves[self.wave]
            self.next_wave = False

        else:
            for x in range(4):
                if self.current_wave[x] > 0:
                    self.enemies.append(enemy_types[x])
                    self.current_wave[x] -= 1
                    break

    def reset_game(self):
        enemy_waves.clear()
        enemy_waves.append([0, 0, 0, 0])
        enemy_waves.append([5, 0, 0, 0])
        enemy_waves.append([10, 0, 0, 0])
        enemy_waves.append([5, 1, 0, 0])
        enemy_waves.append([10, 5, 0, 0])
        enemy_waves.append([5, 10, 1, 0])
        enemy_waves.append([10, 10, 5, 0])
        enemy_waves.append([5, 5, 15, 0])
        enemy_waves.append([0, 10, 10, 3])
        enemy_waves.append([0, 5, 10, 7])
        enemy_waves.append([0, 0, 0, 20])
        self.width = 1088
        self.height = 704
        self.window = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.towers = []
        self.hearts = 20
        self.coins = 600
        self.large_font = pygame.font.SysFont("TimesNewRoman", 36)
        self.coin_font = pygame.font.SysFont("TimesNewRoman", 24)
        self.button_font = pygame.font.SysFont("TimesNewRoman", 26)
        self.game_over_font = pygame.font.SysFont("TimesNewRoman", 80)
        self.moving_tower = None
        self.range = 150
        self.wave = 1
        self.current_wave = enemy_waves[self.wave]
        self.time = pygame.time.get_ticks()
        self.next_wave = False