import pygame
import os
from enemy import Enemy

asset = pygame.image.load(os.path.join("assets", "shipYellow_manned.png"))
yellow_alien = pygame.transform.scale(asset, (48, 48))

class YellowAlien(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.enemy_image = yellow_alien
        self.max_health = 6
        self.current_health = self.max_health
        self.coins = 40