def isSubset( a1, a2, n, m):
    d={}
    for i in a2:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for key in d.keys():
        if key not in a1:
            return "No"
            
    return "Yes"
            
    
