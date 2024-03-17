class Selection {
  List<int> selectionSort(List<int> array) {
    for (var i = 0; i < array.length - 1; i++) {
      int small = i;
      for (var j = i + 1; j < array.length; j++) {
        if (array[small] > array[j]) {
          small = j;
        }
      }
      //swap
      int temp = array[small];
      array[small] = array[i];
      array[i] = temp;
    }
    return array;
  }
}
