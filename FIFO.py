#ile mi zajęło rozkminianie co to jest fifo to aż wstyd się przyznać, trzy dni myślałem że to coś o piłce nożnej i nie rozumiem XD 
#i pytam znajomych a oni "First In First Out", no padłem XDD

class FIFO:

    def __init__(self):
        self.fifo = []
        #self.fifo = [1,2,3,10,15]
        #można też od razu w tym miejscu wrzucić tablicę i bez dodawania potem, ale nie byłem piewien jak to się ma prezentować

    def add(self,x):
        self.fifo.append(x)

    def pop(self):
        return self.fifo.pop(0)
    

f = FIFO()

f.add(10)
f.add(3)
f.add(11)
f.add(31)

print(f.pop())
# ^ ten jest 1 w kolejce, a potem lecą po kolei tam niżej v to zrobiłem dla sprawdzenia sobie, czy to działa tak jak myślę XD
#print(f.pop())
#print(f.pop())
#print(f.pop())
