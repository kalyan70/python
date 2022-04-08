"""arr=[1,2,3,4,5,6,7]
prefix=[0 for i in range(len(arr))]
print(prefix)#[0, 0, 0, 0, 0, 0, 0]
prefix[0]=arr[0]#first element always same in prefix
for i in range(1,len(prefix)):
    
    prefix[i]=prefix[i-1]+arr[i]
print("prefix:",prefix)
print("arr   :",arr)
for j in range(1,len(prefix)):
    prefix[j]=prefix[j-1]-arr[i]
print("prefix :",prefix)
#output
prefix inti[0, 0, 0, 0, 0, 0, 0]
arr        : [1, 2, 3, 4, 5, 6, 7]
prefix +ve: [1, 3, 6, 10, 15, 21, 28]
prefix -ve : [1, -6, -13, -20, -27, -34, -41]      
"""
test_list = [3, 4, 1, 7, 9, 1]
k=sum[test_list[::-1]]
print(k)
