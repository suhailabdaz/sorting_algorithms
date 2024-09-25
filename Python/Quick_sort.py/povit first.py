# .............................quick sort(povit first)...........................

def povit_place(list1,first,last):
    
    povit=list1[first]
    left=first+1
    right=last
    
    while True:
        
        while left<=right and list1[left]<=povit:    #  while left<=right and list1[left]>=povit: (dscenting order)
            left += 1
        while left<=right and list1[right]>=povit:   #  while left<=right and list1[right]<=povit: (dscenting order)
            right -= 1
        if left>right:
            break
        else:   
            list1[left],list1[right]=list1[right],list1[left]
    list1[first],list1[right]=list1[right],list1[first]
    return right

def quicksort(list1,first,last):
    
    if first<last:
        
        p=povit_place(list1,first,last)
        quicksort(list1,first,p-1)
        quicksort(list1,p+1,last)
        
arr=[12,46,87,9,7,90]
quicksort(arr,0,len(arr)-1)
print(arr)

