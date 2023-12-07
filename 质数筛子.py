    def get_prime_list(M):
        primes_list=[] 
        min_prime_factor=[-1]*(M+1)
        div = [1]*(M+1)
        for i in range(2,M+1):
            if div[i]==0:continue
            min_prime_factor[i]=i
            primes_list.append(i) 
            j=i
            while i*j<=M:
                div[i*j]=0 
                if min_prime_factor[i*j]<0:
                    min_prime_factor[i*j]=i
                j+=1 
        return primes_list,min_prime_factor

#分解质因数
def factorize(num):
            ans = [] 
            for i in primes_list:
                if num in primes_set:
                    ans.append(num);break
                if i >num:break
                if num%i==0:
                    ans.append(i)
                while num%i == 0: 
                    num//=i
            return ans

#快速分解质因数（批量)
#因为是批量，可以用一个临时数组保存每个数的最小质因数。这是创建质数筛的时候顺便做的
#然后迭代来获得一个数的所有质因数
    def factorize(num):
        ans = set() 
        while num>1:
            temp = min_prime_factor[num]
            ans.add(temp)
            num//=temp 
        return ans

#最大公约数
    def gcd(  x,  y): 
        return x if y==0 else gcd(y,x%y) 

#组合数
#python3.8 里的math有math.comb(k,a)
#但是很快就溢出了。所以这是带大数余数的。
def combine(K,a):
        MOD = int(1e9+7)
        temp=[0]*(K+1)
        new =[0]*(K+1)
        new[0]=1
        for i in range(1,K+1):
            temp = new.copy()
            new[0]=1;new[i]=1
            for j in range(1,i):
                new[j] =(temp[j-1]+temp[j])%MOD
        return new[a] 






 
#========================一个很弱的分解质因数板子===============================

prime_list = []
M=10**6
vis = [False]*(M+1)

for i in range(2,M+1):
    if not vis[i]:
        vis[i] = True
        prime_list.append(i)
        j = i*i
        while j<=M:
            vis[j] = True
            j += i 

prime_set = set(prime_list) 
#保存最小质因子的方法更快，但是只能动态规划从小到大，也不保存一整个。
@cache
def factorize(num):
    ret = []
    if num == 1:return ret 
    for p in prime_list:  
        if num in prime_set:
            ret.append((num,1)) ;break
        c = 0
        while num%p == 0:  
            num//=p
            c += 1
        if c>0:
            ret.append((p,c)) 
        if num == 1 :break
    return ret