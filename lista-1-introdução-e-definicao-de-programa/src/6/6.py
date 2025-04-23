def yes_if_sum_thirds_exceeds_seconds(list):
    if int(sum_each_third_integer(list)) > int(sum_each_second_integer(list)):
        return 'yes'
    else:
        return 'no'