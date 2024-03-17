
class MergeSort {
  List<int> merge(List<int> array) {
    if (array.length <= 1) {
      return array;
    }
    int mid = array.length ~/ 2;
    List<int> leftArr = merge(array.sublist(0, mid));
    List<int> rightArr = merge(array.sublist(mid));
    return sort(leftArr, rightArr);
  }

  List<int> sort(List<int> leftArr, List<int> rightArr) {
    List<int> result = [];
    int i = 0;
    int j = 0;
    while (i < leftArr.length && j < rightArr.length) {
      if (leftArr[i] < rightArr[j]) {
        result.add(leftArr[i]);
        i++;
      } else {
        result.add(rightArr[j]);
        j++;
      }
    }
    while (i < leftArr.length) {
      result.add(leftArr[i]);
      i++;
    }

    while (j < rightArr.length) {
      result.add(rightArr[j]);
      j++;
    }

    return result;
  }
}

//main function
void main() {
  List<int> array = [1, 2, 5, 6, 7, 4, 3];
  MergeSort ms = MergeSort();
  print(ms.merge(array));
}

/*
output :  
[1, 2, 3, 4, 5, 6, 7]
 */