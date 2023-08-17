def isOneEditAway(s1, s2):

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


# Test cases
input1 = "pale"
input2 = "ple"
print(isOneEditAway(input1, input2))  # Output: True

input3 = "pales"
input4 = "pale"
print(isOneEditAway(input3, input4))  # Output: True

input5 = "pale"
input6 = "bale"
print(isOneEditAway(input5, input6))  # Output: True

input7 = "pale"
input8 = "bake"
print(isOneEditAway(input7, input8))  # Output: False
