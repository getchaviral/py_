arr = [1, 20, 24, 4, 9]
arr = list(set(arr))

arr.sort(reverse=True)

if len(arr) >= 2:
    print("Second largest element:", arr[1])
else:
    print("No second largest element.")
