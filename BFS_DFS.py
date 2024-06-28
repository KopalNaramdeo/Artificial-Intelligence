graph={
    '0':['1','2'],
    '1':['0','2','3'],
    '2':['0','1','4'],
    '3':['1','4'],
    '4':['2','3']
}
visited=[]  #to keep track of visited nodes
queue=[]  #for bfs traversal
def bfs(visited,graph,node):  #node is starting point
   #append the starting node to both visited and queue
    visited.append(node)
    queue.append(node)
    while queue:  #while there are nodes in the queue
        m=queue.pop(0)
        print(m,end=" ")
        for neighbor in graph[m]: #iterates over each neighbor of m
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
print("BFS: ")
bfs(visited,graph,'0')

def dfs(graph,node,visited=None):
    #if visited is not provided as arg then it is initialized
    if visited is None:
        visited=[]
    visited.append(node)
    print(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited)
print("\nDFS: ")
dfs(graph,'0')
