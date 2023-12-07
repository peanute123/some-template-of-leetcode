grid = [ 
    [1,2,4,3],
    [5,1,2,4],
    [6,3,5,9]
]
print(grid)
#=================================================================
# 对子矩阵进行增减操作。
def update(diff,x1,y1,x2,y2,val):
    diff[x1][y1] += val # 左上角加val
    diff[x2+1][y1] -= val # 右上角减val
    diff[x1][y2+1] -= val # 左下角减val
    diff[x2+1][y2+1] += val # 右下角加val

# diff尺寸必须大上一圈
m ,n = len(grid) , len(grid[0])
diff = [ [0]*( n+1 ) for _ in range(m+1) ]
for i in range( m):   
    for j in range( n):
        update(diff,i,j,i ,j ,grid[i][j])  #建议单个修改，也用区间修改。

print(diff)

#==========================还原=======================================
for i in range(m):
    for j in range(n):
        if i == 0 and j == 0 :
            grid[i][j] = diff[i][j]  
        if i == 0 and j != 0 :
            grid[i][j] = diff[i][j] + grid[i][j-1] 
        if j == 0 and i != 0 :
            grid[i][j] = diff[i][j] + grid[i-1][j]
        if i != 0 and j != 0 :
            grid[i][j] = diff[i][j] + grid[i-1][j] + grid[i][j-1] - grid[i-1][j-1]
        #if grid[i][j] == 0: return False
print(grid)

#最后，别用numpy.diff
#=============================================================================
#这里还有一个误区，以为二维差分可以用于求二维区间的和。实际恰恰相反，南辕北辙了属于是。
#区间和，仍然要求助于前缀和。

presum = [ [0]*(n+1) for _ in range(m) ] 
for i in range(m):
    for j in range(n):
        presum[i][j+1] = presum[i][j] + grid[i][j]
presumH = [ [0]*(n+1) for _ in range(m+1) ] 
for i in range(m):
    for j in range(n+1):
        presumH[i+1][j] = presumH[i][j] + presum[i][j]
    
def sum_of_area(x1,y1,x2,y2): 
    return (presumH[x2+1][y2+1] - presumH[x2+1][y1]) - (presumH[x1][y2+1] - presumH[x1][y1])
#其实就是四块板子，大板减去两中板，加上小板
#不过，如果改变了，可以对前缀和做差分。。。 

#=============================================================================
#离散化二维差分模板，注意右边下边要给坐标+1，所以要加入多一倍的点。


points = [[2,1], [6,2]] #输入点
m  = 2# 输入m
def check(day,points):
    pxs = set()
    pys = set()
    for px,py in  points :
        pxs.add(px - day)
        pxs.add(px + day +1)
        pys.add(py - day )
        pys.add(py + day +1)
    
    pxs = sorted(list(pxs))
    pys = sorted(list(pys))
    mapx = { v:k for k,v in enumerate(pxs) }
    mapy = { v:k for k,v in enumerate(pys) }
    m,n = len(mapx) + 1 ,len(mapy) + 1
    diff = [ [0]*n for _ in range(m)] 
    for px,py in points :
        diff[ mapx[px - day] + 1 ][ mapy[py - day] + 1 ] += 1
        diff[ mapx[px - day] + 1 ][ mapy[py + day + 1] + 1 ] -= 1
        diff[ mapx[px + day + 1] + 1 ][ mapy[py - day]  + 1] -= 1
        diff[ mapx[px + day + 1]  + 1][ mapy[py + day + 1] + 1 ] += 1  
    ans = 0
    #还原从1开始，0行0列不用还原了本来就是
    for i in range(1,m ):
        for j in range(1,n):
            diff[i][j] += diff[i-1][j] + diff[i][j-1] - diff[i-1][j-1] 
            ans = max( ans , diff[i][j]) 
    return ans



left,right = 0,10**9
while left<=right:
    mid = left + (right- left)//2
    if check(mid,points) <  m :
        left = mid + 1 
    else:
        right = mid - 1

print(left)



