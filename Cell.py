import pygame, math
from pygame.locals import *
from pygame.sprite import Sprite

class Cell(Sprite):
    def __init__(self,screen,alive,pos,image):
        self.screen=screen
        self.base_image = pygame.image.load(image).convert_alpha()
        self.base_image2 = pygame.image.load("blank.png").convert_alpha()
        self.image = self.base_image
        self.image2= self.base_image2
        self.rect=self.image.get_rect()
        self.pos = pos
        self.rect.topleft= (self.pos[0],self.pos[1])
        self.alive=alive

    def blitme(self):
        if self.alive:
            self.screen.blit(self.image,self.pos)
        else:
            self.screen.blit(self.image2,self.pos)

    def getStatus(self):
        return self.alive

    def kill(self):
        self.alive=False

    def spawn(self):
        self.alive=True