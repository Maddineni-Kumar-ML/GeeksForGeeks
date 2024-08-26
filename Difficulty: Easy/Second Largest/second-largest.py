#User function Template for python3
class Solution:
    def print2largest(self, arr):
        # Code Here
        max1=max(arr)
        while True:
            if(max1 in arr):
                arr.remove(max1)
                continue
            break
        return max(arr)


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.print2largest(arr)
        print(ans)

# } Driver Code Ends