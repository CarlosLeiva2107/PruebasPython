def longest_consective_sunsequence(arr):
    consecutive_numbers = 1

    for i in arr:
        index = 0
        actual_number = i
        consecutive_numbers_actual = 1
        while index < len(arr):
            if actual_number + 1 in arr:
                consecutive_numbers_actual += 1
            else:
                break
            actual_number += 1
            index += 1
        if consecutive_numbers_actual > consecutive_numbers:
            consecutive_numbers = consecutive_numbers_actual
    print(consecutive_numbers)

longest_consective_sunsequence([1, 9, 3, 10, 4, 20, 2,11,13,100])