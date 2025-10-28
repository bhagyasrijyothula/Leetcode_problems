import re
from collections import Counter
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        paragraph = re.sub(r'[^a-z]',' ', paragraph.lower())
        words= paragraph.split()
        banned_set=set(banned)
        counts= Counter(word for word in words if word not in banned_set)
        return counts.most_common(1)[0][0]
        