from gun_tower import GunTower
import pygame
import os

class MachineGunTower(GunTower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_images = []
        self.tower_images1 = []
        self.tower_images2 = []
        self.tower_images3 = []
        self.damage = 2

        tower = pygame.image.load(os.path.join("assets", "towerDefense_tile203.png"))
        tower1 = pygame.image.load(os.path.join("assets", "doubletower1.png"))
        tower2 = pygame.image.load(os.path.join("assets", "doubletower2.png"))
        tower3 = pygame.image.load(os.path.join("assets", "doubletower3.png"))
        self.tower_images.append(tower)
        self.tower_images.append(tower1)
        self.tower_images.append(tower2)
        self.tower_images.append(tower3)
        tower_rotated90 = pygame.transform.rotate(tower, 90)
        tower1_rotated90 = pygame.transform.rotate(tower1, 90)
        tower2_rotated90 = pygame.transform.rotate(tower2, 90)
        tower3_rotated90 = pygame.transform.rotate(tower3, 90)
        self.tower_images1.append(tower_rotated90)
        self.tower_images1.append(tower1_rotated90)
        self.tower_images1.append(tower2_rotated90)
        self.tower_images1.append(tower3_rotated90)
        tower_rotated180 = pygame.transform.rotate(tower, 180)
        tower1_rotated180 = pygame.transform.rotate(tower1, 180)
        tower2_rotated180 = pygame.transform.rotate(tower2, 180)
        tower3_rotated180 = pygame.transform.rotate(tower3, 180)
        self.tower_images2.append(tower_rotated180)
        self.tower_images2.append(tower1_rotated180)
        self.tower_images2.append(tower2_rotated180)
        self.tower_images2.append(tower3_rotated180)
        tower_rotated270 = pygame.transform.rotate(tower, 270)
        tower1_rotated270 = pygame.transform.rotate(tower1, 270)
        tower2_rotated270 = pygame.transform.rotate(tower2, 270)
        tower3_rotated270 = pygame.transform.rotate(tower3, 270)
        self.tower_images3.append(tower_rotated270)
        self.tower_images3.append(tower1_rotated270)
        self.tower_images3.append(tower2_rotated270)
        self.tower_images3.append(tower3_rotated270)