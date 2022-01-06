def findIn2DArray(nums , target):
    n= len(nums)
    row = 0
    col = n -1

    while (row < n and col >=0):
        if(nums[row][col] == target):
            return [row , col]
        elif(nums[row][col] > target):
            col -= 1
        else:
            row += 1
    return -1


def binarySearchCol(nums ,col,target):
    start = 0
    end = len(nums) -1

    while start < end:
        mid = start + (end - start) //2

        if(nums[mid][col] == target):
            return mid
        elif(nums[mid][col] > target):
            end = mid -1
        else:
            start = mid +1
    return start

def binarySearchRow(nums ,row, target):
    start = 0
    end = len(nums[row]) -1
    
    while start <=end:
        mid = start + (end - start) //2
        
        if(nums[row][mid] == target):
            return mid
        elif(nums[row][mid] > target):
            end = mid -1
        else : 
            start  = mid +1
    return -1
        
#for seq number in entire matrix
def findIn2DArray2(nums , target):
    row = 0
    col = len(nums[0])-1

    row = binarySearchCol(nums , col , target)
    if(row >= len(nums)): 
        row  = len(nums) -1
    
    col = binarySearchRow(nums , row , target)
    if(col == -1):
        return [ -1 , -1]
    else:
        return [row , col]


arr = [[10 ,20 ,30 ,40],[15 ,25,35,45],[28,29,37,49],[33,34,38,50]]
print(findIn2DArray(arr,28))
# print(binarySearch([1,2,3,4] , 0))
print(findIn2DArray2([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]] , 14))
