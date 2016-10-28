import pygame
from pygame.constants import RLEACCEL

import patricio
import bob
import tortuga

ANCHO=876
ALTO=550

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
    tortuga1 = tortuga.Tortuga()
    tortuga2 = tortuga.Tortuga()
    tortuga3 = tortuga.Tortuga()
    tortuga4 = tortuga.Tortuga()
    patricio1= patricio.Patricio()
    bob1 = bob.Bob()
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
