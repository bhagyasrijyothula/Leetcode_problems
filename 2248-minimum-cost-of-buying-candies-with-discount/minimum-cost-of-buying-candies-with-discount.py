class Solution(object):
    def minimumCost(self, cost):
        cost.sort()
        took=0
        ans=0
        for i in range(len(cost)-1,-1,-1):
            if took==2:
                took=0
            else:
                ans+=cost[i]
                took+=1
        return ans
        