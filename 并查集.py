# 并查集模板
fa = list(range(n))
size = [1] * n
def find(x: int) -> int:
    if fa[x] != x:
        fa[x] = find(fa[x])  #并查集一定要写成路径压缩的形式
    return fa[x]
def merge(from_: int, to: int) -> None:
    from_ = find(from_)
    to = find(to)
    if from_ != to:
        fa[from_] = to
        size[to] += size[from_]   #这个操作会维护每个集合的大小，我就是在这里不知道吃亏的。
    #虽然他总量不守恒，但每个集合的根的size之和是守恒的

#fa一定不能直接用！ 能用的只能是find(x)!!!
#注意：有的人最后统计有多少组时，直接len(set(fa))这是不对的，因为有些点可能还没被路径压缩。应当全部find一遍。
#最终统计 size要用size(find(x))而不是size[x]因为只有根的size是有效的 