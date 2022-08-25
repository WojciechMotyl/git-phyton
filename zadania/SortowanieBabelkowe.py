#Problem: mamy podaną listę liczb. Np. A = [2,1,5,3,6]. Należy posortować ją rosnąco, za pomocą algorytmu bąbelkowego.

my_list = [7, 4, 2, 9, 11, 1]
n = len(my_list)
print(my_list)
while n > 1:    
    for l in range(0, n-1):
        if my_list[l] > my_list[l+1]:
            my_list[l], my_list[l+1] = my_list[l+1], my_list[l]
            
    n -= 1  
    
print(my_list)      
    
    