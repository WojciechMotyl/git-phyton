my_list = [1,3,5,2,11,7]
l = 9
n = len(my_list)
wynik = [0, 0]
for i in range(0, n):
    a = 1
    for k in range(a, n):
        if my_list[i] + my_list[k] == l:
            if my_list[i] == wynik[1] and my_list[k] == wynik[0]:
                continue
            else:
                wynik = [my_list[i], my_list[k]]
                print('Suma liczby {} jest {}.'.format(wynik, l))
            
            
      
            
        