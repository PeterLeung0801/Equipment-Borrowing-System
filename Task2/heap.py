class MaxHeap:
    def __init__(self):
        # Initializes an empty max heap.
        # 初始化一個空的最大堆。

        # The heap is stored as a list.
        # HEAP 存儲為列表。
        self.heap = []

    def insert(self, value):
        # Inserts a new value into the max heap.
        # 將新值插入最大 HEAP。

        # The value is appended to the end of the heap list, then _heapify_up is called.
        # 該值附加到 HEAP LIST 的末尾，然後調用 _heapify_up。
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        # Removes and returns the maximum element (root) from the max heap.
        # 從最大 HEAP 中移除並返回最大元素（root）。

        # If the heap is empty, returns None.
        # 如果 HEAP 為空，返回 None。
        # If only one element, pops it directly.
        # 如果只有一個元素，直接彈出它。
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # Otherwise, swaps the root with the last element, pops the last element, and calls _heapify_down on the root to restore the heap property.
        # 否則，將 ROOT 與最後一個元素交換，彈出最後一個元素，並在根上調用 _heapify_down 以恢復 HEAP 屬性。
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def build_heap(self, arr):
        # Builds a max heap from the given array.
        # 從 array 構建最大 HEAP。

        # Copies the array into the heap list, then calls _heapify_down on all non-leaf nodes starting from the bottom to establish the heap property throughout the structure.
        # 將 array 複製到 HEAP LIST 中，然後從底部開始對所有 non-leaf nodes 調用 _heapify_down，以在整個結構中建立 HEAP 屬性。
        self.heap = arr[:]
        for i in range((len(arr) // 2) - 1, -1, -1):
            self._heapify_down(i)

    def _heapify_up(self, index):
        # Restores the max heap property by bubbling up the element at the given index.
        # 通過 bubbling up 給定索引處的元素來恢復最大 HEAP 屬性。

        # Compares the element with its parent; if larger, swaps and recursively calls _heapify_up on the parent index until the heap property is satisfied.
        # 將元素與 parent node 比較；如果更大，交換並在 parent 索引上遞歸調用 _heapify_up，直到 heap 屬性滿足。
        # Used after inserting a new element to maintain the heap structure.
        # 用於插入新元素後維持 heap 結構。
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        # Restores the max heap property by bubbling down the element at the given index.
        # 通過 bubbling down 給定索引處的元素來恢復最大 HEAP 屬性。

        # Compares the element with its left and right children; if a child is larger, swaps with the largest child and recursively calls _heapify_down on that child index.
        # 將元素與其左和右子節點比較；如果子節點更大，交換與最大的子節點交換，並在該子索引上遞歸調用 _heapify_down。
        # Used after extracting the max or building the heap to maintain the heap structure.
        # 用於提取最大值或構建堆後維持 HEAP 結構。
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)
