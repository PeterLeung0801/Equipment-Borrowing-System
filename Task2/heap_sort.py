from heap import MaxHeap

def heap_sort(arr):
    heap = MaxHeap()
    heap.build_heap(arr)

    extracted = []
    while heap.heap:
        extracted.append(heap.extract_max())

    return extracted[::-1]

if __name__ == "__main__":
    sample = [4, 10, 3, 5, 1]
    print("Original:", sample)
    print("Sorted:", heap_sort(sample))
    
    sample2 = [42, 17, 93, 8, 56, 31, 64]
    print("\nOriginal:", sample2)
    print("Sorted:", heap_sort(sample2))