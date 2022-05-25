def decodeIP(hex):
    j = str(hex)
    m1,m2,m3,m4 = j[0:2], j[2:4], j[4:6],j[6:]
    
    ip1, ip2, ip3, ip4  = int(m1, 16),int(m2, 16),int(m3, 16),int(m4, 16)
    
    IPadd = str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(ip4)
    
    print(IPadd)
    if ip1>1 and ip1<128:
        print("A")
    if ip1>=128 and ip1<191:
        print("B")
    if ip1>=192 and ip1<223:
        print("C")
    if ip1>=224 and ip1<239:
        print("D")
    if ip1>=240 and ip1<255:
        print("E")
    
    
decodeIP(8000001)
    