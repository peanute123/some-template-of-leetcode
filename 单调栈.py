def dandiaozhan(arr):
    stack = []
    n = len(arr)
    prevBiggerIndex = [-1]*n
    nextBiggerIndex = [n]*n 
    for i,num in enumerate(arr):
        while stack and arr[ stack[-1] ]< arr[i]:
            if len( stack )>1:
                prevBiggerIndex[ stack[-1] ] = stack[-2]
            nextBiggerIndex[ stack[-1] ] = i
            stack.pop(-1)
        stack.append(i)
    while stack:
        if len( stack )>1:
            prevBiggerIndex[ stack[-1] ] = stack[-2] 
        stack.pop(-1)
    return prevBiggerIndex,nextBiggerIndex
dandiaozhan([1,2,4,5,3])

 

#==================================================================================================
#但是单独用到单调栈的很少，都是嵌在别的问题里，比如这一类，长度为k的最大可能的整数

def biggestSubseq(arr ,k): #单调栈找长度为1,2,3,...k的最大的序列
    if k==0:return []
    stack = []
    n = len(arr)
    remain = n-k 
    ret = [ ]
    for i,num in enumerate(arr):
        while stack and arr[ stack[-1] ]< arr[i]: 
            stack.pop(-1)
        stack.append(i)
        if remain==0:
            ret.append( arr[stack[0]] )
            stack.pop(0)
        else:
            remain -= 1
    return ret


biggestSubseq([9,1,2,5,8,3] ,3)