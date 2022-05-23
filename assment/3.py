def stringRemover(string, arr):
    
    for i in arr:
        string = string.replace(i,"")                      
    return string

str = "Hello"
a = ["e","o"]
print(stringRemover(str,a))                