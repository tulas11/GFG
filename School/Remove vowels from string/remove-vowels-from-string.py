#User function Template for python3
class Solution:
	def removeVowels(self, S):
		# code here
		vowels="aeiouAEIOU"
		string=""
		for i in S:
		    if i not in vowels:
		        string+=i
		return string


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.removeVowels(s)
		
		print(answer)


# } Driver Code Ends