class Grupa:

    def __init__(self):

        self.studenci= []

    def zapiszStudenta(self,student):

        if len(self.studenci) < 10:

            self.studenci.append(student)
            print(f"{student} został dodany do kursu.")

        else:

            print(f"Przykro nam {student}. Kurs jest pełen. Proszę o wybranie innej grupy.")


s = Grupa()

s.zapiszStudenta("Discord")
s.zapiszStudenta("Jonatan - student aktorstwa, który jest moim współlokatorem")
s.zapiszStudenta("Lilith")
s.zapiszStudenta("Kicia")
s.zapiszStudenta("Pioter")
s.zapiszStudenta("Gabrysia")
s.zapiszStudenta("Ao Lie")
s.zapiszStudenta("Wukong")
s.zapiszStudenta("Macaque")
s.zapiszStudenta("Mei")
s.zapiszStudenta("Lucyfer")

#oczywiscie nie umiem wybrać normalnie losowych imion, no nie mogę no, to silniejsze ode mnie 