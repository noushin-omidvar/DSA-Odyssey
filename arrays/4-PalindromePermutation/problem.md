# Is Permutation of Palindrome

**Problem:** Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.

## Example

Input: "tact coa"
Output: True (Permutations: "taco cat", "atco cta", etc.)

Input: "hello"
Output: False

## Constraints

- Are the input strings case-sensitive? (Assuming yes for this example.)
- Can the input string contain spaces? (Assuming yes for this example.)

## Approach

To solve this problem, we can count the frequency of each character in the string. For a string to be a permutation of a palindrome, it should have at most one character with an odd frequency (all other characters should have even frequencies).

## Pseudocode

function is_permutation_of_palindrome(s):
    char_count = [0] * 128 # Assuming ASCII characters
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


## Complexity Analysis

- Time Complexity: O(n)
- Space Complexity: O(1) (constant space for the character frequency array)

## Notes

- The function handles spaces by skipping them during character frequency counting.
- The string can be any combination of letters, numbers, and special characters.

## Related Problems

- [Determine if a string has all unique characters](https://github.com/noushin-omidvar/DSA-Odyssey/tree/main/arrays/0-IsUnique).
- [Determine if two strings are permutations of each other](https://github.com/noushin-omidvar/DSA-Odyssey/tree/main/arrays/1-CheckPermutation).
- Check if a string is a palindrome.


