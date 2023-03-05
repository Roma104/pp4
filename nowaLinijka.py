def dopisz(plik):

    text = input("Dopisz : ")

    x = open(plik,"a")
    x.readline
    x.write("\n" + text)
    x.close

dopisz("test3.txt")