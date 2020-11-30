from random import randint
liczba_prób = 0
wylosowana_liczba=randint(0,999)

while True:

    podana_liczba = int(input('Proszę podać liczbę całkowitą z zakresu os 0 do 999'))
    liczba_prób+=1

    if podana_liczba==wylosowana_liczba:
        print(f'Grartulacje. Szukana liczba to {wylosowana_liczba}. Liczba prób: {liczba_prób}')
        break
    elif podana_liczba>wylosowana_liczba:
        print('Podana liczba jest zbyt duża. Podaj mniejszą liczbę.')
    else:
        print('Podana liczba jest zbyt mała. Podaj większą liczbę.')


