#Wypisz liczby od 1 do 100, przy czym liczby podzielne przez 3 zastąp słowem ‘Fizz’, liczby podzielne przez 5, zastąp słowem ‘Buzz’,
#natomiast liczby podzielne i przez 3 i przez 5 zastąp słowem ‘FizzBuzz’.
for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print('FizzBuzz') 
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)           
    