
def getnext(s):#真正对的版本，这个模板很强，又简洁。
    n = len(s)
    pi = [0] * n 
    j = 0
    for i in range(1, n):
        while j>0 and s[i] != s[j]:     # 当前位置s[i]与s[j]不等
            #保证前缀中也有部分重叠的地方，可以利用，如果实在想不起来，这里干脆就暴力吧
            j = pi[j-1]                 # j指向之前位置，s[i]与s[j]继续比较 
        if s[i] == s[j]:                # s[i]与s[j]相等，j+1，指向后一位
            j += 1 
        pi[i] = j  
    return pi
getnext("abcabcabc")

getnext("abcabcabc")



def kmp(s,pat):
    next_arr = getnext(pat)  
    print(next_arr)
    j = 0 ;i=0
    ans = [] 
    while i < len(s) : 
        if s[i] != pat[j] : 
            if j==0:i+=1;continue
            j = next_arr[j-1]+1; continue
        j+=1;i+=1
        if j==len(pat):
            ans.append(i-j) 
            j = next_arr[j-1]+1
    return ans


kmp("abcabcabcabc","abcabc")

