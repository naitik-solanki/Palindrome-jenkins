
def isPalindrome(s):
	return s == s[::-1]
# Driver code
s = "radar"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
