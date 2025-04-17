def min_operations_to_equal(arr, k):
    max_val = max(arr)
    operations =0

    for num in arr:
        diff = max_val - num
        operations =operations + (diff + k - 1) // k

    return operations