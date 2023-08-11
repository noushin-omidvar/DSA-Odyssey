# Check Permutation

**Problem:** Given two strings, write a method to decide if one is a permutation of the other.

## Example

Input: "abc", "bca"
Output: True

Input: "hello", "world"
Output: False

## Constraints

- Are the input strings case-sensitive? (Assuming yes for this example.)
- Can the input strings contain spaces? (Assuming yes for this example.)
- What if one string is longer than the other? (Assuming different lengths are not considered permutations for this example.)

## Approach

To solve this problem, we can check if the two strings have the same characters with the same frequency. We can create character frequency arrays (or dictionaries) for both strings and compare them. If the character frequencies match, the strings are permutations of each other.

## Pseudocode

function is_permutation(str1, str2):
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



## Complexity Analysis

- Time Complexity: O(n)
- Space Complexity: O(1) (constant space for the character frequency array)

## Notes

- If the input strings can contain characters from a larger character set (e.g., Unicode), the space complexity of the algorithm might increase.

## Related Problems

- [Determine if a string has all unique characters](https://github.com/noushin-omidvar/DSA-Odyssey/tree/main/arrays/0-IsUnique).
- Check if a string is a palindrome.
- Replace all spaces in a string with '%20'.
