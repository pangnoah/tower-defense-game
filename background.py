import pygame
import os

screen = pygame.display.set_mode((1024,704))
grass = pygame.image.load(os.path.join("assets", "towerDefense_tile024.png"))
path1 = pygame.image.load(os.path.join("assets", "towerDefense_tile001.png"))
path2 = pygame.transform.rotate(path1, 180)
path3 = pygame.image.load(os.path.join("assets", "towerDefense_tile025.png"))
path4 = pygame.image.load(os.path.join("assets", "towerDefense_tile023.png"))
curve1 = pygame.image.load(os.path.join("assets", "towerDefense_tile002.png"))
curve2 = pygame.image.load(os.path.join("assets", "towerDefense_tile004.png"))
curve3 = pygame.transform.rotate(curve2, 180)
curve4 = pygame.transform.rotate(curve1, 180)
curve5 = pygame.transform.rotate(curve1, 270)
curve6 = pygame.transform.rotate(curve2, 270)
object1 = pygame.image.load(os.path.join("assets", "towerDefense_tile130.png"))
object2 = pygame.image.load(os.path.join("assets", "towerDefense_tile131.png"))
object3 = pygame.image.load(os.path.join("assets", "towerDefense_tile132.png"))
object4 = pygame.image.load(os.path.join("assets", "towerDefense_tile134.png"))
object5 = pygame.image.load(os.path.join("assets", "towerDefense_tile135.png"))
object6 = pygame.image.load(os.path.join("assets", "towerDefense_tile136.png"))
object7 = pygame.image.load(os.path.join("assets", "towerDefense_tile137.png"))

def background():
    for x in range(0, 1088, 64):
        for y in range(0, 704, 64):
            screen.blit(grass, (x, y))
    for i in range(0, 512, 64):
        screen.blit(path1, (i, 128))
        screen.blit(path2, (i, 64))
    screen.blit(path2, (512, 64))
    screen.blit(curve1, (512, 128))
    screen.blit(curve2, (576, 64))
    screen.blit(path4, (576, 128))
    screen.blit(path3, (512, 192))
    screen.blit(curve3, (512, 256))
    screen.blit(curve4, (576, 192))
    screen.blit(path1, (576, 256))
    screen.blit(path1, (640, 256))
    screen.blit(curve1, (704, 256))
    screen.blit(path2, (640, 192))
    screen.blit(path2, (704, 192))
    screen.blit(curve2, (768, 192))
    screen.blit(path4, (768, 256))
    for i in range(320, 512, 64):
        screen.blit(path3, (704, i))
        screen.blit(path4, (768, i))
    screen.blit(curve5, (704, 512))
    screen.blit(curve6, (768, 576))
    screen.blit(path4, (768, 512))
    screen.blit(path1, (704, 576))
    for i in range(0, 704, 64):
        screen.blit(path1, (i, 576))
        screen.blit(path2, (i, 512))
    screen.blit(object2, (394, 335))
    screen.blit(object3, (338, 182))
    screen.blit(object3, (12, 394))
    screen.blit(object5, (193, 318))
    screen.blit(object7, (587, 461))
    screen.blit(object7, (348, 649))
    screen.blit(object6, (701, 83))
    screen.blit(object4, (96, 5))
    screen.blit(object2, (851, 433))