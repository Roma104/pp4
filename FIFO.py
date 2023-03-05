#ile mi zajęło rozkminianie co to jest fifo to aż wstyd się przyznać, trzy dni myślałem że to coś o piłce nożnej i nie rozumiem XD 
#i pytam znajomych a oni "First In First Out", no padłem XDD

class FIFO:

    def __init__(self):
        self.fifo = []

    def add(self,a):
        self.fifo.append(a)

    def pop(self):
        return self.fifo.pop(0)
    

f = FIFO()

f.add(10)
f.add(3)
f.add(1)
f.add(9)
f.add(4)

print(f.pop())

