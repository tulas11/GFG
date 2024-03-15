#User function Template for python3

class Solution:
    def modify(self, s):
        # code here
        a=list(s)
        v=set("aeiouAEIOU")
        
        left=0
        right=len(a)-1
        
        while left<right:
            if a[left] not in v:
                left= left+1 
            elif a[right] not in v:
                right= right-1
            else:
                a[left],a[right]=a[right],a[left]
                left=left+1 
                right=right-1
        
        return "".join(a)
                
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.modify(s)
        print(ans)
# } Driver Code Ends