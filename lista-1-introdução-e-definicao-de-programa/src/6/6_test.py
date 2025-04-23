def test_yes_if_sum_thirds_exceeds_seconds():
    test_cases = [
        ("58 41 78 3 25 9", "yes"),
        ("10 20 30 40 50 60", "no"),
        ("5 15 25 35", "no"),
        ("12, 1", "no"),
        ("1 2 3", "yes"),
        ("7 14 21 28", "no"),
        ("0 0 0 0", "no"),
        ("9 18 27 36", "no"),
        ("11 22 33 44", "no"),
        ("3 6 9 1", "yes")
    ]
    
    for i, (input_list, expected) in enumerate(test_cases):
        result = yes_if_sum_thirds_exceeds_seconds(input_list)
        print(f"Test case {i+1}: input='{input_list}', expected={expected}, got={result}")