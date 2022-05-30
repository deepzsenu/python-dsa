

import itertools


def Sub_Sequences1(STR):
    combs = []
    for l in range(len(STR)):
        combs.append(list(itertools.combinations(STR, l)))
    s = []
    for c in combs:
        for t in c:
            s.append(t)
        

    return (combs)


def matching(arr1, arr2):
    j = (Sub_Sequences1(arr1))
    k = (Sub_Sequences1(arr2))

    l = []
    for i in range(len(j)):
        for m in range(len(k)):
            if j[i] == k[m]:
                l.append(j[i])
    for i in range(len(l)):
        for j in range(len(l[0])):
            print(l[i][j], end = " ")
        print("")
n = int(input())
arr2 = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
matching(arr1, arr2)



