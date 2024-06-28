def find_parent(parent,i):
    #parent= array with parents of each node
    #i= index of node whose parent we want
    if parent[i]==i: #traverse until it reaches root node
        return i
    return find_parent(parent,parent[i])
#used to perform union on two sets
def union(parent,rank,x,y):
    x_root=find_parent(parent,x)
    y_root=find_parent(parent,y)
    #if it is less root of x = parent of y
    if rank[x_root]<rank[y_root]:
        parent[x_root]=y_root
    elif rank[x_root]>rank[y_root]:
        parent[y_root]=x_root
    else:
        parent[y_root]=x_root
        rank[x_root]+=1
def kruskal(graph,vertices):
    result=[]
    graph.sort(key=lambda item:item[2])
    rank=[0]*vertices
    parent=[i for i in range(vertices)]
    mst=0
    for u,v,weight in graph:
        x=find_parent(parent,u)
        y=find_parent(parent,v)
        if x!=y: #edges do not create a cycle
            result.append((u,v,weight))
            union(parent,rank,x,y)
            mst+=weight
    print("Edge : weight\n")
    for u,v,weight in result:
        print(f"{u}->{v}:{weight}")
    print("MST cost: ",mst)
graph=[(0,1,19),
       (0,2,5),
       (1,0,19),
       (1,2,5),
       (1,3,9),
       (1,4,2),
       (2,1,5),
       (2,4,6),
       (3,1,9),
       (3,4,1),
       (4,1,2),
       (4,2,6),
       (4,3,1)]
vertices=5
kruskal(graph,vertices)
