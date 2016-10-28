import pygame

class Bob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenBob=pygame.image.load("recursos2d/BOB.gif").convert_alpha()
    def colocar(self,pantalla,posicionX,posicionY):
        pantalla.blit(self.ImagenBob,(posicionX,posicionY))
    def redimensionar(self,ancho,alto):
        self.ImagenBob=pygame.transform.scale(self.ImagenBob, (ancho, alto))