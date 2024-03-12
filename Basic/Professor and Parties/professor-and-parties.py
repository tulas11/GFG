#User function Template for python3

class Solution:
    def PartyType(self, a, n):
        # Your code goes here
        d={}
        for i in a:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for elements in d.values():
            if elements>=2:
                return "BOYS"
            
        return "GIRLS"
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.PartyType(a, n))

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends