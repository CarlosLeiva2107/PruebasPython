def largest_contiguous_sum(arr):
    max_sum = 0
    actual_max_sum = 0
    for i in arr:
        actual_max_sum += i
        if actual_max_sum < 0:
            actual_max_sum = 0
        if actual_max_sum > max_sum:
            max_sum = actual_max_sum

    #Negative case, add max value among all
    if max_sum == 0:
        max_sum = sorted(arr)[-1]

    print(max_sum)
    return max_sum
largest_contiguous_sum([-2,1,-3,4,-1,2,1,-2,8,-5,4])