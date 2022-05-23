
def OddevenMedian(N,A):
    eve = []
    odd = []
    for i in range(N):
        if A[i]%2==0:
            eve.append(A[i])
        else:
            odd.append(A[i])
            
    eve.sort()
    odd.sort()
    l1 = len(eve)
    l2 = len(odd)
    m1 = 0
    m2 = 0
   
    if l1%2 == 0:
        m1 = (eve[(l1//2)-1]+eve[l1//2])//2
        
    elif l2%2 ==0:
        m2 = (odd[((l2)//2)-1]+ odd[l2//2])//2
    if l1%2 == 1:
        m1 = eve[l1//2]
    if l2%2 ==1:
        m2 = odd[l2//2]        

    return m1+m2

a = [2,1,3,9,20,7,8]
print(OddevenMedian(a,7))
        
    