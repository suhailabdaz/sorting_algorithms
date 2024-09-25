
# .............................quick sort(povit last) dscenting order...........................



def povit_place(arr,first,last):
    
    povit=arr[last]
    left=first
    right=last-1
    
    while True :
        
        while left<=right and arr[left]>=povit:
            left += 1
        while left<=right and arr[right]<=povit:
            right -= 1
        if left >right:
            break
        
        else:
            
            arr[left],arr[right] = arr[right],arr[left]
    arr[last],arr[left] = arr[left],arr[last]
    return left
def quicksort(arr,first,last):
    
    if first<last:
        
        p=povit_place(arr,first,last)
        quicksort(arr,first,p-1)
        quicksort(arr,p+1,last)

arr=[12,46,87,9,7,90]
quicksort(arr,0,len(arr)-1)
print(arr)