# Binary Search in loop

def binarySearch(arr , l , r,x):
    while l<r:
        mid = (l+(r-1))//2
        if(arr[mid] == x):
            return x
        elif (arr[mid]>x):
            r= mid -1
        else : 
            l= mid+1
    
#Binary Search => Recursive

def binarySearchRes(arr  ,l , r, x):
    if l<r:
        mid = (l+(r-1))//2
        if(arr[mid] == x):
            return x
        elif arr[mid] > x:
           return binarySearchRes(arr, l, mid-1,x)
        else:
           return binarySearchRes(arr , mid+1 , r, x)
    else:
        return

            
def printResult(result , x):
    if(result):
        print(x," found in array")
    else:
        print(x," not found in array")
    
if(__name__ == "__main__"):
    arr = [x for x in range(1000)]
    x= 564
    printResult(binarySearch(arr ,0,len(arr), x),x)
    printResult(binarySearchRes(arr ,0,len(arr), x),x)
    x=100000
    printResult(binarySearch(arr ,0,len(arr), x),x)
    printResult(binarySearchRes(arr ,0,len(arr), x),x)



