#Utwórz program, który prosi użytkownika o podanie swojego imienia i wieku. Wydrukuj wiadomość zaadresowaną do nich, która mówi im rok, w którym skończą 100 lat. 
imie = input("Podaj swoje imie")
wiek = int(input("Podaj swój wiek "))
rok = 2022
wynik = rok + 100 - wiek
print("Masz na imie {} i sto lat skończysz w {}".format(imie, wynik))

