class Solution(object):
    def maxProfit(self, prices):
        n=prices[0]
        ans=0
        for i in range(1,len(prices)):
            ans=max(ans,(prices[i]-n))
            n=min(n,prices[i])
        return ans

        