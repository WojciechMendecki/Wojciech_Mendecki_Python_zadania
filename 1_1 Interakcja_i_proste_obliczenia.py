cena=float(input("Proszę podać cenę kilograma kartofli"))


print(f'Cena kg kartofli wynosi {cena}\nza 5kg kartofli zapłacisz {5*cena} złotych')

print('-',30)

cena_kartofle=float(input("Proszę podać cenę kilograma kartofli"))
ilosc_kartofle=float(input("Proszę podać potrzebną ilość kartofli"))

naleznosc_kartofle = cena_kartofle * ilosc_kartofle
print(f'Za {ilosc_kartofle} kg kartofli trzeba zapłacić {naleznosc_kartofle:.2f} zlotych')

print('-',30)

cena_kartofle=float(input("Proszę podać cenę kilograma kartofli"))
ilosc_kartofle=float(input("Proszę podać potrzebną ilość kartofli"))

cena_banany=float(input("Proszę podać cenę kilograma bananów"))
ilosc_banany=float(input("Proszę podać potrzebną ilość bananów"))

naleznosc_kartofle = cena_kartofle * ilosc_kartofle
naleznosc_banany = cena_banany * ilosc_banany

if naleznosc_kartofle>naleznosc_banany:
    wieksza_naleznosc='Wicecj zaplacisz za kartofle.'
elif naleznosc_kartofle<naleznosc_banany:
    wieksza_naleznosc = 'Wiecej zaplacisz za banany.'
else:
    wieksza_naleznosc='Za kartofle i banany zapłacisz taką samą kwotę.'

print(f'Za {ilosc_kartofle} kg kartofli i {ilosc_banany} \
kg bananów zapłacisz razem {naleznosc_kartofle + naleznosc_banany} zł.\n{wieksza_naleznosc}')

