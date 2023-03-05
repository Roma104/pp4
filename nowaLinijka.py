def dopisz(plik):

    text = input("Dopisz : ")

    x = open(plik,"a")
    x.readline
    x.write(text + "\n")
    x.close

dopisz("test5.txt")