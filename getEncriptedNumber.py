def getEncriptedNumber(numbers):
    sum_numbers = numbers
    
    while len(sum_numbers) != 2:
        temp_list = []
        for i,n in enumerate(sum_numbers):
            if i + 1 < len(sum_numbers):
                temp_list.append((n + sum_numbers[i+1]) % 10)
        sum_numbers = temp_list

    print(str(sum_numbers[0]) + str(sum_numbers[1]))
    return str(sum_numbers[0]) + str(sum_numbers[1])

getEncriptedNumber([4,5])