import pygame

class Tortuga(pygame.sprite.Sprite):
    def __init__(self):
      
        pygame.sprite.Sprite.__init__(self)
        self.ImagenTortuga=pygame.image.load("recursos2d/tortuga1.png").convert_alpha()
    
    def colocar(self,pantalla,posicionX,posicionY):
        pantalla.blit(self.ImagenTortuga,(posicionX,posicionY))
    def redimensionar(self,ancho,alto):
        self.ImagenTortuga=pygame.transform.scale(self.ImagenTortuga, (ancho, alto))
    def bajar(self):
        pass
    def subir(self):
        pass