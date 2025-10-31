class Solution(object):
    def romanToInt(self, s):
        n=len(s)
        dici={'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        ans=0
        for i in range(n):
            if i<n-1 and dici[s[i]]< dici[s[i+1]]:
                ans-=dici[s[i]]
                #print(ans)
            else:
                ans+=dici[s[i]]
                #print(ans)
        return ans
        