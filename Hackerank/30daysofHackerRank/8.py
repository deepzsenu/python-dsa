# # Enter your code here. Read input from STDIN. Print output to STDOUT

# t = int(input())
# dic = {}
# for i in range(t):
#     s = list(input().split())
#     name = s[0]
#     val = int(s[1])
#     dic[name] = val
    
# l = []
# for i in range(t):
#     l.append(input())
    
# for i in range(t):
#     if l[i] in dic:
#         print(l[i]+"="+str(dic[l[i]]))
#     else:
#         print("Not found")
    

n = int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {k: v for k,v in name_numbers}
while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break
