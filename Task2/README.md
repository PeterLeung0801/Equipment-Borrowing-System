# Task 2 – Heap and Heap Sort

This directory contains two related concepts:

- **Max Heap** – a data structure and abstract data type (ADT)
- **Heap Sort** – a comparison‑based sorting algorithm that uses the heap ADT

## Max Heap (Data Structure / ADT)

A max heap is a **complete binary tree** stored implicitly in an array where each
parent node is greater than or equal to its children. Because of its structure it
can be efficiently represented as an array: for any index `i`, the left child is
at `2*i+1`, the right child at `2*i+2`, and the parent at `(i-1)//2`.

### Characteristics

- **Type:** Data structure (ADT)
- **Representation:** Array-backed binary tree
- **Heap property:** parent ≥ children (max heap)

### Operations & Time Complexity

| Operation     | Description                                 | Time Complexity |
|---------------|---------------------------------------------|-----------------|
| `insert`      | Add a value, then bubble it up              | O(log n)        |
| `extract_max` | Remove & return root, then heapify down     | O(log n)        |
| `build_heap`  | Turn arbitrary array into max heap          | O(n)            |

### Applications

- Priority queues
- Graph algorithms (Dijkstra, Prim)
- Scheduling systems
- Any scenario requiring fast access to largest element

### Example scenarios

- **Priority queue for a print server:** jobs have different priorities; a max heap
  keeps the highest-priority job at the root so it can be serviced next.

- **Real-time task scheduler:** operating systems and embedded controllers often
  maintain ready tasks in a heap to quickly select the next task with the
  highest priority or earliest deadline.

- **Event simulation:** future events can be managed in a heap ordered by event
  time, allowing the simulator to process the next imminent event in O(log n).

Each of these examples shows how the heap's ability to insert elements and
retrieve the extreme value in logarithmic time makes it a suitable ADT for
priority-driven applications.

## Heap Sort (Algorithm)

Heap sort is a **sorting algorithm** that relies on the heap ADT. It works in two
phases:

1. **Build a max heap** from the input array.
2. **Repeatedly extract** the maximum element (root) and swap it with the last
   element of the heap, then reduce the heap size and re‑heapify.

After extraction is complete the array is sorted in ascending order.

### Steps

```python
# assume `heapify` makes subtree rooted at i a max heap
n = len(arr)
for i in range(n//2-1, -1, -1):       # build heap
    heapify(arr, n, i)
for i in range(n-1, 0, -1):            # extract max repeatedly
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, i, 0)
```

### Time Complexity

- Building heap: **O(n)**
- Each extraction: **O(log n)** and there are n of them
- **Total:** O(n log n) worst/average/best – in-place, not stable

### Example

Run the script to see a generated random list and its sorted result:

python Task2/heap_sort.py


Sample output (your numbers will vary):

Original: [57, 12, 84, 33, 45]
Sorted: [12, 33, 45, 57, 84]

### From initial to max heap

<img width="898" height="665" alt="image" src="https://github.com/user-attachments/assets/467dbc86-f12b-4a93-8f12-73a0115f3e2f" />

