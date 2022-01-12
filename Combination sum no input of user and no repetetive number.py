def combinations_to_target_number(numbers, target_number, combinations=[]):
    # add every number in combinations to get total
    total_sum = sum(combinations)
    # check if the combinations sum is equals to target_number
    if total_sum  == target_number:
        print(combinations)
    # 
    else:
        for i in range(len(numbers)):
            n = numbers[i]
            remaining = numbers[i + 1:]
            combinations_to_target_number(remaining, target_number, combinations + [n])

numbers = [1,2,3,4,5,6,7,8,9,10]
target_number = 10
combinations_to_target_number(numbers, target_number)