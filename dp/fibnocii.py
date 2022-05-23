def fib(f):
    n = [1]*f
    
    for i in range(f):
        if i ==1 or i == 0:
            n[i] = 1
        else:
            n[i] = n[i-1]+n[i-2]            
    return str(n[-1])


print(fib(5))            
        