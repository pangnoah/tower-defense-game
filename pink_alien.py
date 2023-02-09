import pygame
import os
from enemy import Enemy

asset = pygame.image.load(os.path.join("assets", "shipPink_manned.png"))
pink_alien = pygame.transform.scale(asset, (48, 48))

class PinkAlien(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.enemy_image = pink_alien
        self.max_health = 125
        self.current_health = self.max_health
        self.coins = 100