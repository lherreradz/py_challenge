# To resolve this, I use a list that will act as an array and that contain a flags
# to indicate that the number n in the position p n*2=p is contained in the received list
# for negative numbers uses the position (n*2)+1=p

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
    