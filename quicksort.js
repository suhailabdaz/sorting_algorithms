const array=[0,-90,0,88,2]

const quick=(arr)=>{
    if(arr.length<2){
        return arr
    }
    let pivot=arr[arr.length-1]
    let leftArray=[]
    let rightArray=[]
    for(let i=0;i<arr.length-1;i++){
        if(arr[i]<pivot){
            leftArray.push(arr[i])
        }else{
            rightArray.push(arr[i])
        }
    }
    return [...quick(leftArray),pivot,...quick(rightArray)]
}

console.log(quick(array))

// output:[ -90, 0, 0, 2, 88 ]