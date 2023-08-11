# Is Unique

**Problem:** Given a string, determine if it has all unique characters. That is, check if no characters in the string appear more than once.

## Example

Input: "abcdefg"
Output: True

Input: "hello"
Output: False

## Constraints

- Can the input string contain only lowercase letters? (Assuming yes for this example.)
- What is the maximum length of the input string?
- Is the string's length limited? (Assuming no for this example.)

## Approach

To solve this problem, we can use a data structure like a set to keep track of characters we've seen. As we iterate through the string, if we encounter a character that is already in the set, we can conclude that the string does not have all unique characters. Otherwise, we add the character to the set. This approach has a time complexity of O(n), where n is the length of the input string.

## Pseudocode

function isUnique(str):
    charSet = set()
    
    for char in str:
        if char in charSet:
            return False
        charSet.add(char)

    return True


## Complexity Analysis

- Time Complexity: O(n)
- Space Complexity: O(min(n, m)), where m is the size of the character set (assuming ASCII characters, m = 128).

## Notes

- If the input string can contain characters from a larger character set (e.g., Unicode), the space complexity of the algorithm might increase.

## Related Problems

- Determine if two strings are permutations of each other.
- Check if a string is a palindrome.
- Replace all spaces in a string with '%20'.



