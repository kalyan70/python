'''n=int(input())#40
a=list(map(int,input().split()))
l=0
h=len(a)-1
while l<=h:
    m=l+h>>1
    if a[m]==n:
        print(True)
        break
    elif a[m]<n:
        l=m+1
    else:
        h=m-1
else:
    print(False)
'''
'''def floorSqrt(x):
 
    # Base cases
    if (x == 0 or x == 1):
        return x
 
    # Starting from 1, try all numbers until
    # i*i is greater than or equal to x.
    i = 1; result = 1
    while (result <= x):
     
        i += 1
        result = i * i
     
    return i - 1
 
# Driver Code
x = 11
print()
'''
'''
x=4
i=1
result=1

while result<= x:
    i=i+1
    result=i*i
print(i-1)
'''
"""
count = 0
while (count < 5):
    count += 1;#cnt=1,cnt2cnt3cnt4
    print("Hello Geek")#1234
"""
def kalyan(n,m):
    if n==m:
        
        return True
    else:
        return False
    print(kalyan(n,m))
n=int(input())
m=int(input())


























