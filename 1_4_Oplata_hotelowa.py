wiek=int(input("Proszę podać swój wiek"))
liczba_nocy=int((input("Proszę podać liczbę nocy")))

if wiek<18:
    cena_za_noc=100
else:
    if liczba_nocy==1:
        cena_za_noc=200
    elif 2<=liczba_nocy<5:
        cena_za_noc=180
    else:
        cena_za_noc=150

if wiek>=65:
    cena_za_noc=0.9 * cena_za_noc

print(f'Cena za noc po uwzględnieniu zniżek wynosi {cena_za_noc} złotych. \nNależność za pobyt wynosi {liczba_nocy*cena_za_noc: .2f} złotych')

