def findCellingOfArry(arr , target):
    start = 0
    end = len(arr)-1
    
    while start <end:
        mid = start + (end - start) //2
        
        if(arr[mid] == target):
            return mid
        elif arr[mid] > target:
            end = mid 
        else: 
            start = mid+1
    return start

print(findCellingOfArry([2,3,5,9,14,16,18],5))
#find celling of a number => returns a number which is equal to target or greater then target which is lowest number in that part of array.
