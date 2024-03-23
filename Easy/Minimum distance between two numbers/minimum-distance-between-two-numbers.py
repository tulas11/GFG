
class Solution:
    def minDist(self, arr, n, x, y):
        ans=len(arr)
        first=second=-1
        for i in range(len(arr)):
            if arr[i]==x:
                first=i
                if second!=-1 and abs(first-second)<ans:
                    ans=abs(first-second)
            if arr[i]==y:
                second=i
                if first!=-1 and abs(first-second)<ans:
                    ans=abs(first-second)
        return ans if ans!=len(arr) else -1
            
            
        
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x,y = list(map(int, input().strip().split()))
        print(Solution().minDist(arr, n, x, y))



# } Driver Code Ends