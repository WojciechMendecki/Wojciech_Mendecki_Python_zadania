#Założenia:
#	- 0-6   - wiek przedszkolny - cena biletu: 0
#	- 7-17  - wiek szkolny      - cena biletu: 2.28
#	- 18-64 - wiek dorosły      - cena biletu: 3.80
#	- +65   - wiek emerytalny   - cena biletu: 1.90

wiek=int(input('Proszę podać swój wiek:'))
liczba_biletów=int(input('Proszę podać potrzebną liczbę biletów'))

if wiek<=6:
    cena = 0
elif 7<=wiek<=17:
    cena = 2.28
elif 18<=wiek<=64:
    cena = 3.80
else:
    cena=1.90


print(f'Cena biletu po uwzględnieniu zniżek za wiek wynosi: {cena: .2f} zł.\nNależność za bilety wynosi {cena * liczba_biletów :.2f} złotych')

