# Task 2 – Heap and Heap Sort

## Max Heap

A complete binary tree where parent >= children.

Operations: insert, extract_max, build_heap.

Time: O(log n) for insert/extract, O(n) for build.

## Heap Sort

Build heap, extract max repeatedly, reverse for ascending.

Time: O(n log n)

Run: `python Task2/heap_sort.py`

Output:
[1, 3, 4, 5, 10]