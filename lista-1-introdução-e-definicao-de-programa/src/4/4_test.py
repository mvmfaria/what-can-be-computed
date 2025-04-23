def test_sum_each_second_integer():
    test_cases = [
        ("58 41 78 3 25 9", 53),
        ("10 20 30 40 50 60", 120),
        ("5 15 25 35", 50),
        ("12, 1", 1),
        ("1 2 3", 2),
        ("7 14 21 28", 42),
        ("0 0 0 0", 0),
        ("9 18 27 36", 54),
        ("11 22 33 44", 66),
        ("3 6 9 12", 18)
    ]
    
    for i, (input_list, expected) in enumerate(test_cases):
        result = sum_each_second_integer(input_list)
        print(f"Test case {i+1}: input='{input_list}', expected={expected}, got={result}")