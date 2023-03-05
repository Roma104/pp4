class Grupa:

    def __init__(self):
        self.studenci = []

    def zapisz_studenta(self,student):

        if len(self.studenci) < 10:

            self.studenci.append(student)
            return print(f"{student} został dodany do kursu.")

        else:

            return print(f"Przykro nam {student}. Kurs jest pełen. Proszę o wybranie innej grupy.")


s = Grupa()

s.zapisz_studenta("Discord")
s.zapisz_studenta("Jonatan - student aktorstwa, który jest moim współlokatorem")
s.zapisz_studenta("Lilith")
s.zapisz_studenta("Kicia")
s.zapisz_studenta("Pioter")
s.zapisz_studenta("Gabrysia")
s.zapisz_studenta("Ao Lie")
s.zapisz_studenta("Wukong")
s.zapisz_studenta("Macaque")
s.zapisz_studenta("Mei")
s.zapisz_studenta("Lucyfer")

#oczywiscie nie umiem wybrać normalnie losowych imion, no nie mogę no, to silniejsze ode mnie 