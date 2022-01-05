# leetcode problem number 410 
def findPices(nums , target):
    pices = 1
    tempSum = 0
    if (len(nums) <1):
        return 0
    
    for number in nums: 
        tempSum += number
        if(tempSum > target):
            pices += 1
            tempSum = number
    return pices
        

        

def splitArray(nums , m):
    start = max(nums)
    end = sum(nums)

    while start <end :
        mid = start + (end - start) //2

        if(findPices(nums , mid) <= m):
            end = mid
        else: 
            start = mid +1
        
    return start

print(splitArray([7,2,5,10,8] , 2))
print(splitArray([1,2,3,4,5] , 2))
print(splitArray([1,4,4] , 3))