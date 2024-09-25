
#............... dscenting order...........
                       
def merge_sort(arr):
    
    if len(arr)>1:
        m=len(arr)//2
        l_arr=arr[:m]
        r_arr=arr[m:]
        merge_sort(l_arr)
        merge_sort(r_arr)
        
        i=j=k=0
        
        while i<len(l_arr) and j<len(r_arr):
            
            if l_arr[i]>r_arr[j]:   #  l_arr[i]<r_arr[j]  (ascenting order)
                arr[k]=l_arr[i]
                i+=1
                k+=1
                
            else:
                arr[k]=r_arr[j]
                j+=1
                k+=1
                
        while i<len(l_arr):
            arr[k]=l_arr[i]
            i+=1
            k+=1
            
        while j<len(r_arr):
            arr[k]=r_arr[j]
            j+=1
            k+=1
        

arr=[12,54,3,65,76,35,34]
merge_sort(arr)
print(arr)