#two pointer
#nums=list(map(int,input().split()))
nums = [1,2,3,4]
x=5
cnt=0
i=0
j=len(nums)-1
while (i<j):
    if (nums[i]+nums[j]==x):
        cnt+=1
        i+=1
        j-=1
        
    elif(nums[i] + nums[j] < x):
        i+=1
    else:
        j-=1
print(cnt)        
        
