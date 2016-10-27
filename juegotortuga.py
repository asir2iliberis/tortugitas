'''
Created on 11 oct. 2016

@author: Administrator
'''
import pygame
from pygame.constants import RLEACCEL
#CONSTANTES

ANCHO=876
ALTO=550
#La clase tortuga hereda de la clase  Sprite
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
class Patricio(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenPatricio=pygame.image.load("recursos2d/patricio.png").convert_alpha()
    def colocar(self,pantalla,posicionX,posicionY):
        pantalla.blit(self.ImagenPatricio,(posicionX,posicionY))
    def redimensionar(self,ancho,alto):

        self.ImagenPatricio=pygame.transform.scale(self.ImagenPatricio, (ancho, alto))
class Bob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenBob=pygame.image.load("recursos2d/BOB.gif").convert_alpha()
    def colocar(self,pantalla,posicionX,posicionY):
        pantalla.blit(self.ImagenBob,(posicionX,posicionY))
    def redimensionar(self,ancho,alto):
        self.ImagenBob=pygame.transform.scale(self.ImagenBob, (ancho, alto))
def cargar_imagen(nombre,transparente=False):

    try:
        imagen=pygame.image.load(nombre)
    
    except(pygame.error):
        print("No se puede cargar la imagen") 
    imagen=imagen.convert()
    if transparente:
        color=imagen.get_at((0,0))
        imagen.set_colorkey(color, RLEACCEL)
    return imagen

def main():
    
    pygame.init() 
    
     
    pantalla=pygame.display.set_mode((ANCHO,ALTO))
    
     
    pygame.display.set_caption("Tortugas en accion")
     
    ico=pygame.image.load("recursos2d/tortuga1.png")
    pygame.display.set_icon(ico)
    
     
    fondo=cargar_imagen("recursos2d/fondo1.jpg")
    pantalla.blit(fondo,(0,0))
    tortuga1=Tortuga()
    tortuga2=Tortuga()
    tortuga3=Tortuga()
    tortuga4=Tortuga()
    patricio1=Patricio()
    bob1=Bob()
    tortuga1.redimensionar(95, 95)
    tortuga2.redimensionar(95, 95)
    tortuga3.redimensionar(95, 95)
    tortuga4.redimensionar(95, 95)
    patricio1.redimensionar(150, 150)
    bob1.redimensionar(90, 90)
    
    
     
    salir=False
    reloj=pygame.time.Clock()
 
    while salir!=True:
        for event in pygame.event.get(): 
            if event.type==pygame.QUIT or event.type==pygame.K_ESCAPE:
                salir=True
                   
        pygame.display.update()  
        reloj.tick(20)
        patricio1.colocar(pantalla, 570, 175)
        bob1.colocar(pantalla, 170 , 210)
        tortuga1.colocar(pantalla, 250, 300)
        tortuga2.colocar(pantalla, 340, 300)
        tortuga3.colocar(pantalla, 430, 300)
        tortuga4.colocar(pantalla, 520, 300)
     
    pygame.quit()  

if __name__ == "__main__":
    main()
