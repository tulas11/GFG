#User function Template for python3

# function should return a triplet
# if no such triplet is found return
# a container results as empty
def findTriplet(arr,n):
    
    # your code here
    for i in range(n):
        for j in range(i+1,n):
            s=arr[i]+arr[j]
            if s in arr:
                return [arr[i],arr[j],s]
    return []



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for j in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        a=findTriplet(arr,n)
        if(len(a)==3):
            print(1)
        else:
            print(-1)
# } Driver Code Ends