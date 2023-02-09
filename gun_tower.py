import pygame
import os
import math

class GunTower():
    def __init__(self, x, y):
        self.x = x - 32
        self.y = y + 32
        self.tower_images = []
        self.tower_images1 = []
        self.tower_images2 = []
        self.tower_images3 = []
        self.range = 150
        self.in_range = False
        self.counter = 0
        self.damage = 1

        tower = pygame.image.load(os.path.join("assets", "towerDefense_tile249.png"))
        tower1 = pygame.image.load(os.path.join("assets", "shootingtower1.png"))
        tower2 = pygame.image.load(os.path.join("assets", "shootingtower2.png"))
        tower3 = pygame.image.load(os.path.join("assets", "shootingtower3.png"))
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

    def move(self, x, y):
        self.x = x
        self.y = y

    def draw(self, window):
        if self.y >= 165 and self.y < 450 and self.x < 560:
            if self.in_range:
                self.counter += 1
                if self.counter >= len(self.tower_images*20):
                    self.counter = 0
            else:
                self.counter = 0
            tower = self.tower_images[self.counter//20]
            window.blit(tower, (self.x - tower.get_width() + 64, (self.y - tower.get_height())))

        if self.y >= 610 and self.x < 740:
            if self.in_range:
                self.counter += 1
                if self.counter >= len(self.tower_images*20):
                    self.counter = 0
            else:
                self.counter = 0
            tower = self.tower_images[self.counter//20]
            window.blit(tower, (self.x - tower.get_width() + 64, (self.y - tower.get_height())))

        if self.y < 285 and self.x >= 560:
            if self.in_range:
                self.counter += 1
                if self.counter >= len(self.tower_images1*20):
                    self.counter = 0
            else:
                self.counter = 0
            tower = self.tower_images1[self.counter//20]
            window.blit(tower, (self.x - tower.get_width() + 64, (self.y - tower.get_height())))
            
        if self.y >= 285 and self.x >= 740:
            if self.in_range:
                self.counter += 1
                if self.counter >= len(self.tower_images1*20):
                    self.counter = 0
            else:
                self.counter = 0
            tower = self.tower_images1[self.counter//20]
            window.blit(tower, (self.x - tower.get_width() + 64, (self.y - tower.get_height())))

        if self.y < 165 and self.x < 560:
            if self.in_range:
                self.counter += 1
                if self.counter >= len(self.tower_images2*20):
                    self.counter = 0
            else:
                self.counter = 0
            tower = self.tower_images2[self.counter//20]
            window.blit(tower, (self.x - tower.get_width() + 64, (self.y - 64)))

        if self.y < 610 and self.y >= 450 and self.x < 560:
            if self.in_range:
                self.counter += 1
                if self.counter >= len(self.tower_images2*20):
                    self.counter = 0
            else:
                self.counter = 0
            tower = self.tower_images2[self.counter//20]
            window.blit(tower, (self.x - tower.get_width() + 64, (self.y - 64)))

        if self.y >= 285 and self.y < 610 and self.x >= 560 and self.x < 740:
            if self.in_range:
                self.counter += 1
                if self.counter >= len(self.tower_images3*20):
                    self.counter = 0
            else:
                self.counter = 0
            tower = self.tower_images3[self.counter//20]
            window.blit(tower, (self.x, (self.y - tower.get_height())))

    def collide_tower(self, tower):
        dx = self.x - tower.x
        dy = self.y - tower.y
        distance = math.hypot(dx, dy)
        if distance >= 42:
            return False
        else:
            return True

    def attack(self, enemies):
        coins = 0
        self.in_range = False
        closest_enemy = []
        for enemy in enemies:
            dx = self.x - enemy.x + 32
            dy = self.y - enemy.y - 64
            distance = math.hypot(dx, dy)
            if distance < self.range:
                self.in_range = True
                closest_enemy.append(enemy)

        if len(closest_enemy) > 0:
            enemy = closest_enemy[0]
            if self.counter == 20:
                if enemy.destroyed(self.damage) == True:
                    enemies.remove(enemy)
                    coins = enemy.coins

        return coins