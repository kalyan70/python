arr=list(map(int,input().split()))
l=len(arr)
i=0
while i<l:
    if arr[i]==0:
        arr.insert(i,0)
        arr.pop()
        i+=2
    else:
        i+=1
print(arr)
