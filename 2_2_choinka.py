liczba_lini=int(input("Proszę podać liczbę lini")) # i - (licznik) liczba linii


i=1                     # liczba lini

while i<= liczba_lini:
    print(' ' * (liczba_lini-(i-1)),'*' * ((2 * (i - 1) +1)),' ' * (liczba_lini-(i-1)))
    i+= 1

