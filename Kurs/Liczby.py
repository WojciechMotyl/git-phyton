from tkinter import Y


x = 5
y = 3
z = "2"
v = "2.3"

#Dodawanie
wynik = x + y 
print("Wynik: {} typ: {}".format(wynik, type(wynik)))
#Odejmowanie
wynik = x - y
print("Wynik: {}".format(wynik))
#Mnozenie
wynik =  x * y
print("Wynik: {}".format(wynik))
#Dzielenie
wynik = x / y
print("Wynik: {} typ: {}".format(wynik, type(wynik)))
#Dzielenie calkowite
wynik =  x // y
print("Wynik: {}".format(wynik))
#Modulo
wynik = x % y
print("Wynik: {}".format(wynik))
#Potega
wynik =  x ** y
print("Wynik: {}".format(wynik))


wynik = x + int(z) 
print("Wynik: {} typ: {}".format(wynik, type(wynik)))
