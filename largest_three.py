arr = [10, 20, 20, 4, 45, 99, 99]

unique_arr = list(set(arr))


if len(unique_arr) < 3:
    print("Less than 3 distinct elements in the array.") 
else:
    unique_arr.sort(reverse=True)

    print(" 3 largest distinct elements:", unique_arr[:3])
