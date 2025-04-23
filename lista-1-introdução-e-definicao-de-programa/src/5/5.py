def sum_each_third_integer(list):
    current_number = ''
    counter = 0
    sum = 0
    for n in list:
        if n != ' ':
            current_number += n
        else:
            if counter == 2:
                sum += int(current_number)
                counter = 0
            else:
                counter += 1
            current_number = ''
    if counter == 2:
        sum += int(current_number)
    return sum