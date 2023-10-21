# Solution 1:
# Time complexity: O(n^2)
# Space complexity: O(1)
def maxProfitN2(prices) -> int:
    """
    :type prices: List[int]
    :rtype: int
    """
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            max_profit = max(max_profit, prices[j] - prices[i])
    return max_profit


# Solution 2:
# Time complexity: O(n)
# Space complexity: O(1)
def maxProfit(prices) -> int:
    """
    :type prices: List[int]
    :rtype: int
    """
    res = 0
    should_buy = prices[0]
    for price in prices:
        if price < should_buy:
            should_buy = price
        else:
            cur_profit = price - should_buy
            res = max(res, cur_profit)

    return res
