class Solution(object):
    def distributeCandies(self, candyType):
        numunique= len(set(candyType))
        max_allowd=len(candyType)//2
        return min(numunique,max_allowd)
        