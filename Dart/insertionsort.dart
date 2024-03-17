void insertionSort(List<int> arr) {
  for (int i = 1; i < arr.length; i++) {
    int temp = arr[i];
    int j = i - 1;
    // Move elements of arr[0..i-1] that are greater than temp
    // to one position ahead of their current position
    while (j >= 0 && arr[j] > temp) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = temp;
  }
}