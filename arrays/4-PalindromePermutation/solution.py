def is_permutation_of_palindrome(s):
    char_count = [0] * 128  # Assuming ASCII characters
    odd_count = 0

    for char in s:
        if char == ' ':
            continue
        char_count[ord(char)] += 1
        if char_count[ord(char)] % 2 == 0:
            odd_count -= 1
        else:
            odd_count += 1
    return odd_count <= 1


# Test cases
input1 = "tact coa"
print(is_permutation_of_palindrome(input1))  # Output: True

input2 = "hello"
print(is_permutation_of_palindrome(input2))  # Output: False
