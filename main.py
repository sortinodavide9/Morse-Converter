import pygame as pg
import sys
from pygame import *
from converter import converter
pg.init()
#Finestra:
WINDOW_SIZE = (600,600)
screen = pg.display.set_mode(WINDOW_SIZE,0,0)
#Timer FPS
clock = pg.time.Clock()
#Testo:
base_font = pg.font.Font(None,32)
textList = [""]
listCounter = 0
accapoCounter = 0

while True:
    clock.tick(60)
    screen.fill((255,0,0)) 
    #POLL EVENTS
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        if event.type == KEYDOWN:
            listCounterTemp = listCounter
            accapoCounter += 1
            textList[listCounterTemp] += event.unicode #immissione del testo
            if event.key == K_ESCAPE:
                pg.quit()
                sys.exit()
            elif event.key == 8:#tasto per cnacellare
                    if(len(textList[listCounterTemp]) >= 1):
                        accapoCounter -= 2
                        #Cancellazione di un carattere:
                        temp = textList[listCounterTemp]
                        textList[listCounterTemp] = ""
                        for characters in range(len(temp)-1):
                            textList[listCounterTemp] += temp[characters] 
                    else:
                        #cancellare il carattere se si trova nella riga precedente
                        listCounterTemp -= 1
                        if(len(textList[listCounterTemp]) >= 1):
                            accapoCounter -= 2
                            #Cancellazione di un carattere:
                            temp = textList[listCounterTemp]
                            textList[listCounterTemp] = ""
                            for characters in range(len(temp)-1):
                                textList[listCounterTemp] += temp[characters]
        elif event.type == pg.MOUSEBUTTONDOWN:#cliccare tasto stamp
            pos = pg.mouse.get_pos()
            if(pos[0] >= 450 and pos[0] <= 600 and pos[1] >= 545 and pos[1] <= 595 ):
                converter(textList)
            if(pos[0] >= 20 and pos[0] <= 170 and pos[1] >= 545 and pos[1] <= 595 ):
                textList.clear()
                textList.append("")
    if(accapoCounter >= 53):#per andare a capo
        listCounter += 1
        textList.append("")
        accapoCounter = 0
    #Draw & Update:
    posy = 0   
    for text in textList:
        textSurface = base_font.render(text,True,(255,255,255))
        screen.blit(textSurface,(0,posy))
        posy += 15
    #Pulsante di stampa:
    pg.draw.rect(screen, (2,30,33),(450, 545,150,50))
    textButtonSurface = base_font.render("Stamp",True,(255,255,255))
    screen.blit(textButtonSurface,(450, 545))
    #Pulsante Clear
    pg.draw.rect(screen, (2,30,33),(20, 545,150,50))
    textButtonSurface = base_font.render("Clear",True,(255,255,255))
    screen.blit(textButtonSurface,(20, 545))
    pg.display.update()
    
        