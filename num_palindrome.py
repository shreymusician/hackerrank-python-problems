def is_palindrome(num):
    num_copy = num
    rev = 0
    
    while(num > 0):
        dig = num % 10
        rev = rev*10 + dig
        num = num // 10
    
    return rev
    
print(is_palindrome(136589))
        