class Solution:
    def print2largest(self, arr, n):
        first = second = float('-inf')

        # There should be at least two elements
        if n < 2:
            return -1

        for i in range(n):
            # If current element is greater
            # than first then update both
            # first and second
            if arr[i] > first:
                second = first
                first = arr[i]

            # If arr[i] is in between first
            # and second then update second
            elif arr[i] > second and arr[i] != first:
                second = arr[i]

        if second == float('-inf'):
            return -1
        else:
            return second
# class Solution:
# 	def print2largest(self,arr, n):
# 		# code here
# 		arry=sorted(set(arr))
# 		if len(arry)==1:
# 		    return -1
# 		else:
# 		    return arry[-2]

#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
