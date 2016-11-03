import pygame

class Patricio(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenPatricio = pygame.image.load("recursos2d/patricio.png").convert_alpha()
        self.ImagenPatricio_inv = pygame.transform.flip(self.ImagenPatricio,True,False);
        self.ImagenPatricio_rect = self.ImagenPatricio.get_rect()
        self.ImagenPatricio_inv_rect = self.ImagenPatricio_inv.get_rect()