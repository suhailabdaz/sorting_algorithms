        
#.................... find median povit ....................

import statistics
def povit_place(list1,first,last):
    
    m=(first+last)//2
    povit_val=statistics.median([list1[first],list1[m],list1[last]])
    if povit_val == list1[first]:
        ind=first
    elif povit_val == list1[m]:
        ind=m
    else:
        ind=last
    list1[ind],list1[last]=list1[last],list1[ind]
    povit=list1[last]
    left=first
    end=last-1
    
    while True:
        
        while left <= end and list1[left]>=povit:
            left+=1
        while left <= end and list1[end]<=povit:
            end-=1
        if left>end:
            break
        else:
            list1[left],list1[end]=list1[end],list1[left]
    list1[last],list1[left]=list1[left],list1[last]
    return left

def quicksort(list1,first,last):
    
    if first<last:
        
        p=povit_place(list1,first,last)
        quicksort(list1,first,p-1)
        quicksort(list1,p+1,last) 
    
    
    
    
list1=[10,30,2,50,5,20,2]
print(list1)
n=len(list1)
quicksort(list1,0,n-1)
print(list1)
        
        