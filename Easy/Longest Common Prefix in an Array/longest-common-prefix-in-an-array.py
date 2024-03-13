#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        arr.sort()
        a=0
        b=0
        st=""
        while(a<len(arr[0]) and b<len(arr[n-1])):
            if arr[0][a] != arr[n-1][b]:
                break
            st+=arr[0][a]
            a+=1
            b+=1
        if(st==""):
            return "-1"
        return st
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends