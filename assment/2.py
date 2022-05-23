def maxiPow(N,K,A):
    
    if N == 0:
        return 0
    
    maxi = A[0]
    oddheight = 0
    count = 1
    for i in range(1,N):
        if A[i-1] <A[i] and oddheight<K and maxi<A[i]:
            count+=1
            maxi = A[i]
            if A[i-1]%2==1:
                oddheight+=1                   
    return count


            