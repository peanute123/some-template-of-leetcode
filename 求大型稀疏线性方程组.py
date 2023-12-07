1.高斯消元法
2.最小二乘解
2.非负最小二乘
3.稀疏共轭梯度法
#=============================直接解方程==================================================
import scipy

X = scipy.linalg.solve(A, B) # 需要方阵,如果不是方阵 solve(A.T@A, A.T@B)  

#=============================最小二乘解==================================================
#如果非方阵，方程个数大于变量数，矩阵超定。可以最小二乘解
import numpy as np  
from scipy.linalg import lstsq  
def LSQ(m,Ain,people_in):
    A = []
    for peo in Ain:
        a = [0]* m
        for p in peo:
            a[p] = 1
        A.append(a)
    A = np.array(A) 
    B = np.array(people_in)   
    
    X,err,dim,eigen = lstsq(A, B)
    X = [int( max(x,1) +.49) for x in X.tolist()] 
    return X

#============================非负最小二乘==================================================
import scipy
def NNLS(m,Ain,people_in):
    
    A = []
    max_possible = [1]*m 
    for peo,b in zip(Ain,people_in):
        a = [0]* m
        max_v =  b - len(peo) + 1
        for p in peo:
            a[p] = 1
            max_possible[p] = min(max_possible[p],max_v)
        A.append(a)
    A = np.array(A) 
    B = np.array(people_in)   

    for p in range(m):
        A[:,p] *= max_possible[p] 
    
    X,residual = scipy.optimize.nnls( A, B )  
    X = [int( x/max_possible[p] + .49 ) for p, x in enumerate(X.tolist())] 
    return X


#如果说要增加一个正则项，只能从改变系数矩阵入手。
#比如给每一个变量一个 xi = 0 的来惩罚过大的x, 可以下接一个nxn的单位矩阵

A1=np.random.randn( 3,4 )
lamb = 1
n_variables = A1.shape[1]

A2 = np.concatenate([A1, np.sqrt(lamb)*np.eye(n_variables)])
B2 = concatenate([B1, np.zeros(n_variables)])

scipy.optimize.nnls( A2, B2 )  

#============================共轭梯度法==================================================
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import cg
def ConjugateGradient( m,Ain,people_in): 
    row_ind,col_ind = [],[]
    for i,peo in enumerate(Ain) : 
        for p in peo:
            row_ind.append(i)
            col_ind.append(p)   
    B = np.array(people_in)
    #通过三个数组构造稀疏矩阵的
    SPARSE = csc_matrix( ([1]*len(row_ind) , (row_ind, col_ind) ), shape=( len(Ain), m) )
    
    
    X,info = cg(SPARSE.T@SPARSE, SPARSE.T@B,tol=1e-12) #转化成方阵用共轭梯度法求解
    X = [int( max(x,1) +.49) for x in X.tolist()] 
    return X


#共轭梯度法是，每一步都和之前的所有方向，关于 A.T@A这个方阵 正交。 所以最多N步就能到达最优点

 
    

#===================================================================================================================
迭代法看似很简单，像雅可比迭代法，但是这么简单的方法，绝不像网上说的那样什么都可以拿来用。它的条件极为严苛。

那些狗屁博文只会告诉你迭代法好用，不会告诉你需要满足以下条件之一。哪个都不简单。
判断迭代法收敛的办法：

1、首先根据方程组的系数矩阵A的特点判断； 
主对角元绝对占优，这个很难，主对角元绝对值大于该行所有其他绝对值。


2、可根据迭代矩阵的范数判断； 
矩阵的范数是一种度量矩阵大小的方法。矩阵的范数有很多种，比如1范数、2范数、无穷范数等等。其中，1范数是矩阵每一列上的元素绝对值先求和，再从中取个最大的，（列和最大）；2范数是矩阵的所有特征值的平方和再开根号；无穷范数是矩阵每一行上的元素绝对值先求和，再从中取个最大的，（行和最大）。

3、只好根据迭代矩阵的谱半径来判断；
谱半径就是最大特征值，最大特征值必须小于1才能收敛，这个很难，而且算特征值又是一个苦难的问题。


#===================================================================================================================
5.奇异值分解求广义逆矩阵，再求解

N = 5
arr = []
mother = [1] * N
for i in range(N):
    ar = mother[:i] + [0] + mother[i+1:]
    arr.append(ar)

def svd(A):
    U, s, VT = np.linalg.svd(A)
    S = np.zeros_like(A)
    S[:min(A.shape), :min(A.shape)] = np.diag(s)
    return U, S, VT
 
U, S, VT = svd( np.array(arr))
print(U @ S @ VT)#看看还原力度如何


#好,V @ S^-1 @ U 就是系数矩阵的逆矩阵了
#S的对角元是从大到小的排序的特征值，后面有0，需要截断

cut_down = 0
for i in range( min(S.shape)) :
    if abs(S[i,i]) <1e-6:
        cut_down = i;break

reS = np.diag( [ 1/S[i,i] for i in range(cut_down) ])
reA = VT[:cut_down,:].T @ reS @ U[:,:cut_down].T 
x = reA @ np.array(b)   #这就是解了，但是实际差距很大很大

