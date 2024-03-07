arr=[1,4,0,9,-1]

const selection=(arr)=>{
    for(let i=0;i<arr.length-1;i++){
        let minindex=i
        for(let j=i+1;j<arr.length;j++){
            if(arr[j]<arr[minindex]){
                minindex=j
            }
        }
            [arr[i],arr[minindex]]=[arr[minindex],arr[i]]
    }
    return arr
}
console.log(arr);
selection(arr)
console.log(arr);

// output:[ 1, 4, 0, 9, -1 ]
// [ -1, 0, 1, 4, 9 ]