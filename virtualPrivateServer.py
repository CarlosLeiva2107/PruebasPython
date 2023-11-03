def virtualPrivateServer(process, m):
    max_sums = []
    max_value = 0
    for i in range(len(process)):
        sum_numbers = 0
        for j in range(m):  
            if i+j < len(process):
                sum_numbers += process[i+j]
        max_sums.append(sum_numbers)
    max_value = max(max_sums)
    for i in range(len(max_sums)):
        if max_sums[i] == max_value:
            for j in range(m):
                del process[i]
    print(sum(process))
    
   


virtualPrivateServer([4,6,10,8,2,1],3)
