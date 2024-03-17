#User function Template for python3
class Solution:

	def fascinating(self,n):
	    # code here
        two=str(n*2)
    	three=str(n*3)
    	fascinating=str(n)+two+three
    # 	print(fascinating)
    	if set(fascinating)==set("123456789") and len(fascinating)==9:
    	        return "Fascinating"
	    
	            


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input().strip())
        ob = Solution()
        ans = ob.fascinating(n)
        if ans:
            print("Fascinating")
        else:
            print("Not Fascinating")
        tc -= 1

# } Driver Code Ends