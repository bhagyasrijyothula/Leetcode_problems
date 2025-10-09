class Solution(object):
    from collections import Counter
    def commonChars(self, words):
        common_ch=Counter(words[0])
        for ch in words[1:]:
            common_ch&=Counter(ch)
        return list(common_ch.elements())
        