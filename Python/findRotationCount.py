def findPivot(nums):
    start =0
    end = len(nums) -1

    while start <= end:
        mid = start + (end - start) //2
        if(mid <end and nums[mid] > nums[mid+1]):
            return mid
        if(mid>start and nums[mid] < nums[mid -1]):
            return mid -1
        if(nums[mid] > nums[end]):
            end = mid -1
        else:
            start = mid +1
    return -1

def findCount(nums):
    pivot = findPivot(nums)
    if(pivot == -1):
        return 0
    else:
        return pivot +1

print("number of rotation count is " , findCount([8,9,1,2,3,4])) 
