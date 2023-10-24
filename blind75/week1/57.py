from typing import List

# Solution
# Time complexity: O(n)
# Space complexity: O(n)


def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    res = []
    for interval in intervals:
        if interval[0] > newInterval[1]:
            res.append(newInterval)
            newInterval = interval
        elif interval[1] >= newInterval[0]:
            newInterval[0] = min(interval[0], newInterval[0])
            newInterval[1] = max(interval[1], newInterval[1])
        else:
            res.append(interval)
    res.append(newInterval)
    return res
