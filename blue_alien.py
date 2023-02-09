import pygame
import os
from enemy import Enemy

asset = pygame.image.load(os.path.join("assets", "shipBlue_manned.png"))
blue_alien = pygame.transform.scale(asset, (48, 48))

class BlueAlien(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.enemy_image = blue_alien
        self.max_health = 24
        self.current_health = self.max_health
        self.coins = 60