import pygame
from pygame.locals import *
from pygame.constants import RLEACCEL
from time import sleep


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
    
    
    tortuga1 = tortuga.Tortuga()
    tortuga2 = tortuga.Tortuga()
    tortuga3 = tortuga.Tortuga()
    patricio1= patricio.Patricio()
    bob1 = bob.Bob()
    patricio1.redimensionar(150, 150)
    bob1.redimensionar(90, 90)
    
    
     
    nume2 = []
    nume2.append(tortuga1.gene())
    #print ("numero generado tor1 "+ str(nume2[0]))
    nume2.append(tortuga2.gene())
    #print ("numero generado tor2 "+ str(nume2[1]))
    nume2.append(tortuga3.gene())
    #print ("numero generado tor3 "+ str(nume2[2])) 
     
    
    salir=False
    clock = pygame.time.Clock()
    pygame.time.set_timer(USEREVENT+1, 1000)
 
    while salir!=True:
        time = clock.tick(60)
        for event in pygame.event.get(): 
            if event.type==pygame.QUIT or event.type==pygame.K_ESCAPE:
                salir=True
            if event.type == USEREVENT+1:
                
                for number in range(1,4):
                    if nume2[number-1] > 0:
                        if number == 1:
                            nume2[number-1]-= 1
                            #print("tor1:"+str(nume2[number-1]))
                        if number == 2:
                            nume2[number-1]-= 1
                            #print("tor2:"+str(nume2[number-1]))
                        if number == 3:
                            nume2[number-1]-= 1
                            #print("tor3:"+str(nume2[number-1]))
                            
        for number in range(1,4):
            if nume2[number-1] == 1:
                if number == 1:
                    tortuga1.bajar(time)
                if number == 2:
                    tortuga2.bajar(time)
                if number == 3:
                    tortuga3.bajar(time)

            if nume2[number-1] == 0:
                if number == 1:
                    tortuga1.__init__()
                    nume2[0]=tortuga1.gene()
                    #print("tor1 generado:"+str(nume2[0]))
                    
                if number == 2:
                    tortuga2.__init__()
                    nume2[1]=tortuga2.gene()
                    #print("tor2 generado:"+str(nume2[1]))
                    
                if number == 3:
                    tortuga3.__init__()
                    nume2[2]=tortuga3.gene()
                    #print("tor2 generado:"+str(nume2[2]))
        
        pantalla.blit(fondo,(0,0))
        patricio1.colocar(pantalla, 570, 175)
        bob1.colocar(pantalla, 170 , 210)
        tortuga1.redimensionar(95, 95)
        tortuga2.redimensionar(95, 95)
        tortuga3.redimensionar(95, 95)
        tortuga1.colocar(pantalla, 260, tortuga1.rect.centery)
        tortuga2.colocar(pantalla, 385, tortuga2.rect.centery)
        tortuga3.colocar(pantalla, 510, tortuga3.rect.centery)
        pygame.display.update()
     
    pygame.quit()  

if __name__ == "__main__":
    main()
