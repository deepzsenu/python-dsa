def fun(k,arr):
    i = 0
    while i+1<len(arr):
        j = (arr[i:i+k])
        stri = []
        bin = []
        
        for m in range(len(j)):         
            b = "{0:b}".format(int(j[m]))
            s = b.replace("0", "")
            bin.append(s)
            stri.append(j[m])
            
        minl = len(bin[0])
        nu = stri[0]
        for n in range(len(bin)):
            if len(bin[n])>=minl:
                minl = len(bin[n])
                nu = stri[n]   
                     
        
        print(nu, end = " ")
        i+=1

kn = list(map(int, input().split()))
n = kn[0]
k = kn[1]
arr = list(map(int, input().split()))
fun(k, arr)