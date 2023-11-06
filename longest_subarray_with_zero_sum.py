def longest_subarray_with_zero_sum(arr):
    current_sum = 0
    longest_subarray = []
    max_number = 1

    for n,i in enumerate(arr):
        current_sum += i
        for j in range(n+1,len(arr)):
            current_sum += arr[j]
            max_number += 1
            if current_sum == 0:
                longest_subarray.append(max_number)
        max_number = 1
        current_sum = 0


    print(max(longest_subarray))
    return max(longest_subarray)

longest_subarray_with_zero_sum([15, -2, 2, -8, 1, 7, 10, 23])