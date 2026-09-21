n = int(input('Enter a number : '))
rev = 0
nc = n

while(n>0):
    dig = n % 10
    rev = rev*10 + dig
    n = n // 10
    
print('Reversed Number : ', rev)