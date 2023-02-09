import pygame
import os
from enemy import Enemy

asset = pygame.image.load(os.path.join("assets", "shipGreen_manned.png"))
green_alien = pygame.transform.scale(asset, (48, 48))

class GreenAlien(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.enemy_image = green_alien
        self.max_health = 70
        self.current_health = self.max_health
        self.coins = 80