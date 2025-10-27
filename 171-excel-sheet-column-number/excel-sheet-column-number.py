class Solution(object):
    def titleToNumber(self, columnTitle):
        res=0
        for char in columnTitle:
            res=res* 26 +(ord(char)- ord('A')+1)
        return res
        