
from typing import List


class Solution:
    def duplicates(self, n : int, arr : List[int]) -> List[int]:
        # code here
        #print(arr)
        dup=[]
        for i in range(n):
            #print(arr[0:i], arr[i+1:n], "===>")
            if(arr[i] in arr[0:i]) or (arr[i] in arr[i+1:n]):
                dup.append(arr[i])
                #print(arr[i])
        if(len(dup)==0):
            return [-1]
        
        return sorted(list(set(dup)))
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = IntArray().Input(n)

        obj = Solution()
        res = obj.duplicates(n, arr)

        IntArray().Print(res)

# } Driver Code Ends