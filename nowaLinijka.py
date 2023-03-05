def dopisz(plik):

    text = input("Dopisz: ")

    x = open(plik,"a")
    x.write(text + "\n")
    x.close


dopisz("test5.txt")