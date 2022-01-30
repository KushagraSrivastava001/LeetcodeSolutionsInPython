def permutation(string,answer):
    if len(string)==0:
        print(answer,end=' ')
        return
    for i in range(len(string)):
        ch=string[i]
        left=string[0:i]
        right=string[i+1:]
        result=left+right
        permutation(result,answer+ch)
s="abcd"
ans=""
permutation(s,ans)
