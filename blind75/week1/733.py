from typing import List


# Solution
# Time complexity: O(m * n)
# Space complexity: O(m * n)
def floodFill(
    self, image: List[List[int]], sr: int, sc: int, color: int
) -> List[List[int]]:
    # 2 2 2
    # 2 2 0
    # 2 0 1
    nrows, ncols = len(image), len(image[0])

    def dfs(i, j, starting):
        if i < 0 or j < 0 or i >= nrows or j >= ncols:
            return
        if image[i][j] != starting:
            return
        if starting == color:
            return
        image[i][j] = color
        dfs(i - 1, j, starting)
        dfs(i + 1, j, starting)
        dfs(i, j - 1, starting)
        dfs(i, j + 1, starting)

    dfs(sr, sc, image[sr][sc])
    return image
