
# .............................quick sort(povit random)...........................


import random
    
def povit_place(list1,first,last):
    r=random.randint(first,last)
    list1[r],list1[last]=list1[last],list1[r]
    povit=list1[last]
    left=first
    end=last-1
    while True:
        
        while left<=end and list1[left]<=povit:
            left+=1
        while left<=end and list1[end]>=povit:
            end-=1
        if left>end:
            break
        else:
            list1[left],list1[end] = list1[end],list1[left]
    list1[last],list1[left]=list1[left],list1[last]
    return left

def quicksort(list1,first,last):
    
    if first<last:
        p=povit_place(list1,first,last)
        quicksort(list1,first,p-1)
        quicksort(list1,p+1,last)
        
arr=[12,46,87,9,7,90]
quicksort(arr,0,len(arr)-1)
print(arr)