from pygame.locals import *
from pygame.constants import RLEACCEL
from time import sleep
import sys, pygame
from time import clock
from pygame.constants import K_q

import constantes
import bob
import tortuga
import patricio

pygame.init()



pantalla = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO))
WIDTH=800
HEIGHT=600
def Ganar(self):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tortus")
 
    background_image = load_image('recursos2d/win.png')

    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
 
        screen.blit(background_image, (0, 0))
        p_jug, p_jug_rect = texto('Has ganado para volver a jugar presiona enter', WIDTH/2, HEIGHT/1.1)
        keys = pygame.key.get_pressed()
        if keys[K_KP_ENTER]:
            pygame.init()
            main()
        screen.blit(p_jug, p_jug_rect)
        pygame.display.flip()
    pygame.init()
    main()
def load_image(filename, transparent=False):  
    try:
        image = pygame.image.load(filename)    
    except pygame.error as message:   
        print("Cannot load image: " + filename)
        raise SystemExit(message)    
    return image.convert_alpha()
def cargar_imagen(nombre,transparente=False):
    imagen=pygame.image.load(nombre)
    imagen=imagen.convert()
    if transparente:
        color=imagen.get_at((0,0))
        imagen.set_colorkey(color, RLEACCEL)
    return imagen
def gameover(self):
    WIDTH=800
    HEIGHT=600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

 
    background_image = load_image('recursos2d/over.jpg')


    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
 
        screen.blit(background_image, (0, 0))
        p_jug, p_jug_rect = texto('Para volver a jugar Porfavor presiona enter', WIDTH/2, HEIGHT/1.1)
        keys = pygame.key.get_pressed()
        if keys[K_KP_ENTER]:
            pygame.init()
            main()
        screen.blit(p_jug, p_jug_rect)
        pygame.display.flip()
    pygame.init()
    main()
    
def texto(texto, posx, posy, color=(255, 0, 0)):
    fuente = pygame.font.Font('recursos2d/DroidSans.ttf', 25)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect

def text_objects(text, font):
    textSurface = font.render(text, True, constantes.black)
    return textSurface, textSurface.get_rect()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        pantalla.fill(constantes.cyan)
        largeText = pygame.font.SysFont('comicsansms',115)
        TextSurf, TextRect = text_objects("Tortuguitas", largeText)
        pygame.display.set_caption("Super-Tortus")
        ico=pygame.image.load("recursos2d/tortu1.png")
        pygame.display.set_icon(ico) 
        TextRect.center = ((876/2),(550/2))
        pantalla.blit(TextSurf, TextRect)
        button("Iniciar!",150,450,100,50,constantes.green,constantes.bright_green,main)
        button("Quitar",550,450,100,50,constantes.red,constantes.bright_red,quitgame)
        pygame.display.update()
        
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(pantalla, ac,(x,y,w,h))
        
        if click[0] == 1 and action != None:
            action()  
    else:
        pygame.draw.rect(pantalla, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    pantalla.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()
    
def main():
    
    pygame.init() 
    pantalla=pygame.display.set_mode((constantes.ANCHO,constantes.ALTO))
    pygame.display.set_caption("Super-Tortus")
    ico=pygame.image.load("recursos2d/tortu1.png")
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
    nume2.append(tortuga2.gene())
    nume2.append(tortuga3.gene())
    salir=False
    clock = pygame.time.Clock()
    pygame.time.set_timer(USEREVENT+1, 1000)
    patricio1 = patricio.Patricio()

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
                        if number == 2:
                            nume2[number-1]-= 1
                        if number == 3:
                            nume2[number-1]-= 1
        global tortuga1a, tortuga2a, tortuga3a 
        tortuga1a=''
        tortuga2a=''
        tortuga3a=''                  
        for number in range(1,4):
            if nume2[number-1] == 1:
                if number == 1:
                    tortuga1.bajar(time)
                    tortuga1a='1'
                if number == 2:
                    tortuga2.bajar(time)
                    tortuga2a='1'
                if number == 3:
                    tortuga3.bajar(time)
                    tortuga3a='1'

            if nume2[number-1] == 0:
                if number == 1:
                    tortuga1.__init__()
                    nume2[0]=tortuga1.gene()
                    tortuga1a='0'
                    
                if number == 2:
                    tortuga2.__init__()
                    nume2[1]=tortuga2.gene()
                    tortuga2a='0'
                    
                if number == 3:
                    tortuga3.__init__()
                    nume2[2]=tortuga3.gene()
                    tortuga3a='0'
       
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
            MposX+=3
            cont+=1
            direc=True
        elif teclado[K_LEFT]:
            MposX-=3
            cont+=1
            direc=False            
        else :
            cont=6
             
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()   
         

 
        global salto_Par, bajada_Par
   
           
        if direc==True and salto==False :
            pantalla.blit(patricio1.ImagenPatricio, ( MposX, MposY),(xixf[i]))
       
        if direc==False and salto==False :
            pantalla.blit(patricio1.ImagenPatricio_inv, ( MposX, MposY),(Rxixf[i]))

        if salto==True:            
               
            if direc==True:
                pantalla.blit(patricio1.ImagenPatricio, ( MposX, MposY),(xixf[4]))
            if direc==False:
                pantalla.blit(patricio1.ImagenPatricio_inv, ( MposX, MposY),(Rxixf[4]))  
               
            if bajada==False:
                MposY-=4              
                   
            if bajada==True:
                MposY+=4              
               
            if MposY<=110:
                bajada=True
               
            if MposY>=185:
                bajada=False
                salto=False
            
        if 150 <= MposX <= 190:
            Ganar('')
        if 205 <= MposX <= 305:
            if MposY == 185:
                if tortuga1a == '1':
                    gameover('')  
                    
        if 305 <= MposX <= 330:
            if MposY == 185:
                gameover('')  

        if 330 <= MposX <= 430:
            if MposY == 185:
                if tortuga2a == '1':
                    gameover('')  
                    
        if 430 <= MposX <= 465:
            if MposY == 185:
                gameover('')  

        if 465 <= MposX <= 555:
            if MposY == 185:
                if tortuga3a == '1':
                    gameover('')         
                    
        pygame.display.flip()
     
    pygame.quit()  

if __name__ == "__main__":
    game_intro()
    main()
    quit()
    
