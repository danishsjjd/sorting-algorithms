def bubble_sort(arr):
    for i in range(0, len(arr)):
        swapped = False
        for j in range(1, len(arr) - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                swapped = True
        if not swapped:
            break
    return arr
