def test_eh_palindromo():
    test_cases = [
        ("A man a plan a canal Panama", "yes"),
        ("racecar", "yes"),
        ("hello", "no"),
        ("Was it a car or a cat I saw", "yes"),
        ("No lemon no melon", "yes"),
        ("Python", "no"),
        ("Madam", "yes"),
        ("Step on no pets", "yes"),
        ("Not a palindrome", "no"),
        ("Able was I saw Elba", "yes")
        ]

    for i, (input_text, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: input='{input_text}', expected='{expected}', got=", end="")
        eh_palindromo(input_text)