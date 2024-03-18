#User function template for Python
# Sure, here's the approach to reverse every sub-array group of size K:

# Iterate through the array:

# Start iterating through the array from index 0.
# Define a while loop that continues until the end of the array is reached.
# Reverse sub-arrays of size K:

# For each sub-array group of size K:
# Determine the start and end indices of the current sub-array group.
# Reverse the elements within this sub-array group.
# Move to the next sub-array group by incrementing the index by K.
# Handling the last sub-array:

# If there are remaining elements at the end of the array that are fewer than K:
# Reverse these remaining elements.
# Continue until the end of the array:

# Continue this process until you reach the end of the array.

class Solution:	
    #Function to reverse every sub-array group of size k.
	def reverseInGroups(self, arr, N, K):
		# code her
        for i in range(0,N,K):
            arr[i:i + K] = reversed(arr[i:i + K])
    	return arr
		    
		


#{ 
 # Driver Code Starts
#Initial template for Python

import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        arr=[int(x) for x in input().strip().split()]
        
        ob = Solution()
        ob.reverseInGroups(arr,N,K)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()




# } Driver Code Ends