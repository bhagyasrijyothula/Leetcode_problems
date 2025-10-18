class Solution(object):
    def isPalindrome(self, x):
        n=0
        sum=x
        while sum>0:
            rev=sum%10
            n=n*10+rev
            sum//=10
        if x==n:
            return True
        else:
            return False
        