'''
Kruskal 算法
Kruskal 算法是一种常见并且好写的最小生成树算法，由 Kruskal 发明。该算法的基本思想是从小到大加入边，是一个贪心算法。

其算法流程为：
将图 G={V,E} 中的所有边按照长度由小到大进行排序，等长的边可以按任意顺序。

初始化图 G'为{V,∅}，从前向后扫描排序后的边，如果扫描到的边 e 在 G'中连接了两个相异的连通块,则将它插入 G'中。

最后得到的图 G'就是图 G 的最小生成树。

在实际代码中，我们首先将这张完全图中的边全部提取到边集数组中，然后对所有边进行排序，从小到大进行枚举，每次贪心选边加入答案。使用并查集维护连通性，若当前边两端不连通即可选择这条边。
'''
#====================================================== 
def Kruskal(m,edge):
    fa = list(range(m))
    def find(x):
        if fa[x] != x:
            fa[x] = find(fa[x])
        return fa[x]
    def union(x,y):
        fx, fy = find(x),find(y)
        fa[fx] = fy 
    edge.sort(key=lambda x: x[2]) 
    mst = []
    value = 0
    for i,j,v in edge:
        if find(i) != find(j):
            union(i,j)
            mst . append((i,j))
            value += v
    return value,mst
Kruskal( 4,[ [0,1,10],[0,2,11],[0,3,12],[1,2,13],[1,3,14], [2,3,6]  ])



#==========================================================#======================================================
'''
Prim 加点
点集：每次比较点集与非集合的点，最小距离添加新的点。
看起来每新增一个点是 i*(V-i)，应该是O(n^3)
实际可以通过维护一个每个点与点集的最小距离数组，达到总体O(n^2)的复杂度。
'''
#======================================================
from heapq import heappush,heappop
def Prim(m,edge): 
    g = [ [] for _ in range(m)]
    edge.sort(key=lambda x: x[2])
    for i,j,v in edge:
        g[i].append((j,v))
        g[j].append((i,v))

    mst = []
    ans = 0
    left=set([0])
    toBeAdd = []

    INF = 10**9 ; dist = [INF]*m   #dist[0] = 0
    valids = [ None for _ in range(m)] 
    for j,v in g[0]:
        dist[j] = v
        valids[j] = [v,j,0,True] #保存每个点，加入左边时，用以连接的那条边
        heappush(toBeAdd,valids[j]) #利用懒删除堆，去掉已经过时了的最短边信息
   
    while toBeAdd:
        while toBeAdd and not toBeAdd[0][3]:
            heappop( toBeAdd )
        if len(toBeAdd)==0:break
        v,j,i,_ = heappop( toBeAdd )
        left.add(j)
        ans += v
        mst.append((i,j))
        valids[j][3] = False 
        for jj,v in g[j]: 
            if jj not in left and v<dist[jj]:#可能被这条边更新的所有点，更新他们的距离。松弛操作
                valids[jj][3]=False
                dist[jj] = v
                valids[jj] = [v,jj,j,True]
                heappush(toBeAdd,valids[jj])
        
    return ans,mst
Prim( 4,[ [0,1,10],[0,2,11],[0,3,12],[1,2,13],[1,3,14], [2,3,6]  ])

