def sortZerosOnesTwos(array):
    count0=0
    count1=0
    count2=0
    for i in array:
        if i==0:
            count0+=1
        if i==1:
            count1+=1
        if i==2:
            count2+=1
    arr=[]
    for i in range(count0):
        arr.append(0)
    for i in range(count1):
        arr.append(1)
    for i in range(count2):
        arr.append(2)
    return arr
            
        
    
    
print(sortZerosOnesTwos([1,2,2,0,0,0,2]))
