def string_compression(s):

    counter = 0
    compressed = ''

    for i in range(len(s)):
        counter += 1
        if i + 1 >= len(s) or s[i] != s[i+1]:
            compressed += s[i] + str(counter)
            counter = 0

    return s if len(compressed) >= len(s) else compressed


# Test cases
input1 = "aabcccccaaa"
print(compress_string(input1))  # Output: "a2b1c5a3"

input2 = "abcdef"
print(compress_string(input2))  # Output: "abcdef"
