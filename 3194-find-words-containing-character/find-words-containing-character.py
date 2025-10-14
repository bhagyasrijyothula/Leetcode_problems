class Solution(object):
    def findWordsContaining(self, words, x):
        n=len(words)
        temp=[]
        for i, word in enumerate(words):
            if x in words[i]:
                temp.append(i)
        return temp
        