# Check permutation: Given two strings, write a method to decide if one is a permutation of the other.


# Solution 1: Sort the strings and compare them
# Time complexity: O(nlogn)
# Space complexity: O(n)
def check_permutation_1(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = sorted(s1)
    s2 = sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


# Solution 2:
# Time complexity: O(n)
# Space complexity: O(n)
def check_permutation_2(s1, s2):
    if len(s1) != len(s2):
        return False
    mapping = {}
    for c in s1:
        if c not in mapping:
            mapping[c] = 0
        mapping[c] += 1
    for c in s2:
        if c not in mapping:
            return False
        mapping[c] -= 1
        if mapping[c] < 0:
            return False
    return True


res = check_permutation_2("abc", "cbA")
print(res)
