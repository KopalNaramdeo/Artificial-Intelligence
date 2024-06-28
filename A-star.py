graph_node={
    'A':[('B',2),('E',3)],
    'B':[('G',9),('C',1)],
    'C':None,
    'D':[('G',1)],
    'E':[('D',6)]
    }  #stores a key value pair where eg A is connected to B and E with weight 2 and 3 resp
def h(n): #defines heuristic values
    heuristic={
        'A':11,
        'B':6,
        'C':99,
        'D':1,
        'E':7,
        'G':0
    }
    return heuristic[n]
#to retrieve negihbors of node n from graph
def get_neighbors(n):
    if n in graph_node:
        return graph_node[n]
    else:
        return None
    
def astar(start,goal):
    open_set=set(start) #keeps track of nodes for expansion
    closed_set=set()#keeps track of nodes that have been explored
    g={} #stores shortest path from start node to each node
    parents={} #stores the parent node of each node along the current shortest path.
    g[start]=0
    parents[start]=start
    while len(open_set)>0: #continues till there are nodes in openset to be explored
        n=None #n holds node with lowest total cost
        for v in open_set:
            if n==None or g[v]+h(v)<g[n]+h(n):
                n=v
        if n==goal or graph_node[n]==None: 
            #checks if n is goal or it has no neighbor
            pass
        else:
            for (m,weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    g[m]=g[n]+weight
                    parents[m]=n
                else:
                    if g[m]>g[n]+weight:
                        g[m]=g[n]+weight
                        parents[m]=n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n==None:
            print("No path found")
            return None
        if n==goal:
            path=[]
            while parents[n]!=n:
                path.append(n)
                n=parents[n]
            path.append(start)
            path.reverse()
            print("Path -> ",path)
            return path
        open_set.remove(n)
        closed_set.add(n)
astar('A','G')
