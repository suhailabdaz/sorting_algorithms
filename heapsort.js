const heapsort = (arr) => {
    const parentindex = (i) => {
        return Math.floor((i - 1) / 2);
    };

    let index = parentindex(arr.length - 1);
    for (let i = index; i >= 0; i--) {
        maxhepify(i, arr, arr.length);
    }

    function maxhepify(index, arr, n) {
        let leftIndex = 2 * index + 1;
        let rightIndex = 2 * index + 2;
        let endindex = n;
        let indextoshift = index;

        if (leftIndex < endindex && arr[leftIndex] > arr[indextoshift]) {
            indextoshift = leftIndex;
        }
        if (rightIndex < endindex && arr[rightIndex] > arr[indextoshift]) {
            indextoshift = rightIndex;
        }
        if (indextoshift !== index) {
            [arr[index], arr[indextoshift]] = [arr[indextoshift], arr[index]];
            maxhepify(indextoshift, arr, n);
        }
    }

    for (let i = arr.length - 1; i > 0; i--) {
        [arr[0], arr[i]] = [arr[i], arr[0]];
        maxhepify(0, arr, i);
    }

    return arr;
};

const arr = [2, 0, 34, 9, -1, 90];
const res = heapsort(arr);
console.log(res);

