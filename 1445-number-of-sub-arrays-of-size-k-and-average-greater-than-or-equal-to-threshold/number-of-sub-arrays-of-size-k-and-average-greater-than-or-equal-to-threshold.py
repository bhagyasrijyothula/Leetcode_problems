class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        ans=0
        l=0
        temp=0
        n=len(arr)
        for r in range(n):
            temp+=arr[r]
            if r-l==k:
                temp-=arr[l]
                l+=1
            if r-l+1==k:
                if (temp/k)>=threshold:
                    ans+=1
        return ans
                