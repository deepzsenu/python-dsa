import math
def fun(d,cars,n):
    max_time = -math.inf
    
    for i in range(n):
        dist =  d - cars[i][0]
        time  = dist/cars[i][1]
        if time> max_time:
            max_time = time
    samy =  d/max_time
    return samy
        
d, n = map(int, input().split())
cars = []
for i in range(n):
    ki, si = map(int, input().split())
    cars.append([ki, si])
x = fun(d,cars,n)
print ('%.6f'%x)
    