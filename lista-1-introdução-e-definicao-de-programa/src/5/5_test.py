def test_sum_each_third_integer():
    test_cases = [
        ("10 20 30 40 50 60", 90),
        ("1 2 3 4 5 6 7 8 9", 18),
        ("100 200 300 400 500", 300),
        ("5 10 15 20 25 30", 45),
        ("3 6 9 12 15 18", 27),
        ("0 1 2 3 4 5", 7),
        ("7 14 21 28 35 42", 63),
        ("11 22 33 44 55", 33),
        ("8 16 24 32 40", 24),
        ("2 4 6 8 10 12", 18)
    ]
    for i, (input_list, expected) in enumerate(test_cases):
        result = sum_each_third_integer(input_list)
        print(f"Test case {i+1}: input='{input_list}', expected={expected}, got={result}")