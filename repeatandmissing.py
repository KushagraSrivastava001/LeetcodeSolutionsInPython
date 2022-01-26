def findTwoElement(arr, n):
        d={}
        for i in range(1,n+1):
            if i not in d:
                d[i]=0
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        arr1=[]
        for key in d.keys():
            if d[key]==2:
                arr1.append(key)
            if d[key]==0 :
                arr1.append(key)
                
        return arr1
        
    
    
print(findTwoElement([1,2,2],3))
