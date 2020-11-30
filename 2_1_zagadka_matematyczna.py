from random import randint

liczba_1 = randint(0,99)
liczba_2 = randint(0,99)

print(f'Pierwsza liczba to: {liczba_1}\nDruga liczba to: {liczba_2}')

wynik = int(input("Proszę podać sumę tych liczb"))

while True:
    if wynik == liczba_1 + liczba_2 :
        print(f'Gratulacje! Podałeś właściwy wynik. Suma liczb wynosi {liczba_1 + liczba_2}')
        exit()
    else:
        print(f'Błędny wynik. Proszę spróbowąć raz jeszcze')
        wynik=int(input('Proszę podać sumę liczb'))
