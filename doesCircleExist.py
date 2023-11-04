def doesCircleExist(commands):
    result_array = []
    for command in commands:
        possible_result = ''
        command = command.replace('G', '')
        if command == 'R' or command == 'L':
            possible_result = 'YES'
        else:
            possible_result = 'NO'
        for n,c in enumerate(command):
            if n > 0:
                if c == 'R' and command[n-1] == 'R' or c =='L' and command[n-1] == 'L':
                    possible_result = 'YES'
                else:
                    possible_result = 'NO'
        result_array.append(possible_result)
    return result_array

print(doesCircleExist(['G','L','GRGL','GRGRGRGL','GR','GRGRGLGRGRGR']))