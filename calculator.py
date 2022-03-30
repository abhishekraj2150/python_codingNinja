while True:
    n=int(input())
    if n==1:
        a = int(input())
        b = int(input())
        summ = a + b
        print(summ)
    elif n==2:
        c = int(input())
        d = int(input())
        diff = c - d
        print(diff)
    elif n == 3:
        e = int(input())
        f = int(input())
        product = e*f
        print(product)
    elif n == 4:
        g = int(input()) 
        h = int(input()) 
        divide = g//h
        print(divide)
    elif n == 5:
        a = int(input()) 
        b = int(input()) 
        mod = a%b
        print(mod)
    elif n == 6:
        break
    else:
        print("Invalid Operation")
    
        
