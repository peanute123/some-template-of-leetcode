
from collections import deque 
def topOrder(m,edge):  
    g = [ [] for _ in range(m)]
    inDegree,outDegree = [0]*m , [0]*m
    for i,j in edge:
        g[i].append(j)
        inDegree[j] += 1
        outDegree[i] += 1

    toBeDelete = deque( [ i  for i in range(m) if inDegree[i] == 0 ] )
    order = []
    visited = 0
    while toBeDelete:
        top = toBeDelete.popleft( ) #用队列就变成广度优先
        order.append(top)
        visited += 1
        for nex in g[top]:
            inDegree[nex] -=1
            if inDegree[nex] == 0:
                toBeDelete.append(nex)
            
    if visited != m: 
        return [ ] #有环
    return order

topOrder(6,[[0,1],[1,3],[3,2],[4,2],[5,2] ])

#==============================================================

def topOrder(m,edge):  
    g = [ [] for _ in range(m)]
    inDegree,outDegree = [0]*m , [0]*m
    for i,j in edge:
        g[i].append(j)
        inDegree[j] += 1
        outDegree[i] += 1

    toBeDelete = [ i  for i in range(m) if inDegree[i] == 0 ] 
    order = []
    visited = 0
    while toBeDelete:
        top = toBeDelete.pop(-1) #用栈就变成深度优先
        order.append(top)
        visited += 1
        for nex in g[top]:
            inDegree[nex] -=1
            if inDegree[nex] == 0:
                toBeDelete.append(nex)
            
    if visited != m: 
        return [ ] #有环
    return order

topOrder(6,[[0,1],[1,3],[3,2],[4,2],[5,2] ])