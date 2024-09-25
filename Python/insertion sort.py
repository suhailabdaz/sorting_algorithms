
#................. insertion sort...................


def insertion(arr):
    
    for i in range(1,len(arr)):
        curr=arr[i]
        ind=i
        while arr[ind-1]>curr and ind>0:
            
            arr[ind]=arr[ind-1]
            ind-=1
        arr[ind]=curr
        
arr=[12,44,3,65,87,45]

insertion(arr)
print(arr)