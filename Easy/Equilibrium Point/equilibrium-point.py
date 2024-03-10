# User function Template for python3
import math
class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        if len(A)==1:
            return 1
        else:
            sumi=0
            newsum=0
            element=0
            for i in range(N):
                sumi+=A[i]
            #print(sumi)
            for i in range(N-1):
                newsum+=A[i]
                if(newsum==sumi-A[i+1]-newsum):
                    return i+2
        return -1   
            



#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends