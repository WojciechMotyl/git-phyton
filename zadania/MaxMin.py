#Przy użyciu języka Python, należy znaleźć najmniejszą oraz największa liczbę na liście.
#Czyli, dla przykładu, jeżeli nasza lista to:
lista = [1,3,7,11,2,-6,0]
max = None
min = None
for i in lista:
    if max == None or max > i:
        max = i
    if min == None or min < i:
        min = i
print('To jest namniejsza liczba {}'.format(min))
print('To jest najwieksza liczba {}'.format(max))            