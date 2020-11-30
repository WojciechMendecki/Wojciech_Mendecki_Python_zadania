a=float((input("proszę podać długość pierwszego boku trójkąta")))
b=float((input("proszę podać długość drugiego boku trójkąta")))
c=float((input("proszę podać długość treciego boku trójkąta")))

import math

if max(a,b,c)>= (a+b+c)/2:          #sprawdza czy najdłuższy bok jest dłuższy (lub równy) niż połowa obwodu
    print('Nie można zbudować trójkąta o takich długościach boków')
    exit()


polowa_obwodu = (a+b+c)/2

pole =math.sqrt (polowa_obwodu * (polowa_obwodu-a) * (polowa_obwodu - b) * (polowa_obwodu - c))

print(f'Pole trójkąta wynosi {pole:.2f}')