#single number 2
l = [30000,500,100,30000,100,30000,100]
m={}
for i in l:#2236
    if i in m:
        print(m[i])
        m[i]= m[i]+1
    else:
        m[i]=1
        print(m)
        break        
for k,v in m.items():
    if v==1:
        break
print(k)   

    
