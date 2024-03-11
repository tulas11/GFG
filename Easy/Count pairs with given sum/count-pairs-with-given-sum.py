#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        cc=0
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        # print(d)   
        for i in arr:
            if k-i!=i:
                if k-i in d:
                    cc=cc+d[k-i]
            else:
                if k-i in d:
                    cc=cc+d[k-i]-1
        # print(cc) 
        return cc//2
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends