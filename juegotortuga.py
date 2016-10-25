'''
Created on 11 oct. 2016

@author: Administrator
'''
import pygame
from pygame.constants import RLEACCEL
#CONSTANTES

ANCHO=0#1400
ALTO=0#787
#La clase tortuga hereda de la clase  Sprite
class Tortuga(pygame.sprite.Sprite):
    def __init__(self):
      
        pygame.sprite.Sprite.__init__(self)
        self.ImagenTortuga=pygame.image.load("../recursos2d/tortuga.png").convert_alpha()
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
        self.ImagenPatricio=pygame.image.load("../recursos2d/patricio.png").convert_alpha()
    def colocar(self,pantalla,posicionX,posicionY):
        pantalla.blit(self.ImagenPatricio,(posicionX,posicionY))
    def redimensionar(self,ancho,alto):
        #Escalar las tortugas
        self.ImagenPatricio=pygame.transform.scale(self.ImagenPatricio, (ancho, alto))
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
    
     
    pantalla=pygame.display.set_mode((ANCHO,ALTO), pygame.FULLSCREEN)
    
     
    pygame.display.set_caption("Tortugas en accion")
     
    ico=pygame.image.load("../recursos2d/tortuga.png")
    pygame.display.set_icon(ico)
    
     
    fondo=cargar_imagen("../recursos2d/b.jpg")
    pantalla.blit(fondo,(0,0))
    tortuga1=Tortuga()
    tortuga2=Tortuga()
    tortuga3=Tortuga()
    patricio1=Patricio()
    tortuga1.redimensionar(150, 150)
    tortuga2.redimensionar(150, 150)
    tortuga3.redimensionar(150, 150)
    patricio1.redimensionar(250, 250)
    
    
     
    salir=False
    reloj=pygame.time.Clock()
 
    while salir!=True:
        for event in pygame.event.get(): 
            if event.type==pygame.QUIT or event.type==pygame.K_ESCAPE:
                salir=True
                   
        pygame.display.update()  
        reloj.tick(20)
        patricio1.colocar(pantalla, 1050, 225)
        tortuga1.colocar(pantalla, 700, 475)
        tortuga2.colocar(pantalla, 850, 475)
        tortuga3.colocar(pantalla, 1000, 475)
     
    pygame.quit()  

if __name__ == "__main__":
    main()
