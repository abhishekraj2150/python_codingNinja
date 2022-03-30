def checkPalindrome(num):
#Implement Your Code Here
	pass
		
n = int(input())
rev = 0
c = n
while n >0:
    a = n%10
    rev = rev*10+a
    n = n//10
if rev == c:
    print("true")
else:
    print("false")
        
