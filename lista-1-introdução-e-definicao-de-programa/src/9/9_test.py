def test_count_elements():
    test_cases = [
        ("apple, banana, apple, orange, banana", "apple:2, banana:2, orange:1"),
        ("cat, dog, cat, bird", "cat:2, dog:1, bird:1"),
        ("red, blue, green, red", "red:2, blue:1, green:1"),
        ("one, two, three", "one:1, two:1, three:1"),
        ("a, b, a", "a:2, b:1"),
        ("x, y, z", "x:1, y:1, z:1"),
        ("hello, world", "hello:1, world:1"),
        ("test, test", "test:2"),
        ("python, java", "python:1, java:1"),
        ("apple", "apple:1")
    ]
    
    for i, (input_elements, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: input='{input_elements}', expected='{expected}', got=", end="")
        count_elements(input_elements)