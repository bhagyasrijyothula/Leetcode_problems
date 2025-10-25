class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix=strs[0]
        prefix_len=len(prefix)
        for s in strs[1:]:
            while prefix !=s[0:prefix_len]:
                prefix_len-=1
                if prefix_len==0:
                    return ""
                prefix= prefix[0:prefix_len]
        return prefix
        