import sys
vertices=[[0,0,1,1,0,0,0],
          [0,0,1,0,0,1,0],
          [1,1,0,1,1,0,0],
          [1,0,1,0,0,0,1],
          [0,0,1,0,0,1,0],
          [0,1,0,0,1,0,1],
          [0,0,0,1,0,1,0]]
#1 if there is an edge 0 if there is no edge
edges=[[0,0,1,2,0,0,0],
       [0,0,2,0,0,3,0],
       [1,2,0,1,3,0,0],
       [2,0,1,0,0,0,1],
       [0,0,3,0,0,2,0],
       [0,3,0,0,2,0,1],
       [0,0,0,1,0,1,0]]
num_of_vertices=len(vertices[0])
visited_distance=[[0,0]] #first is whether visited or not and second is distance
for i in range(num_of_vertices-1):
    visited_distance.append([0,sys.maxsize])
def to_be_visited():#finds next vertex to visit based on the shortest distance
    global visited_distance
    v=-10
    for index in range(num_of_vertices):
        if visited_distance[index][0]==0 and(v<0 or visited_distance[index][1]<=visited_distance[v][1]):
            #checks whether each vertex has been visited and no vertex has been selected yet or
            #the distance of current vertex is less than the previous
            v=index
    return v
for vertex in range(num_of_vertices):
    to_visit=to_be_visited()  #called to find the next vertex to visit
    for neighbor in range(num_of_vertices):
        if vertices[to_visit][neighbor]==1 and visited_distance[neighbor][0]==0:
        #checks if there is an edge bw tovisit vertex and neighbor
        #and if the neighbor has not been visited yet
            new_distance=visited_distance[to_visit][1]+edges[to_visit][neighbor]
            #If the neighbor is valid, it calculates the new distance to reach the neighbor from the source vertex
            if visited_distance[neighbor][1]>new_distance:
                visited_distance[neighbor][1]=new_distance
    visited_distance[to_visit][0]=1
i=0 #keep track of current vertex being printed
for distance in visited_distance:
    print("Distance of ",chr(ord('a')+i),"from source vertex: ",distance[1])
    #chr(ord('a') + i): This converts the current index i to its corresponding letter representation, starting from 'a'.
    #distance[1] = shortest distance
    i+=1


