
#* heap sort in ascending order 

def heapify(arr,len,i):
    par=i
    left=2*i +1
    right=2*i +2                             #* descending order
                                            
    if left<len and arr[par]<arr[left]:    #* if left<len and arr[par]<arr[left]:
        par=left
        
    if right<len and arr[par]<arr[right]:  #* if right<len and arr[par]>arr[right]:

        par=right
        
    if par != i:
        arr[i],arr[par]=arr[par],arr[i]
        heapify(arr,len,par)
        
def heap_sort(arr):
    
    l=len(arr)
    for i in range(l//2 -1, -1, -1):
        heapify(arr,l,i)
        
    for j in range(l-1,0,-1):
        arr[0],arr[j]=arr[j],arr[0]
        heapify(arr,j,0)
        
    return arr
a=[10,30,50,28,3,5,53]
print(heap_sort(a))