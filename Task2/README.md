# Task 2 – Self Study on Heap and Heap Sort

## 1. Data Structure: Max Heap

A heap is a complete binary tree that satisfies the heap property.

In a Max Heap:
The value of each parent node is greater than or equal to its children.

### Abstract Data Type (ADT)

Operations supported:
- insert(value)
- extract_max()
- build_heap()

### Time Complexity

- insert(): O(log n)
- extract_max(): O(log n)
- build_heap(): O(n)

### Applications

- Priority queue implementation
- Task scheduling systems
- Graph algorithms

---

## 2. Algorithm: Heap Sort

Heap Sort is a comparison-based sorting algorithm built on the Heap data structure.

### Procedure

1. Insert all elements into a Max Heap.
2. Repeatedly extract the maximum element.
3. Reverse the extracted sequence to obtain ascending order.

### Time Complexity

- Best Case: O(n log n)
- Worst Case: O(n log n)
- Space Complexity: O(1)

### Example

Input:
[4, 10, 3, 5, 1]

Output:
[1, 3, 4, 5, 10]