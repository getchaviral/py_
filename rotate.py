def rotate_right(arr, d):
    n = len(arr)
    d = d % n 
    return arr[-d:] + arr[:-d]


arr = [1, 2, 3, 4, 5, 6, 7]

rotated_right = rotate_right(arr, 3)
print("  after right rotation  3:", rotated_right)


