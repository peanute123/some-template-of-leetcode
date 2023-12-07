class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.c = [0] * (n + 1)

    #从1开始， array[1]保存1,array[2]保存1与2之和, array[3]保存3,array[4]保存1,2,3,4之和
    def update(self, x, delta):
        while x <= self.n:
            self.c[x] += delta
            x += x & -x

    #这个函数只能求1~x的前缀和 
    #实际使用时，求某一段a~b的和用 query(b) - query(a-1)
    def query(self, x):
        s = 0
        while x:
            s += self.c[x]
            x -= x & -x
        return s

  


bit = BinaryIndexedTree(10)
for i in range(1,11): #不能对0使用
    bit.update(i,i)

#求a[1]~a[10]的和
print(  bit.query(10)-bit.query(0) )