n=int(input("How much values you want add "))
print("enter values")
arr=[]
for i in range(n):
    arr.append(int(input()))
print(arr)

for i in range(len(arr)-1,0,-1):
    
    for j in range(i):
        
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)