# Utwórz program, który pyta użytkownika o liczbę, a następnie wyświetla listę wszystkich dzielników tej liczby.

def divisor(a = 0):
    if not a == 0:
        for ele in range(1, a+1):
            if a % ele == 0:
                print(ele)
                
number = int(input('Podaj liczbe'))
divisor(number)                  
      
                
            