def get_pairs (number_list, expected_sum):
    list_size = (max(number_list)*2)+3 if max(number_list) > expected_sum else (expected_sum*2)+3
    numbers = [False] * list_size
    pairs = []
    for number in number_list:
        difference = expected_sum-number
        if numbers[get_position_in_list(difference)] == True: 
            numbers[get_position_in_list(difference)] = False
            pairs.append([difference, number])
        else:
            numbers[get_position_in_list(number)] = True    
    return pairs
            
def get_position_in_list(number):
    return number * 2 if number >= 0 else (number * 2)+1
    