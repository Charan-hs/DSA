def peakIndexInMountainArray( arr):
    start  = 0 
    end  = len(arr) - 1

    while start <= end:
        mid  = start + (end - start) //2
        if ( mid+1>= len(arr)):
            start  = mid
            break
            
        if(arr[mid] > arr[mid + 1]):
            # we are in dec part of array
            end = mid -1
        else: 
            # we are in asc part of array
            start = mid +1
    return arr[start]
        