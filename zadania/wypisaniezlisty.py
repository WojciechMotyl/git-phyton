"""""
 Weź listę, powiedz na przykład tę:
 a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
i napisz program, który wypisze wszystkie elementy listy, które są mniejsze niż 5.

Dodatki:

Zamiast drukować elementy jeden po drugim, 
stwórz nową listę zawierającą wszystkie elementy mniejsze niż 5 z tej listy i wydrukuj tę nową listę
Napisz to w jednym wierszu Pythona.
Poproś użytkownika o numer i zwróć listę zawierającą tylko elementy z oryginalnej listy a, 
które są mniejsze niż liczba podana przez użytkownika.
"""
import os

def clear():
    os.system('cls')
    
my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
print('Liczby z listy {} mniejsze od 5 to:'.format(my_list))
for n in my_list:
    if n < 5:
        print(n)
    else:
        continue
input()
clear()    
print('Liczby z listy {} mniejsze od 5 zapisane w nowej liście'.format(my_list))
for i in my_list:
    if i < 5:
        new_list.insert(i, i)
        
    else:
        continue
print(new_list)
input()
clear()
a =  int(input('Podaj liczbe'))
print('Liczby z listy {} mniejsze od twojej liczby {} to:'.format(my_list, a))   
for k in my_list:
    if k < a:
        print(k)
    else:
        continue
     
      
      
      
        
        
    