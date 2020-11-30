dzien_oddania=int(input("Podaj liczbę od 1 do 6 \noznaczającą dzień tygodnia,\
    \nw którym buty zostały oddane do naprawy"))

if not 1<=dzien_oddania<=6:
    print('Błędnie podany dzień tygodnia. Weź się trochę ogarnij:-)')
    exit()

czas_naprawy=int(input("Podaj przewidywany czas naprawy"))

dzien_odbioru = (dzien_oddania + czas_naprawy)%7

komunikat=''

if dzien_odbioru==0:
    dzien_odbioru=1
    komunikat="Zakład jest nieczynny w niedzielę. Proszę przyjść po odbiór w poniedziałek"

nazwy_dni=('poniedziałek', 'wtorek','środa', 'czwartek', 'piątek', 'sobota')

print(f'Buty będa do odbioru w {nazwy_dni[dzien_odbioru-1]}.\n{komunikat}')





