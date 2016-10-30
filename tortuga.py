import pygame
import random

class Tortuga(pygame.sprite.Sprite):
    def __init__(self):
      
        pygame.sprite.Sprite.__init__(self)
        self.ImagenTortuga=pygame.image.load("recursos2d/tortuga1.png").convert_alpha()
        self.rect = self.ImagenTortuga.get_rect()
        self.rect.centery = 180
        self.speed = [0.5, -0.5]
    
    def colocar(self,pantalla,posicionX,posicionY):
        pantalla.blit(self.ImagenTortuga,(posicionX,posicionY))
    def redimensionar(self,ancho,alto):
        self.ImagenTortuga=pygame.transform.scale(self.ImagenTortuga, (ancho, alto))
        
    def bajar(self, time):

        if self.rect.centery <= 430:
            self.rect.centery -= self.speed[1] * time
            
    def subir(self):
        pass
    
    def gene(self):
        numero = random.randint(4,15)
        return numero