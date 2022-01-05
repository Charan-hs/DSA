
def findPivot( nums):
    start = 0
    end = len(nums) -1
    
    while start <= end:
        mid = start + (end - start)//2
        # print(start , end  , mid)
        
        if(mid<end and nums[mid] >nums[mid+1]):
            return mid
        if(mid>start and nums[mid-1] > nums[mid]):
            return mid -1
        
        if(nums[start] == nums[mid] and nums[end] == nums[end]):
            # print("enter")
            if(start <end  and nums[start] > nums[start + 1]):
                return start
            start +=1 
            if(end>start  and nums[end] < nums[end -1]):
                return end -1
            end -=  1
            
        
        elif(nums[mid]>nums[start] or (nums[mid] == nums[start] and nums[mid] > nums[end])):
            start = mid +1
        else:
            end = mid -1
        
    return -1


def binarySearch(nums , start , end , target):
    # print(start ,end , target , "kadbcjdc")
    
    while start <= end:
        mid = start + (end - start) //2
        # print(nums[mid] , target, "mid")
        
        if(nums[mid] == target):
            return target
        if(nums[mid] > target):
            end = mid -1
        else:
            start = mid +1
    return -1
            

def search(nums, target):
    
    pivot = findPivot(nums)
    # print((pivot) , "pivot")
    if (pivot != -1):
        foundInAsc = binarySearch(nums , 0,pivot,target)
        # print(foundInAsc)
        if(foundInAsc == -1):
            if(binarySearch(nums , pivot+1 , len(nums)-1 , target) == -1):
                return False
            else:
                return True
        else :
            return True
    else:
        found = binarySearch(nums ,0 , len(nums)-1 , target)
        # print(found , "found")
        if (found == -1):
            # print("return  from here")
            return False
        else: 
            return True
            

print(search([1,0,1,1],0))
        
        