import random

def heap_sort(arr):
    # Sorts the given array using the heap sort algorithm.
    # 使用 heap sort algorithm 對給定數組進行排序。

    # First, builds a max heap by calling heapify on all non-leaf nodes.
    # 首先，通過對所有 non-leaf nodes 調用 heapify 來構建最大 heap。
    # Then, repeatedly swaps the root (maximum element) with the last element and calls heapify on the reduced heap to maintain the heap property.
    # 然後，反復將root（最大元素）與最後一個元素交換，並在縮小的堆上調用 heapify 以維持堆屬性。
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, n, i):
    # Maintains the max heap property for the subtree rooted at index i. The heap is represented in the array arr, with n elements.
    # 維持以索引 i 為 root 的子樹的最大 heap 屬性。heap 在數組 arr 中表示，有 n 個元素。

    # Compares the root with its left and right children, and swaps with the largest
    # 將 root 與其左和右子節點比較，並與最大的交換

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

if __name__ == "__main__":
    # generate simple random lists
    sample = random.sample(range(1, 100), 5)
    print("Original:", sample)
    print("Sorted:", heap_sort(sample[:]))
    
    sample2 = random.sample(range(1, 100), 10)
    print("\nOriginal:", sample2)
    print("Sorted:", heap_sort(sample2[:]))
