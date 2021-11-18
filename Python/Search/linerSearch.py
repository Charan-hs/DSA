def linearSearch(arr,A):
    for x in arr:
        if(x ==A):
            return x
    return 
def printResult(result , x):
    if(result):
        print(x," found in array")
    else:
        print(x," not found in array")
    
if(__name__ == "__main__"):
    arr = [1,234,4545,6536,564,647,76,75,75,2542,25,4542545,4545,2454545,4524,2423,424,2425246,576764,647]
    x= 564
    printResult(linearSearch(arr , x),x)
    x=10000
    printResult(linearSearch(arr , x),x)
