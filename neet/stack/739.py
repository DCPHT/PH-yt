from typing import List


# Solution 1: Brute force
# Time complexity: O(n^2)
# Space complexity: O(n)
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    for i in range(len(temperatures)):
        for j in range(i, len(temperatures)):
            if temperatures[j] > temperatures[i]:
                res[i] = j - i
                break

    return res


# Solution 2: Use a stack to store the numbers
# Time complexity: O(n)
# Space complexity: O(n)
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    stack = []
    res = [0] * len(temperatures)
    for i, temperature in enumerate(temperatures):
        while stack and temperature > stack[-1][0]:
            val, idx = stack.pop()
            res[idx] = i - idx
        stack.append((temperature, i))
    return res
