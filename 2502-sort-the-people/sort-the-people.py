class Solution(object):
    def sortPeople(self, names, heights):
        return [name for i, name in sorted(zip(heights, names), reverse = True)]
        