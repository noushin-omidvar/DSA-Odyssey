# URLify

**Problem:** Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the true length of the string.

## Example

Input: "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"

Input: "Hello World  ", 11
Output: "Hello%20World"

## Constraints

- Can we assume that the string has at least one space? (Assuming yes for this example.)
- What if there are multiple spaces in a row? (Assuming they are replaced with a single '%20' for this example.)
- Are trailing spaces significant? (Assuming no for this example.)

## Approach

To solve this problem, we can perform the following steps:
1. Iterate through the string from the end and copy characters to their new positions, replacing spaces with '%20'.
2. Keep track of two pointers: one for the current position in the original string and another for the current position in the new string.

## Pseudocode

function urlify(s, true_length):
    s = list(s) # Convert string to a list of characters
    space_count = s.count(' ')
    new_index = true_length + space_count * 2

    for i in range(true_length - 1, -1, -1):
        if s[i] == ' ':
            s[new_index - 1] = '0'
            s[new_index - 2] = '2'
            s[new_index - 3] = '%'
            new_index -= 3
        else:
            s[new_index - 1] = s[i]
            new_index -= 1

    return ''.join(s)



## Complexity Analysis

- Time Complexity: O(n)
- Space Complexity: O(1) (in-place transformation)

## Notes

- In Python, strings are immutable, so we convert the string to a list of characters to perform the in-place transformation.
- If we are allowed to use additional space, we can create a new string and replace spaces without the in-place constraint.

## Related Problems

- [Determine if a string has all unique characters](https://github.com/noushin-omidvar/DSA-Odyssey/tree/main/arrays/0-IsUnique).
- [Determine if two strings are permutations of each other](https://github.com/noushin-omidvar/DSA-Odyssey/tree/main/arrays/1-CheckPermutation).
- Check if a string is a palindrome.
