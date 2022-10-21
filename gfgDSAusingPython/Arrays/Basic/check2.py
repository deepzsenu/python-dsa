check1 = ["learn", "Quiz", "Practice", "Contribute"]

check2 = check1
check3 = check1[:]
check2[0] = "Code"
check3[1] = 'Mcq'
count =0 
for c in (check1, check2, check3):
    if c[0] == "Code":
        count+=1
    if c[1] == "Mcq":
        count+=10

# print(count)

def gfg(x, l):
    for i in range(x):
        l.append(i*i)
    print(l)

# gfg(3, [3,2,1])
l = range(100, 110)
# print(l.index(105))


l1 = [1,2,3,4,5]
l2 =l1
l2[0] = 0

# print(l1)

l1 = [1998, 2002]
l2 = [2014, 2016]
print((l1+l2)*2)

