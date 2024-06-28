INF=999999
v=5 #no of vertices in the graph
graph=[
    [0,4,0,3,5],
    [4,0,2,0,0],
    [0,2,0,1,0],
    [3,0,1,0,0],
    [5,0,0,0,0]
]
no_edges=0 #keeps track of number of edges in MST
visited=[0,0,0,0,0] 
visited[0]=True #keeps track of all visited vertices
                #initial vertex is 1 i.e visited
print("Edge  :","Weight\n")
while(no_edges<v-1):
    a=0
    b=0
    min=INF
    for i in range(v):
        if visited[i]:
            #checks if i vertex is visited
            for j in range(v):
                if((not visited[j]) and graph[i][j]):
                    #indicates an edge has not been included in MST yet
                    if graph[i][j]<min:
                        min=graph[i][j]
                        a=i
                        b=j
    print(a,"-",b,":",graph[a][b],"\n")
    no_edges+=1
    visited[b]=True
