def binarySearch(nums ,start,end , target):
    if start<=end:
        mid = start + (end - start)//2
        if(nums[mid] == target):
            return mid
        elif (nums[mid]<target):
            return binarySearch(nums , mid+1 , end,target)
        else:
            return binarySearch(nums,start,mid-1,target)
    return -1

def findPositionOfInfinteArray(nums , target):
    start = 0
    end = 1

    while start<=end:
        if(nums[-1]<target):
            return -1
        
        if(nums[end]<target):
            start = end+1
            end = start*2
            
        else:
            return binarySearch(nums,start,end,target)
            
        
        
            
if __name__ == "__main__":
    nums = [x for x in range(1000)]
    print(findPositionOfInfinteArray(nums , 56))
    print(findPositionOfInfinteArray(nums , 56000))
    print(findPositionOfInfinteArray(nums , -56))