a = input()
i = 0
evensum = 0 
oddsum = 0
while i < len(a):
    if int(a[i])%2 == 0:
        evensum += int(a[i])
        
    if int(a[i])%2 == 1:
        oddsum += int(a[i])
        
    i += 1
    
print(evensum," ",oddsum)
    
