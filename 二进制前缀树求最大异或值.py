'''
这是一类特殊方法，二进制前缀树，其中插入每个长度32的数字，查询是先取反，然后往下，如果没有子树的，代表这一位跟所有数都不一样，它的反也就跟所有数都一样。然后继续往有子树的那个方向走。如果有子树,直接加上这一位的2的幂次。
这样，传播到最小一层就是最大异或值。复杂度是O（CN）但是由于这个C就是32，一般的题目比logN要大，所以实际复杂度比O（NlogN）还可恶一点，经常过不去。
'''


class Node:
    def __init__(self):
        self.left = None
        self.right = None 
        self.isLeaf = False 

class Trie: 
    def __init__(self,depth):
        self.root = Node() 
        self.depth = depth

    def insert(self,num): 
        node = self.root  
        for i in range(self.depth):
            if  num  & (1 << (self.depth - 1- i))  == 0: 
                if not node.left:
                    node.left = Node()
                node = node.left
            else: 
                if not node.right:
                    node.right = Node()
                node = node.right
            if i==self.depth-1:
                node.isLeaf = True 
    def delete(self,num): 
        node = self.root  
        stack = [node]
        for i in range(self.depth):
            if  num  & (1 << (self.depth - 1- i))  == 0:   
                node = node.left
            else:  
                node = node.right
            stack.append(node) 
        while len(stack)>=2 : 
            if stack[-1] == stack[-2].left:
                stack[-2].left = None
                if stack[-2].right:
                    break 
            else:
                stack[-2].right = None
                if stack[-2].left:
                    break 
            stack.pop()  
        
        
    def search(self,num):
        num = (1<<self.depth) - 1 - num 
        node = self.root
        ret = 0   
        for i in range(self.depth):   
            if num  & (1 << (self.depth - 1- i))  == 0: 
                if not node.left:   
                    node = node.right
                else:
                    ret += 1<<(self.depth-1-i)  
                    node = node.left
            else:
                if not node.right: 
                    node = node.left
                else:
                    ret +=  1<<(self.depth-1-i) 
                    node = node.right 
        return ret 

class Solution:
    def findMaximumXOR(self, nums ) -> int:
        depth = max(nums).bit_length()  
#这有个巨坑，就是可能树上的数据位数，和异或运算的数据位数不一样。有些丧心病狂的题，树上只有百万级，但参与查询的是十亿级别。
#所以要求  树上最长的位数，和运算数最长的位数的最大值
        trie = Trie( depth+1 )
        for num in nums:
            trie.insert(num)
        
        ans = 0
        for num in nums:
            tmp =  trie.search(num ) 
            if tmp > ans :
                ans = tmp
        return ans 

