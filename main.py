import pygame as pg
from pygame import *
pg.init()
#Finestra:
WINDOW_SIZE = (600,600)
screen = pg.display.set_mode(WINDOW_SIZE,0,0)
#Timer FPS
clock = pg.time.Clock()
#Testo:
base_font = pg.font.Font(None,32)
user_text = ""
while True:
    clock.tick(60)
    #POLL EVENTS
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        if event.type == KEYDOWN:
            user_text+=event.unicode
            if event.key == K_ESCAPE:
                pg.quit()
                sys.exit()
        
        #Draw & Update:     
        textSurface = base_font.render(user_text,True,(255,255,255))
        screen.blit(textSurface,(0,0))
        pg.display.update()
    
        