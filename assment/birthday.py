def birthday(s, num, step):
  if step == 0:
      if num == s:
          return "Yes"
      else:
          return "No"
  i = s
  while True:
    if num == i:
      return "YES"
    if step>0:
      if i>num:
        return "NO"
    if step<0:
      if i<num:
        return "No"
    i+=step
  
    

t = int(input())

while t>0:
  l = list(map(int, input().split()))
  s = l[0]
  num = l[1]
  step = l[2]
  print(birthday(s,num,step))
  t-=1