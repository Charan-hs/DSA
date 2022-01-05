import sys 

def getMaxOfListByK(arr: list , k: int) -> int:
 maxSum = -sys.maxsize
 n= len(arr)
 for i in range( n - k +1 ):
  currentSum = 0
  for j in range(k):
   currentSum += arr[i + j]
  maxSum = max(maxSum , currentSum)

 return maxSum



arrList = [100,2,1,4,5,6]
k = 3

if __name__ == "__main__":
 print(getMaxOfListByK(arrList , k))