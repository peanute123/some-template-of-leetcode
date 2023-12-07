#普通版本
n = 10
left = [0]*(n*4)
right = [0]*(n*4)
#lazy = [0]*(n*4)
sum0 = [0]*(n*4)
max0 = [0]*(n*4)  
def build(idx,L,R):
    left[idx] = L
    right[idx] = R
    if L!=R:
        build(idx*2,L,(L+R)//2)
        build(idx*2+1,(L+R)//2+1,R)  

def update(idx,L,R,v):
    if L==left[idx] and R==right[idx] and L==R: 
        sum0[idx]+= v
        max0[idx]+= v
        return 
    le,ri =  left[idx] ,right[idx]
    mid = (le + ri)//2
    if L<=mid:
        if R<=mid:
            update(idx*2,L,R,v) 
        else:
            update(idx*2,L,mid,v)
            update(idx*2+1,mid+1,R,v)
    else:
        update(idx*2+1,L,R,v)
    sum0[idx] += v*(R-L+1)
    max0[idx] = max(max0[idx*2],max0[idx*2+1] )

def query(idx,L,R):
    if L==left[idx] and R==right[idx] and L==R: 
        return sum0[idx],max0[idx]
     
    le,ri =  left[idx],right[idx]
    mid = (le + ri)//2
    if L<=mid:
        if R<=mid:
            return query(idx*2,L,R) 
        else:
            s1,m1= query(idx*2,L,mid )
            s2,m2= query(idx*2+1,mid+1,R )
            return s1+s2,max(m1,m2)
    else:
        return query(idx*2+1,L,R ) 
build(1,0,9)
#print(left,right)
arr=[[0,4,1],[5,9,1],[3,7,1]]
for l,r,v in arr:
    update(1,l,r,v) 

print([query(1,i,i) for i in range(10)])

#====================================================再改成懒更新=====================================================
nums1 = []
n = len(nums1)
left = [0]*(n*4)
right = [0]*(n*4) 
lazy = [1]*(n*4)
sum0 = [0]*(n*4) 
def build(idx,L,R):
    left[idx] = L
    right[idx] = R
    if L!=R:
        build(idx*2,L,(L+R)//2)
        build(idx*2+1,(L+R)//2+1,R)  

def update(idx,L,R):
    if L== left[idx] and R==right[idx]:
        sum0[idx] = R - L + 1 - sum0[idx] 
        lazy[idx] *= -1
        return 
    le,ri =  left[idx] ,right[idx]
    mid = (le + ri)//2
    pushdown(idx)
    if L<=mid:
        if R<=mid:
            update(idx*2,L,R ) 
        else:
            update(idx*2,L,mid )
            update(idx*2+1,mid+1,R )
    else:
        update(idx*2+1,L,R )
    sum0[idx] = sum0[idx*2] + sum0[idx*2+1]

def pushdown(idx):
    lazy[idx*2] *=  lazy[idx] 
    lazy[idx*2+1] *=  lazy[idx]
    if lazy[idx] == -1: 
        sum0[idx*2] = right[idx*2] - left[idx*2] + 1 - sum0[idx*2] 
        sum0[idx*2+1] = right[idx*2+1] - left[idx*2+1] + 1 - sum0[idx*2+1]
    lazy[idx] = 1

def query(idx,L,R):
    if L== left[idx] and R==right[idx]: 
        return sum0[idx]  
    pushdown(idx)
    le,ri =  left[idx],right[idx]
    mid = (le + ri)//2
    if L<=mid:
        if R<=mid:
            return query(idx*2,L,R) 
        else: 
            return query(idx*2,L,mid )+query(idx*2+1,mid+1,R ) 
    else:
        return query(idx*2+1,L,R )  

build(1,0,n-1)
for i,num in enumerate(nums1):
    if num == 1:
        update(1, 0 , n-1,  i,i ) #注意前面三个参数是代表，入口，只能是1,节点1的左边界，节点1的右边界，可以扩大，但一旦确定，永远不能变了！
print(sum0)
ans = [] 
[query(1,0,n-1,i,i) for i in range(n)]

#===================================最后改成动态开点====================================

#我这个L和R是紧紧跟着区间缩小的，而不是不变的，因此查询区间是不固定的，所以无法得知新开的点左右边界应该是什么，得全部推翻重来。
#因为真正的动态开点线段树，是不用知道节点号，也能自然知道左右区间的。
#因为会遍历到哪些区间，从一开始就完全决定了的。
# 稍微改造下就好了，build都是多余的
nums1 = [0,1,0,1,0,1,0,1,0,1]
n = len(nums1)
lazy = [1]*(n*4)
sum0 = [0]*(n*4)  

def update(idx,lc,rc,L,R):
    if L <= lc and rc <= R:
        sum0[idx] = rc - lc + 1 - sum0[idx] 
        lazy[idx] *= -1
        return  
    mid = (lc + rc)//2
    pushdown(idx,lc,rc) #注意，此时不再有left和right数组了，因为当前节点的left和right的值就是lc,rc
    if L <= mid: update(idx*2,lc,mid,L,R ) 
    if R > mid: update(idx*2+1,mid+1,rc,L,R ) 
    sum0[idx] = sum0[idx*2] + sum0[idx*2+1]#回收

def pushdown(idx,lc,rc):
    lazy[idx*2] *=  lazy[idx] 
    lazy[idx*2+1] *=  lazy[idx]
    mid = (lc + rc)//2
    if lazy[idx] == -1: 
        sum0[idx*2] = mid - lc + 1 - sum0[idx*2] 
        sum0[idx*2+1] = rc - mid - sum0[idx*2+1]
    lazy[idx] = 1

def query(idx,lc,rc,L,R):
    if L <= lc and rc <= R:
        return sum0[idx]  
    pushdown(idx,lc,rc) 
    mid = (lc + rc)//2
    ret = 0 
    if L <= mid: ret += query(idx*2,lc,mid,L,R ) 
    if R > mid: ret += query(idx*2+1,mid+1,rc,L,R )  
    return ret

#build(1,0,n-1)
for i,num in enumerate(nums1):
    if num == 1:
        update(1, 0 , n-1,  i,i ) #注意前面三个参数是代表，入口，只能是1,节点1的左边界，节点1的右边界，可以扩大，但一旦确定，永远不能变了！
print(sum0)
ans = [] 
[query(1,0,n-1,i,i) for i in range(n)]

#===========================然后就很简单了，弄成动态开点，只要把idx*2 ,idx*2+1的部分，改成left,right保存指针就好了=====================
nums1 = [0,1,0,1,0,1,0,1,0,1]
n = len(nums1) 
lazy = [1]*(n*4)
sum0 = [0]*(n*4)
left_child = [0]*(n*4)
right_child = [0]*(n*4)
cnt = 1 
def lazy_create(idx):
    global cnt
    if idx>cnt: # 代表此处没有点，创建
        cnt += 1
    if left_child[idx] == 0:
        cnt += 1
        left_child[idx] = cnt  #每次都必然创建两个点，而且right_child必然比left_child大1，所以其实只要一个left就够了
        cnt += 1
        right_child[idx] = cnt  


def update(idx,lc,rc,L,R):
    lazy_create(idx)
    if L <= lc and rc <= R:
        sum0[idx] = rc - lc + 1 - sum0[idx] 
        lazy[idx] *= -1
        return  
    mid = (lc + rc)//2
    pushdown(idx,lc,rc)
    if L <= mid: update( left_child[idx] ,lc,mid,L,R ) 
    if R > mid: update( right_child[idx] ,mid+1,rc,L,R )  
    sum0[idx] = sum0[ left_child[idx] ] + sum0[ right_child[idx] ]#回收

def pushdown(idx,lc,rc):
    lazy[ left_child[idx] ] *=  lazy[idx] 
    lazy[ right_child[idx] ] *=  lazy[idx]
    if lazy[idx] == -1: 
        mid = (lc + rc)//2
        sum0[ left_child[idx] ] = mid - lc + 1- sum0[ left_child[idx] ] 
        sum0[ right_child[idx] ] = rc - mid - sum0[ right_child[idx] ]
    lazy[idx] = 1

def query(idx,lc,rc,L,R):
    lazy_create(idx)
    if L <= lc and rc <= R:
        return sum0[idx]  
    pushdown(idx,lc,rc) 
    mid = (lc + rc)//2
    ret = 0 
    if L <= mid: ret += query( left_child[idx],lc,mid,L,R ) 
    if R > mid: ret += query( right_child[idx] ,mid+1,rc,L,R )  
    return ret
     
#build(1,0,n-1)
for i,num in enumerate(nums1):
    if num == 1:
        update(1, 0 , n-1,  i,i ) 
print(sum0)
ans = [] 
[query(1,0,n-1,i,i) for i in range(n)]

#========================为了省空间，不用初始化一个大数组，改成一点点追加=========================

nums1 = [0,1,0,1,0,1,0,1,0,1]
n = len(nums1) 
lazy = [1] 
sum0 = [0] 
left_child = [0]  
def lazy_create(idx): 
    if idx >= len(sum0):
        lazy.append(1)
        sum0.append(0)
        left_child.append(0) 
    if left_child[idx] == 0:
        left_child[idx] = len(sum0)
        lazy.append(1)
        sum0.append(0)
        left_child.append(0)  
        lazy.append(1)
        sum0.append(0)
        left_child.append(0) 

def update(idx,lc,rc,L,R):
    lazy_create(idx)
    if L <= lc and rc <= R:
        sum0[idx] = rc - lc + 1 - sum0[idx] 
        lazy[idx] *= -1
        return  
    mid = (lc + rc)//2
    pushdown(idx,lc,rc)
    if L <= mid: update( left_child[idx] ,lc,mid,L,R ) 
    if R > mid: update( left_child[idx]+1 ,mid+1,rc,L,R )  
    sum0[idx] = sum0[ left_child[idx] ] + sum0[ left_child[idx]+1 ]#回收

def pushdown(idx,lc,rc):
    ls = left_child[idx] 
    lazy[ ls  ] *=  lazy[idx] 
    lazy[ right_child[idx] ] *=  lazy[idx]
    if lazy[idx] == -1: 
        mid = (lc + rc)//2
        sum0[ ls ] = mid - lc + 1- sum0[ ls ] 
        sum0[ ls+1 ] = rc - mid - sum0[ ls+1 ]
    lazy[idx] = 1

def query(idx,lc,rc,L,R):
    lazy_create(idx)
    if L <= lc and rc <= R:
        return sum0[idx]  
    pushdown(idx,lc,rc) 
    mid = (lc + rc)//2
    ret = 0 
    if L <= mid: ret += query( left_child[idx],lc,mid,L,R ) 
    if R > mid: ret += query( right_child[idx] ,mid+1,rc,L,R )  
    return ret
     
#build(1,0,n-1)
for i,num in enumerate(nums1):
    if num == 1:
        update(1, 0 , n-1,  i,i ) 
print(sum0)
ans = [] 
[query(1,0,n-1,i,i) for i in range(n)]

#但是由于某些题目就是单点修改，所以必然开到最小的叶节点为止，此时提升不了多少。
#======================================================================================
#最后，换成结构体
class Node:
    def __init__(self):
        self.lazy = 1
        self.val = 0
        self.left = 0


nums1 = [0,1,0,1,0,1,0,1,0,1]
n = len(nums1) 
lazy = [1] 
sum0 = [0] 
left_child = [0]  
NODES = [None]


def lazy_create(idx): 
    if idx >= len(NODES):
        NODES.append( Node() ) 
    if NODES[idx].left == 0:
        NODES[idx].left = len(NODES)
        NODES.append( Node() )  
        NODES.append( Node() )  

def update(idx,lc,rc,L,R):
    lazy_create(idx)
    if L <= lc and rc <= R:
        NODES[idx].val = rc - lc + 1 - NODES[idx].val 
        NODES[idx].lazy *= -1
        return  
    mid = (lc + rc)//2
    pushdown(idx,lc,rc)
    ls = NODES[idx].left
    if L <= mid: update( ls ,lc,mid,L,R ) 
    if R > mid: update( ls + 1 ,mid+1,rc,L,R )  
    NODES[idx].val = NODES[ls].val + NODES[ls+1].val #回收

def pushdown(idx,lc,rc):
    ls =  NODES[idx].left
    NODES[ ls ].lazy *=  NODES[ idx ].lazy
    NODES[ ls+1 ].lazy *=  NODES[ idx ].lazy
    if NODES[ idx ].lazy == -1: 
        mid = (lc + rc)//2
        NODES[ ls ].val = mid - lc + 1 - NODES[ ls ].val
        NODES[ ls + 1].val = rc - mid -  NODES[ ls + 1 ].val
    NODES[idx].lazy = 1

def query(idx,lc,rc,L,R):
    lazy_create(idx)
    if L <= lc and rc <= R:
        return NODES[idx].val
    pushdown(idx,lc,rc) 
    ls =  NODES[idx].left
    mid = (lc + rc)//2
    ret = 0 
    if L <= mid: ret += query( ls,lc,mid,L,R ) 
    if R > mid: ret += query( ls + 1 ,mid+1,rc,L,R )  
    return ret
      
for i,num in enumerate(nums1):
    if num == 1:
        update(1, 0 , n-1,  i,i ) 
ans = [] 
[query(1,0,n-1,i,i) for i in range(n)]

#太好了，至此，我也终于有了自己的线段树模板