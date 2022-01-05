#34 leetcode

def findIndexOfTarget( nums , target, isStart):
    start = 0
    end = len(nums) -1
    currentFoundPosition = -1
    while start <= end : 
        mid = start +(end- start)//2
        if(nums[mid] == target):
            currentFoundPosition = mid
            if(isStart):
                end = mid -1
            else:
                start = mid +1
        elif(nums[mid] > target):
            end = mid - 1
        else:
            start  = mid +1
    return currentFoundPosition
    
def searchRange( nums, target):
    ans = [-1 ,-1]
    if len(nums) == 0:
        return ans
    ans[0] = findIndexOfTarget(nums , target , True)
    ans[1] = findIndexOfTarget(nums , target , False)
    return ans

print(searchRange([5,7,7,8,8,10] , 7))