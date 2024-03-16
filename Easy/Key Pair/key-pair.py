#User function Template for python3
class Solution:
        # code here
        def hasArrayTwoCandidates(self, arr, n, x):
            d = {}
            for i in range(n):
                if arr[i] in d:
                    d[arr[i]] += 1
                else:
                    d[arr[i]] = 1
        
            for i in range(n):
                if x - arr[i] in d:
                    if x - arr[i] != arr[i] or d[x - arr[i]] > 1:
                        return 1
        
            return 0

        
        






#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.hasArrayTwoCandidates(arr, n, x)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends