
sum = 0
j = int(input())

for i in range(1, j):  
    if j % i == 0:
        sum = sum + i
print(sum + j)
