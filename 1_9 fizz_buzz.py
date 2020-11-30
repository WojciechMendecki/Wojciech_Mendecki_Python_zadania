i=1
text1=''
text2=''

while i<100:
    i+=1
    if i % 3 == 0:
        text1='Fizz' #text 1 - podzielne przez 3 - przypisuje Fizz
    if i % 5 == 0:
        text2 ='Buzz' #text 1 - podzielne przez 5 - przypisuje Buzz

    print(f'{i} {text1}{text2}')
    text1 = ''
    text2 = ''

