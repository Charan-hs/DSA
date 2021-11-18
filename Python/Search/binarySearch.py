def binarySearch(arr , l , r,x):
    while l<r:
        mid = (l+(r-1))//2
        if(arr[mid] == x):
            return x
        elif (arr[mid]>x):
            r= mid -1
        else : 
            l= mid+1

            
def printResult(result , x):
    if(result):
        print(x," found in array")
    else:
        print(x," not found in array")
    
if(__name__ == "__main__"):
    arr = [x for x in range(1000)]
    x= -564
    printResult(binarySearch(arr ,0,len(arr), x),x)
    x=100000
    printResult(binarySearch(arr ,0,len(arr), x),x)
