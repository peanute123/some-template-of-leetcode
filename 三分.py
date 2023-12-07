 
left = 1; right = 10
def check(mid):          
    return   (mid-5)**2 #凹函数

while left   < right :
    mid1 = (left*2 + right) // 3
    mid2 = (left + right*2) // 3
    if check(mid1)>check(mid2):
        left = mid1 + 1
    else:
        right =  mid2 - 1  
check(left) 


