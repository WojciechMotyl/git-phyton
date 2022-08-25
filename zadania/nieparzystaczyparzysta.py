#Poproś użytkownika o numer. W zależności od tego, czy liczba jest parzysta, czy nieparzysta, wydrukuj odpowiednią wiadomość do użytkownika. 
#Poproś użytkownika o dwie liczby: jedną do sprawdzenia (zadzwoń num) i jedną do podzielenia przez ( check). 
# Jeśli checkdzieli się równo na num, poinformuj o tym użytkownika. Jeśli nie, wydrukuj inną odpowiednią wiadomość.
#Jeśli liczba jest wielokrotnością 4, wydrukuj inną wiadomość.

import os

clear =  lambda: os.system('cls')
clear()
number =  int(input("Podaj losową liczbę "))
if number % 4 == 0:
    print("Twoja liczba {} jest wielokrotnością libczy 4".format(number))
elif number % 2 == 0:
    print("Twoja liczba {} jest parzysta". format(number))    
else:
    print("Twoja liczba {} jest nieparzysta".format(number))
input()    
clear()
num = int(input("Podaj dzielna "))
check = int(input("Podaj dzielnik "))

if num % check == 0:
    print("Twoja dzielna {} dzieli sie całkowicie przez {}".format(num, check))
else:
    print("Twoja dzielna {} nie dzieli sie całkowicie przez {}".format(num, check))
    
    