def fun(x,y):
    if x == 0:
        return y
    else:
        return fun(x-1, x+y)

# print(fun(4,3))

# def fn(n):
#     if n>4000:
#         return
#     print(n)
#     fn(n*2)
#     print(n)

# fn(1000)

# def fn(n):
#     if n == 4:
#         return n
#     else:
#         return 2*fn(n+1)
# print(fn(2))


# def fn(x,y):
#     if y ==0:
#         return 0
#     return (x+fn(x,y-1))


def fn(n):
    if n>0:
        return (n+fn(n-2))
    else:
        return 0


print(fn(10))