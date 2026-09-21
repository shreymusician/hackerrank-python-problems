def print_dig(num): 
    count = 0
    
    print("Digits : ", end = "")
    
    while(num != 0):
        dig = num % 10
        print(dig, end = " ")
        
        num = num // 10
        count += 1
    
    print("\nCount : ", count)

print_dig(5667)