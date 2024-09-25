n=int(input("how many number you want ? "))
arr=[int(input("enter Value : ")) for i in range(n)]
print(arr)
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr)

