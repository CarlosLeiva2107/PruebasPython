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
    max_index = max_sums.index(max_value)

    for j in range(m):
        del process[max_index]
        
    print(sum(process))
    
   


virtualPrivateServer([10,4,8,1],2)
