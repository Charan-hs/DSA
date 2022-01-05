from typing import List


def countingSort(numList : List[int]) -> List[int]:
 countList = [0] * (len(numList) + 1)
 print(countList)
 
 return numList

def main() -> None:
 print(countingSort([1,2,3]))

if __name__ == "__main__":
 main()