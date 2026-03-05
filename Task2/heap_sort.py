def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, n, i):
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
    sample = [4, 10, 3, 5, 1]
    print("Original:", sample)
    print("Sorted:", heap_sort(sample[:]))
    
    sample2 = [42, 17, 93, 8, 56, 31, 64]
    print("\nOriginal:", sample2)
    print("Sorted:", heap_sort(sample2[:]))