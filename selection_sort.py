def selectionSort(array):
    size=len(array)  #if not user defined then take size as arg
    for step in range(size):
        min_index=step  #while the loop iterates each element i.e step is considered as min 
        for i in range(step+1,size): #iterates through the unsorted portion i.e step+1 till end of array
            if array[i]<array[min_index]:
                min_index=i
        (array[step],array[min_index])=(array[min_index],array[step])
'''data=[-2,0,3,-10,22]
size=len(data)'''
min_elements=int(input("Enter no of elements you want: "))
print(f"Enter {min_elements} elements separated by space: ")
data=input().split()[:min_elements]
data=[int(x) for x in data]

selectionSort(data)
print("Sorted in ascending order: ")
print(data)