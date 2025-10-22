class Solution(object):
    def lengthOfLastWord(self, s):
        substring=s.split()[-1]
        return len(substring)
        