import pygame as pg
from pygame import *
import sys
text = ""

def converter(textList):
    global text
    file = open("Morse.txt", "w")
    for textElement in textList:
        text += textElement
    for c in text:
        if(c == "a"):
            file.write(".- ")
        elif(c == "b"):
            file.write("-... ")
        elif(c == "c"):
            file.write("-.-. ")
        elif(c == "d"):
            file.write("-.. ")
        elif(c == "e"):
            file.write(". ")
        elif(c == "f"):
            file.write("..-. ")
        elif(c == "g"):
            file.write("--. ")
        elif(c == "h"):
            file.write(".... ")
        elif(c == "i"):
            file.write(".. ")
        elif(c == "j"):
            file.write(".--- ")
        elif(c == "k"):
            file.write("-.- ")
        elif(c == "l"):
            file.write(".-.. ")
        elif(c == "m"):
            file.write("-- ")
        elif(c == "n"):
            file.write("-. ")
        elif(c == "o"):
            file.write("--- ")
        elif(c == "p"):
            file.write(".--. ")
        elif(c == "q"):
            file.write("--.- ")
        elif(c == "r"):
            file.write(".-. ")
        elif(c == "s"):
            file.write("... ")
        elif(c == "t"):
            file.write("- ")
        elif(c == "u"):
            file.write("..- ")
        elif(c == "v"):
            file.write("...- ")
        elif(c == "w"):
            file.write(".-- ")
        elif(c == "x"):
            file.write("-..- ")
        elif(c == "y"):
            file.write("-.-- ")
        elif(c == "z"):
            file.write("--.. ")
        else:
            file.write(" / ")
    file = open("Morse.txt", "r")
    punto = pg.mixer.Sound('..wav')# .
    trattino = pg.mixer.Sound('-.wav')# -
    for character in file.read():
        pg.time.delay(500)
        for event in pg.event.get():
            if event.type == KEYDOWN:
                pg.quit()
                sys.exit()
        if(character == "."):
            punto.play()
        elif(character == "-"):
            trattino.play()
        elif(character == " " or character == "/"):
            pg.time.delay(200)
    file.close()
    pg.quit()
    sys.exit()
