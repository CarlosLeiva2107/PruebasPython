def howManySwaps(arr, n):
    swaps = 0

    #First compare items and get the posible indexes you can make swap
    for i in range(n):
        for j in range(i, n):
            temp_swap = []
            if arr[i] > arr[j]:
                temp_swap.append([i,arr[i],j,arr[j]])
        
        #Find the minimum value of all the possible swaps
        minimum = 0
        for k in temp_swap:
            if minimum == 0:
                minimum = k[3]
            if minimum > k[3]:
                minimum = k[3]
        #Finally, make the correct swap
        for c in temp_swap:
            if c[3] == minimum:
                arr[c[0]], arr[c[2]] = arr[c[2]], arr[c[0]]
                swaps += 1
    print(swaps)
    return swaps

howManySwaps([7,2,1],3)