def is_unique(s):
    char_set = set()
    for char in s:
        if char in char_set:
            return False
        char_set.add(char)
    return True

# Test cases
input1 = "abcdefg"
print(is_unique(input1))  # Output: True

input2 = "hello"
print(is_unique(input2))  # Output: False
