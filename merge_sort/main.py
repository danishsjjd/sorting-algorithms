def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    half_length = len(arr) // 2
    return merge(merge_sort(arr[:half_length]), merge_sort(arr[half_length:]))


def merge(a, b):
    results = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            results.append(b[j])
            j += 1
        else:
            results.append(a[i])
            i += 1

    while i < len(a):
        results.append(a[i])
        i += 1

    while j < len(b):
        results.append(b[j])
        j += 1

    return results
