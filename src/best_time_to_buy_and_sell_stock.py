class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        l = 0
        r = 1
        while (r < len(prices)):
            currProf = prices[r] - prices[l]

            if currProf < 0:
                l = r
                r += 1
                continue

            maxProf = max(maxProf, currProf)
            r += 1

        return maxProf