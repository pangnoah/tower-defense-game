import pygame

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.enemy_image = None
        self.max_health = 1
        self.current_health = 1

    def draw(self, window):
        speed = 0.35
        if self.x < 555 and self.y < 235:
            self.x += speed
        elif self.y < 235:
            self.y += speed
        elif self.x < 745 and self.y < 555:
            self.x += speed
        elif self.y < 555:
            self.y += speed
        else:
            self.x -= speed
        window.blit(self.enemy_image, (self.x, self.y))
        self.draw_health_bar(window)

    def draw_health_bar(self, window):
        length = 50
        change_health = length / self.max_health
        health_bar = change_health * self.current_health
        pygame.draw.rect(window, (255,0,0), (self.x - 3, self.y - 20, length, 10), 0)
        pygame.draw.rect(window, (0, 255, 0), (self.x - 3, self.y - 20, health_bar, 10), 0)

    def destroyed(self, damage):
        self.current_health -= damage
        if self.current_health <= 0:
            return True
        return False