#User function Template for python3
import sys
def findElement( arr, n):
    minArr=[None]*(n)
    maxArr=[None]*(n)
    big=0
    small= sys.maxsize
    for i in range(n):
        if arr[i]>big:
            big=arr[i]
        maxArr[i]=big
        
    for i in range(n-1,-1,-1):
        if arr[i]<small:
            small=arr[i]
        minArr[i]=small
    for i in range(n):
        if i!=0 and i!=(n-1):
            if minArr[i]==maxArr[i]:
                return arr[i]
                break
    return -1
        
