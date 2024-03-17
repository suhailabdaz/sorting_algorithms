//Heap sort function
List<int> heapSort(MinHeap minHeap) {
  List<int> sortedList = [];
  
  while (minHeap.heap.isNotEmpty) {
    int minElement = minHeap.peek();
    sortedList.add(minElement);
    minHeap.remove();
  }

  return sortedList;
}
// construction of heap
class MinHeap {
  List<int> heap = [];

  MinHeap(List<int> list) {
    buildHeap(list);
  }

  void buildHeap(List<int> list) {
    heap = list;
    for (int i = parent(heap.length - 1); i >= 0; i--) {
      shiftDown(i);
    }
  }

  void shiftDown(int current) {
    int end = heap.length - 1;
    int left = leftChild(current);

    while (left <= end) {
      int right = rightChild(current);
      int idxToShift;

      if (right <= end && heap[right] < heap[left]) {
        idxToShift = right;
      } else {
        idxToShift = left;
      }

      if (heap[current] > heap[idxToShift]) {
        swap(heap, current, idxToShift);
        current = idxToShift;
        left = leftChild(current);
      } else {
        return;
      }
    }
  }

  void shiftUp(int current) {
    int parents = parent(current);
    while (current > 0 && heap[parents] > heap[current]) {
      swap(heap, current, parents);
      current = parents;
      parents = parent(current);
    }
  }

  int parent(int i) {
    return (i - 1) ~/ 2;
  }

  int leftChild(int i) {
    return 2 * i + 1;
  }

  int rightChild(int i) {
    return 2 * i + 2;
  }

  void swap(List<int> list, int i, int j) {
    int temp = list[i];
    list[i] = list[j];
    list[j] = temp;
  }

  int peek() {
    return heap[0];
  }

  void display() {
    for (int i = 0; i < heap.length; i++) {
      print(heap[i]);
    }
  }

  void remove() {
    swap(heap, 0, heap.length - 1);
    heap.removeLast();
    shiftDown(0);
  }

  void insert(int data) {
    heap.add(data);
    shiftUp(heap.length - 1);
  }
}




// for example main function is provided

void main(List<String> args) {
  List<int> list = [9, 7, 8, 6, 3, 4, 5, 1];
  MinHeap minHeap = MinHeap(list);
  print("Min Heap:");
  minHeap.display();
  List<int> sortedList = heapSort(minHeap);
  print("\nSorted Array:");
  for (int i = 0; i < sortedList.length; i++) {
    print(sortedList[i]);
  }
}

// Solution is commented

/* 

Min Heap:
1
3
4
6
9
8
5
7

Sorted Array:
1
3
4
5
6
7
8
9

*/