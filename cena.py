
# Aby obliczyć cenę netto, trzeba od ceny brutto odliczyć stawkę VAT – w tym celu należy podzielić cenę brutto przez 1,23 lub 1,08,
#  w zależności od stawki 
# Tu będzie ten podatek trzeba samemu wpisać jaki jest tylko no w formie dziesiętnej typu np 5% to tu 0.05 

def cena_netto(cena_brutto,podatek):
    
    if podatek >=0 and cena_brutto >=0:
        return print(round(cena_brutto/(podatek),2))
    else:
        return print("Podatek i cena brutto nie mogą być ujemne!")

#testy =D
cena_netto(100,1.08)
cena_netto(100,1.23)
cena_netto(300,-8)
cena_netto(-300,1.08)