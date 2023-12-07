#合并
def merge( intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort( ) 
    ans = []
    cur_left,cur_right = intervals[0] 
    for i,j in intervals:
        if i>cur_right:
            ans.append([cur_left,cur_right])
            cur_left,cur_right = i,j
        else:
            if j>cur_right:
                cur_right = j 
    ans.append([cur_left,cur_right])
    return ans

#求交
def inter(block1,block2): #block1:  List[int] 
    l1,r1 = block1
    l2,r2 = block2 
    a,b = max(l1,l2),min(r1,r2)
    if a>= b:return None
    return [a,b] 

def interSection(sch1,sch2): #sch1: List[List[int]]
    idx1 ,idx2 = 0,0
    res = []
    while idx1<len(sch1) and idx2<len(sch2):
        ret = inter(sch1[idx1] ,sch2[idx2])
        if ret :
            res.append(ret)
        if sch1[idx1][1] < sch2[idx2][1] :#右边更小的前进
            idx1 += 1
        else:
            idx2 += 1
    return res 


interSection([[1,2],[4,4]] ,[ [2,3],[4,5] ] )