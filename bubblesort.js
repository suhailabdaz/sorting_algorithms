const arr=[5,8,1,4,44,1]

const bubble=(arr)=>{
    const swap=(arr,left,right)=>{
        [[arr[left],arr[right]]=[arr[right],arr[left]]]
    }
    for(let i=0;i<arr.length;i++){
        for(let j=0;j<arr.length-i-1;j++){
            if(arr[j]>arr[j+1]){
                swap(arr,j,j+1)
            }
        }
    }
    return arr
}
console.log(arr);
bubble(arr);
console.log(arr);

// output:[ 5, 8, 1, 4, 44, 1 ]
// [ 1, 1, 4, 5, 8, 44 ]
