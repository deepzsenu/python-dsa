def findUnique(arr1, arr2):
    a = set(arr1)
    b = set(arr2)
    return list(a.intersection(b))


a = [1,2,3,4]
b = [3,4,5,6,7]

print(findUnique(a,b))