i = 0  # licznik - numer kolejnej podanej liczby

suma =0
srednia=0
maksimum=None
minimum=None


while True:

    liczba=input('Proszę podać liczbę. Żeby zakończyć proszę wpisać słowo \"koniec\".')

    if liczba.upper()=='KONIEC':
        break
    else:
        i += 1
        liczba = float(liczba)
        ostatnia_podana_liczba=liczba
        suma = suma + liczba
        srednia=suma/i


        if maksimum is None or liczba>maksimum:
            maksimum=liczba

        if minimum is None or liczba<minimum:
            minimum=liczba

if i ==0:
    print(f'Nie podano żadnej liczby.')
elif i==1:
    print(f'Podano tylko jedną liczbę: {ostatnia_podana_liczba:.2f}')
else:
    print(f'Podano liczb :{i}. \nSuma podanych liczb wynosi: {suma:.2f}. \nŚrednia liczb {srednia:.2f}. \
    \nNajwiększa licza to {maksimum:.2f} \nnajmniejsza z liczb to {minimum}')








