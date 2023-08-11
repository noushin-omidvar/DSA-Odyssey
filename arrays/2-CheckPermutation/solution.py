def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    
    char_count = [0] * 128  # Assuming ASCII characters
    
    for char in str1:
        char_count[ord(char)] += 1
    
    for char in str2:
        char_count[ord(char)] -= 1
        if char_count[ord(char)] < 0:
            return False
    
    return True

# Test cases
input1 = "abc"
input2 = "bca"
print(is_permutation(input1, input2))  # Output: True

input3 = "hello"
input4 = "world"
print(is_permutation(input3, input4))  # Output: False
