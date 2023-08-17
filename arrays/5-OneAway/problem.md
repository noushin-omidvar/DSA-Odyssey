# One Away

**Problem:** There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away from each other.

## Example

Input: "pale", "ple"
Output: True

Input: "pales", "pale"
Output: True

Input: "pale", "bale"
Output: True

Input: "pale", "bake"
Output: False

## Constraints

- Are the input strings case-sensitive? (Assuming yes for this example.)
- Can the input strings contain spaces? (Assuming yes for this example.)

## Approach

To solve this problem, we can perform the following checks:
1. If the lengths of the strings differ by more than one, they can't be one edit away.
2. Find the first difference and check if the rest is the same 

## Pseudocode

function isOneEditAway(s1, s2):
    if len(s1) > len(s2):
        return isOneEditAway(s2, s1)

    if len(s2) - len(s1) > 1:
        return False

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if len(s1) == len(s2):
                return s1[i + 1:] == s2[i + 1:]
            else:
                return s1[i:] == s2[i + 1:]

    return len(s1) + 1 == len(s2)


## Complexity Analysis

- Time Complexity: O(n)
- Space Complexity: O(1)

## Notes

- This approach assumes that the characters are from a standard character set (e.g., ASCII).

## Related Problems

- [Determine if a string has all unique characters](https://github.com/noushin-omidvar/DSA-Odyssey/tree/main/arrays/0-IsUnique).
- [Determine if two strings are permutations of each other](https://github.com/noushin-omidvar/DSA-Odyssey/tree/main/arrays/1-CheckPermutation).
- Check if a string is a palindrome.
