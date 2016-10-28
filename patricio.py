import pygame

class Patricio(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenPatricio=pygame.image.load("recursos2d/patricio.png").convert_alpha()
    def colocar(self,pantalla,posicionX,posicionY):
        pantalla.blit(self.ImagenPatricio,(posicionX,posicionY))
    def redimensionar(self,ancho,alto):

        self.ImagenPatricio=pygame.transform.scale(self.ImagenPatricio, (ancho, alto))