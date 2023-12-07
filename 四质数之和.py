#把一个>=8的数拆成4个质数之和
#哥德巴赫猜想，>4的偶数可以写成两个奇数质数之和。
#所以偶数必然可以拆成2+2+p1+p2
#所以奇数必然可以拆成2+3+p1+p2

def two_prime(target):
    #质数最大间隔不超过246，所以 n-246~n之间必然至少存在一个质数。之多遍历246个一定能找到！
    for x in range(2,246):   
        y = target - x
        if y >= 2 and is_prime(x) and is_prime(y):
            return [x, y]
    return [-1, -1]  #这是不存在的

def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
 
target = int(input())
if target % 2 == 0:
    ret = two_prime(target - 4)
    print(f"{2} {2} {ret[0]} {ret[1]}")
else:
    ret = two_prime(target - 5)
    print(f"{2} {3} {ret[0]} {ret[1]}")