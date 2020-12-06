text = ""
file = open("Morse.txt", "w")
def converter(textList):
    global text
    print("Funzione")
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
    file.close()
    
