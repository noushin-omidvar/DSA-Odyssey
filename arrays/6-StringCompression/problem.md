# String Compression

**Problem:** Implement a method to perform basic string compression using the counts of repeated characters. For example, the string "aabcccccaaa" would become "a2b1c5a3". If the "compressed" string would not become smaller than the original string, your method should return the original string.

## Example

Input: "aabcccccaaa"
Output: "a2b1c5a3"

Input: "abcdef"
Output: "abcdef"

## Constraints

- Are the input strings case-sensitive? (Assuming yes for this example.)

## Approach

To solve this problem, we can iterate through the characters of the string while keeping track of the current character and its count. If the next character is different, we add the current character and its count to the compressed string. After processing all characters, we compare the length of the compressed string with the original string and return the shorter of the two.

## Pseudocode
```
function string_compression(s):
    compressed = ''
    count = 0

    for i in range(len(s)):
        count += 1
        
        if i + 1 >= len(s) or s[i] != s[i + 1]:
            compressed += s[i] +str(count)
            count = 0

    return s if len(compressed) >= len(s) else compressed
```


## Complexity Analysis

- Time Complexity: O(n)
- Space Complexity: O(n) (for the compressed string)

## Notes

- The function assumes that the characters are from a standard character set (e.g., ASCII).

## Related Problems

- [Determine if a string has all unique characters](https://github.com/noushin-omidvar/DSA-Odyssey/tree/main/arrays/0-IsUnique).
- [Determine if two strings are permutations of each other](https://github.com/noushin-omidvar/DSA-Odyssey/tree/main/arrays/1-CheckPermutation).
- Check if a string is a palindrome.
