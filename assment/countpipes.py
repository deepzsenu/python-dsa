from collections import Counter as cnt
def printResult(arr, m):
    count = cnt(arr)
    j = []
    for i in count:
        j.append(i)
    print(len(j))
    for i in j:
        print(i, end = " ")
    print()
    
    

def main():
    m = int(input())
    strs = input().split()
    arr = []
    for i in strs:
        arr.append(int(i))
        
    printResult(arr, m)
main()