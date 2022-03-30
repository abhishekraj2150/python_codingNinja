def reverse(n):
#Implement Your Code Here
	pass	

n=int(input())
rev = 0
while n>0:
    d = n%10
    n = n//10
    rev = rev*10+d
    
result = rev
print(result)
