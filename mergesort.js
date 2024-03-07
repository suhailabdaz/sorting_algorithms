const array = [1, 0, 8, 3,-67,1];

const mergesort = (arr) => {
    if(arr.length<2){
        return arr
    }
    const mid = Math.floor(arr.length / 2);
    const leftArray = arr.slice(0, mid);
    const rightArray = arr.slice(mid);
    return merge(mergesort(leftArray), mergesort(rightArray));
}

const merge = (leftArray, rightArray) => {
    let sortedArray = [];

    while (leftArray.length && rightArray.length) {
        if (leftArray[0] <= rightArray[0]) {
            sortedArray.push(leftArray.shift());
        } else {
            sortedArray.push(rightArray.shift());
        }
    }

    return [...sortedArray, ...leftArray, ...rightArray];
}
console.log(mergesort(array));

// output:[ -67, 0, 1, 1, 3, 8 ]
