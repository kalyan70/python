#suffix_sum

arr=[10,20,30,40,50]
n=len(arr)
suffix_sum=[0 for i in range(n)]#this line work all elements zero

#print(suffix_sum)

suffix_sum[n-1]=arr[n-1]#in pefix[0]=n[0]
for i in range(n-2,-1,-1):
    suffix_sum[i]=suffix_sum[i+1]+arr[i]
print(suffix_sum)

#prefix_sum
arr1=[10,20,30,40,50]
m=len(arr1)
pr=[0 for i in range(m)]
pr[0]=arr1[0]
for j in range(1,len(pr)):
    pr[j]=pr[j-1]+arr1[j]
print(pr)
k=sum(suffix_sum)
n=sum(pr)
print(k,n)
