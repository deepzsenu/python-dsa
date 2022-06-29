def fun(n, j):
    vol = []
    mass = []
    for i in range(n):
        s = list(j[i].split(" "))
        vol.append(int(s[0])) 
        mass.append(int(s[-2]))        
    d= sum(mass)/sum(vol)    
    return d

n = int(input())
j= list(input().split("-"))
x = fun(n,j)
print(x)