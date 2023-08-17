def urlify(s, true_length):
    s = list(s)  # Convert the input string to a list of characters
    # Count the spaces within the true length of the string
    space_count = s[:true_length].count(' ')
    # Calculate the new length after URL encoding
    index = true_length + space_count * 2

    # Iterate through the characters in reverse order
    for i in range(true_length - 1, -1, -1):
        if s[i] == ' ':
            # Replace a space with '%20' and adjust the index for the next character
            s[index - 1] = '0'
            s[index - 2] = '2'
            s[index - 3] = '%'
            index -= 3
        else:
            # Copy non-space character to its new position and adjust the index
            s[index - 1] = s[i]
            index -= 1

    # Convert the modified character list back to a string and return
    return ''.join(s)


# Test cases
input1 = "Mr John Smith    "
length1 = 13
print(urlify(input1, length1))  # Output: "Mr%20John%20Smith"

input2 = "Hello World  "
length2 = 11
print(urlify(input2, length2))  # Output: "Hello%20World"
