from scipy import optimize as op
import numpy as np  
import math 
class Solution:
    def allZero(self, arr: List[int] )->bool:
        for ele in arr:
            if ele!=0 :
                return False;
        return True 
    def minStickers(self, stickers: List[str], target: str) -> int:
        need = [0]*26 
        for c in target:
            need[ ord(c) - ord('a') ]  += 1
        have = [] 
        for stk in stickers:
            has=[0]*26
            for c in stk:
                if need[ ord(c) - ord('a') ] !=0:
                    has[ ord(c) - ord('a')]  += 1
            if not self.allZero(has):
                have.append(has)
              
        A = np.array(have).transpose().tolist()
        print(A)
        AA=[]
        NEED = [] 
        for i in range(26):
            if need[i] != 0 :
                NEED.append(need[i])
                if self.allZero(A[i]):
                    return -1
                AA.append(A[i])
        c=np.array([1]*len(AA[0]) ) 
        A_ub = - np.array(AA)  
        B_ub=-np.array(NEED) 
        print(A_ub) 
        print(c) 
        print(B_ub) 
         
        
        res=op.linprog(c,A_ub,B_ub, bounds=tuple([(0,len(target) )]* len(AA[0]))  ) #变量个数
         
        print(res) 
        return math.ceil(res.fun-1e-6) 
 
=====================但是题目都要求整数规划==========================


from scipy import optimize as op
import numpy as np  
import math 
#加入整数约束条件求解实现  分枝界定法求解
class Solution: 

    def allZero(self, arr: List[int] )->bool:
        for ele in arr:
            if ele!=0 :
                return False;
        return True 
    def integerPro(self, c, A, b, BOUNDS , t=1.0E-5):
        res =  op.linprog(c, A_ub=A, b_ub=b, bounds = BOUNDS)
        bestVal = 1000000000
        bestX = res.x
        if not(type(res.x) is float or res.status != 0):
            bestVal = sum([x*y for x,y in zip(c, bestX)])
        if all(((x-math.floor(x))<=t or (math.ceil(x)-x)<=t) for x in bestX):
            return (bestVal,bestX)
        else:
            ind = [i for i, x in enumerate(bestX) if (x-math.floor(x))>t and (math.ceil(x)-x)>t][0]
            newCon1 = [0]*len(A[0])
            newCon2 = [0]*len(A[0])
            newCon1[ind] = -1
            newCon2[ind] = 1
            newA1 = A.copy()
            newA2 = A.copy()
            newA1.append(newCon1)
            newA2.append(newCon2)
            newB1 = b.copy()
            newB2 = b.copy()
            newB1.append(-math.ceil(bestX[ind]))
            newB2.append(math.floor(bestX[ind]))
            r1 = self.integerPro(c, newA1, newB1 , BOUNDS = BOUNDS )
            r2 = self.integerPro(c, newA2, newB2 ,  BOUNDS = BOUNDS )
            if r1[0] < r2[0]:
                return r1
            else:
                return r2
    def minStickers(self, stickers: List[str], target: str) -> int:
         
        need = [0]*26 
        for c in target:
            need[ ord(c) - ord('a') ]  += 1
        have = [] 
        for stk in stickers:
            has=[0]*26
            for c in stk:
                if need[ ord(c) - ord('a') ] !=0:
                    has[ ord(c) - ord('a')]  += 1
            if not self.allZero(has):
                have.append(has)
              
        A = np.array(have).transpose().tolist()
        print(A)
        AA=[]
        NEED = [] 
        for i in range(26):
            if need[i] != 0 :
                NEED.append(need[i])
                if self.allZero(A[i]):
                    return -1
                AA.append(A[i])
        c=np.array([1]*len(AA[0]) ) 
        A_ub = - np.array(AA)  
        B_ub=-np.array(NEED)  
        res = self.integerPro(c.tolist(),A_ub.tolist(),B_ub.tolist(), BOUNDS=tuple([(0,len(target) )]* len(AA[0]))  )
        return math.ceil(res[0]-1e-6)

