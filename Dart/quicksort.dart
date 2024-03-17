
class QuickSort {
  List<int> quick(List<int> array) {
    sort(array, 0, array.length - 1);
    return array;
  }

  void sort(List<int> array, int start, int end) {
    if (start >= end) {
      return;
    }
    int pivot = start;
    int left = start + 1;
    int right = end;
    while (left <= right) {
      if (array[left] > array[pivot] && array[right] < array[pivot]) {
        swap(array, left, right);
        left++;
        right--;
      }
      if (array[left] <= array[pivot]) {
        left++;
      }
      if (array[right] >= array[pivot]) {
        right--;
      }
    }
    swap(array, pivot, right);
    sort(array, start, right - 1);
    sort(array, right + 1, end);
  }

  void swap(List<int> array, int i, int j) {
    int temp = array[i];
    array[i] = array[j];
    array[j] = temp;
  }
}

//main function
void main() {  
  List<int> arr = [1, 4, 3, 6, 4, 3, 9];
  arr.forEach((element) {
    print(element);
  });
  QuickSort q = QuickSort();
  print(q.quick(arr));
}
/*
output : 
1
4
3
6
4
3
9

[1, 3, 3, 4, 4, 6, 9]
 */
