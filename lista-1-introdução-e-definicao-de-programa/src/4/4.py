def sum_each_second_integer(list):
    current_number = ''
    counter = 0
    sum = 0
    for n in list:
        if n  != ' ':
            current_number += n
        else:
            if counter == 1:
                sum += int(current_number)
                counter = 0
            else:
                counter += 1
            current_number = ''
    if counter == 1:
        sum += int(current_number)
    return sum