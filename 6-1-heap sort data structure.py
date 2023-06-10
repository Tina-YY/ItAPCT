# root: A[0], left child: 2*i+1, right child: 2*i+2, parent: (i - 1) / 2, start build: n/2 - 1
class BigRootHeap:
    length = None
    heap_size = None
    data = None

    def __init__(self, A):
        self.length = len(A)
        self.heap_size = self.length
        # not change the original sort of array A
        self.data = A.copy()
        self._build_heap()

    def _max_heapify(self, i):
        case = 0

        if (i << 1) + 1 < self.heap_size and self.data[i] < self.data[(i << 1) + 1]:
            temp = self.data[i]
            self.data[i] = self.data[(i << 1) + 1]
            self.data[(i << 1) + 1] = temp
            case = 1
        if (i << 1) + 2 < self.heap_size and self.data[i] < self.data[(i << 1) + 2]:
            temp = self.data[i]
            self.data[i] = self.data[(i << 1) + 2]
            self.data[(i << 1) + 2] = temp
            case = 2

        if case == 1:
            self._max_heapify((i << 1) + 1)
        if case == 2:
            self._max_heapify((i << 1) + 2)

    def _build_heap(self):
        start = ((self.length - 1) >> 1) - 1
        for i in range(start, -1, -1):
            self._max_heapify(i)

    def heap_sort_recursive(self):
        if self.heap_size == 0:
            self.heap_size = self.length
            return

        temp = self.max_element()
        self.data[0] = self.data[self.heap_size - 1]
        self.data[self.heap_size - 1] = temp

        self.heap_size = self.heap_size - 1
        self._max_heapify(0)
        self.heap_sort_recursive()

    def heap_sort_loop(self):
        i = self.heap_size - 1
        while i >= 0:
            temp = self.max_element()
            self.data[0] = self.data[i]
            self.data[i] = temp
            self.heap_size = self.heap_size - 1
            self._max_heapify(0)
            i -= 1
        self.heap_size = self.length

    def max_element(self):
        return self.data[0]

    def insert_element(self, x):
        self.length = self.length + 1
        self.heap_size = self.heap_size + 1
        self.data.append(-9999999)
        self.update_element_by_key(self.length - 1, x)

    # default: x > self.data[i]
    def update_element_by_key(self, i, x):
        self.data[i] = x
        while i > 0 and self.data[i] > self.data[(i - 1) >> 1]:
            self.data[i] = self.data[(i - 1) >> 1]
            self.data[(i - 1) >> 1] = x
            i = (i - 1) >> 1

    def delete_element_by_key(self, i):
        self.length = self.length - 1
        self.heap_size = self.heap_size - 1
        if self.data[i] > self.data[self.length]:
            self.data[i] = self.data[self.length]
            self._max_heapify(i)
        if self.data[i] < self.data[self.length]:
            self.update_element_by_key(i, self.data[self.length])

    def return_data(self):
        return self.data[:self.length]


# tests
A = [5, 3, 17, 10, 84, 19, 6, 22, 9]
heap = BigRootHeap(A)
heap.heap_sort_recursive()
print("heap sort recursive:", heap.data)

heap = BigRootHeap(A)
heap.heap_sort_loop()
print("heap sort loop:", heap.return_data())

print("original line:", A)
heap = BigRootHeap(A)
print("after once built:", heap.return_data())
heap.insert_element(100)
print("after insert:", heap.return_data())
heap.update_element_by_key(4, 120)
print("after update:", heap.return_data())
heap.delete_element_by_key(4)
print("after delete a number:", heap.return_data())
