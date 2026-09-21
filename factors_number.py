n = int(input('Enter a number : '))
print('Factors : 1 ', end='')

for i in range(2, n*n):
    if(n % i == 0):
        print(i, end=' ')