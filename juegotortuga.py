from pygame.locals import *
from pygame.constants import RLEACCEL
from time import sleep
import sys, pygame
from time import clock
from pygame.constants import K_q

import patricio
import bob
import tortuga

ANCHO=876
ALTO=550

def imagen(filename, transparent=False):  
    image = pygame.image.load(filename)       
    return image.convert_alpha()

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
    
    global salto,MposX,MposY,bajada, direc, cont,bajada
    MposX =700
    MposY =185
    xixf={}
    Rxixf={}
    direc= None
    salto=None
    cont=6
    direc=True
    i=0
    bajada=False
    salto = False
    xixf[0]=(0,0,60,123)
    xixf[1]=(66,0,75,123)
    xixf[2]=(141,0,75,123)
    xixf[3]=(219,0,60,123)
    xixf[4]=(279,0,81,123)
    xixf[5]=(360,0,81,123)

    Rxixf[0]=(366,0,66,123)
    Rxixf[1]=(288,0,75,123)
    Rxixf[2]=(222,0,66,123)
    Rxixf[3]=(150,0,69,123)
    Rxixf[4]=(72,0,78,123)
    Rxixf[5]=(0,0,75,123)
    

    
    tortuga1 = tortuga.Tortuga()
    tortuga2 = tortuga.Tortuga()
    tortuga3 = tortuga.Tortuga()

    bob1 = bob.Bob()

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
    patricio1 = imagen("recursos2d/patricio.png",True)   
    patricio_inv=pygame.transform.flip(patricio1,True,False);
 
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

        bob1.colocar(pantalla, 170 , 210)
        tortuga1.redimensionar(95, 95)
        tortuga2.redimensionar(95, 95)
        tortuga3.redimensionar(95, 95)
        tortuga1.colocar(pantalla, 260, tortuga1.rect.centery)
        tortuga2.colocar(pantalla, 385, tortuga2.rect.centery)
        tortuga3.colocar(pantalla, 510, tortuga3.rect.centery)           
            
        teclado = pygame.key.get_pressed()
       
        if teclado[K_UP]:
            salto=True
           
        if teclado[K_RIGHT]:
            MposX+=2
            cont+=1
            direc=True
        elif teclado[K_LEFT]:
            MposX-=2
            cont+=1
            direc=False            
        else :
            cont=6
             
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()   
         
        p=6

        if cont==p:
            i=0
       
        if cont==p*2:
            i=1
       
        if cont==p*3:
            i=2
       
        if cont==p*4:
            i=3
       
        if cont==p*5:
            i=4
       
        if cont==p*6:
            i=5
            cont=0 
 
        global salto_Par, bajada_Par
   
           
        if direc==True and salto==False :
            pantalla.blit(patricio1, ( MposX, MposY),(xixf[i]))
       
        if direc==False and salto==False :
            pantalla.blit(patricio_inv, ( MposX, MposY),(Rxixf[i]))

        if salto==True:            
               
            if direc==True:
                pantalla.blit(patricio1, ( MposX, MposY),(xixf[4]))
            if direc==False:
                pantalla.blit(patricio_inv, ( MposX, MposY),(Rxixf[4]))  
               
            if bajada==False:
                MposY-=4              
                   
            if bajada==True:
                MposY+=4              
               
            if MposY<=110:
                bajada=True
               
            if MposY>=185:
                bajada=False
                salto=False

        pygame.display.flip()
     
    pygame.quit()  

if __name__ == "__main__":
    main()
