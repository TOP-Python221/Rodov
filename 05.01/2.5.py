i = int(input())

num1 = i

for j in range(i):
    j = int(input())
    num1 = str(num1) + str(j) + ' ' 
    if j % i != 0: break
    
print(num1)

