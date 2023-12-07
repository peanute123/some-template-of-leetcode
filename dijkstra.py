#自己写的渣渣python实现

graph=[ [] for _ in range(n)]
for i,j,v in edges:
    graph[i].append((j,v+1))
    graph[j].append((i,v+1))

def dijkstra(graph):
    dist=[10**9+1]*n 
    used=[False]*n
    q = [(0,0)]
    used[0]=True  
    while q  :
        di , i = heappop(q)
        if di<dist[i]: 
            dist[i] = di 
            used[i] = True
            for j,v in graph[i]:
                if not used[j]:
                    heappush(q, ( dist[i]+v ,j ) )
    return dist

distance = dijkstra(graph)