class Solution:
    def romanToInt(self, s: str) -> int:
        ht = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans=0
        for i in range(len(s)-1):
            if ht[s[i]] < ht[s[i+1]]:
                ans = ans - ht[s[i]]
            else:   
                ans = ans + ht[s[i]]
        return ans + ht[s[-1]]
