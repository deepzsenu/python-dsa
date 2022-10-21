"""Array insert at index
BasicAccuracy: 44.81%Submissions: 62199Points: 1
Insertion is a basic but frequently used operation. Arrays in most languages cannnot be dynamically shrinked or expanded. Here, we will work with such arrays and try to insert an element at some index.

You are given an array arr(0-based index). The size of the array is given by sizeOfArray. You need to insert an element at given index and print the modified array.

Example 1:

Input:
sizeOfArray = 6
arr[] = {1, 2, 3, 4, 5}
index = 5, element = 90
Output: 1 2 3 4 5 90
Explanation: 90 is inserted at index
5(0-based indexing). After inserting,
array elements are like
1, 2, 3, 4, 5, 90.
Example 2:

Input:
sizeOfArray = 6
arr[] = {1, 2, 3, 4, 5}
index = 2, element = 90
Output: 1 2 90 3 4 5
Explanation: 90 is inserted at index 
2(0-based indexing). After inserting,
array elements are like 
1, 2, 90, 3, 4, 5.
Your Task:
You don't need to read input or print anything.. The input is already taken care of by the driver code. You only need to complete the function insertAtIndex() that takes arr, sizeOfArray, index, element as input and modifies the array arr as per requirements. The printing is done by driver code.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
2 <= sizeOfArray <= 10000
0 <= element, arri <= 106
0 <= index <= sizeOfArray-1

 """


def insertAtIndex( arr, sizeOfArray, index, element):
    """n = len(arr)
    for i in range(n-1, index, -1):
        arr[i] = arr[i-1]
        arr[index]  = element"""

    if len(arr)==index:
        arr.append(element)
    else:
        arr.insert(index,element)
    arr = arr.pop()
    return arr
    #Your code here

#  Driver Code Starts
#Initial Template for Python 3


def main():
    T=int(input())
    while(T>0):
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        arr.append(-1)
        index,element=map(int,input().strip().split())
        insertAtIndex(arr,sizeOfArray,index,element)
        for i in range(sizeOfArray):
            print(arr[i],end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()