def test_reverse_string():
    test_cases = [
        ("hello", "olleh"),
        ("world", "dlrow"),
        ("python", "nohtyp"),
        ("test", "tset"),
        ("example", "elpmaxe"),
        ("reverse", "esrever"),
        ("string", "gnirts"),
        ("function", "noitcnuf"),
        ("code", "edoc"),
        ("testcase", "esactset")
    ]
    
    for i, (input_string, expected) in enumerate(test_cases):
        result = reverse_string(input_string)
        print(f"Test case {i+1}: input='{input_string}', expected='{expected}', got='{result}'")