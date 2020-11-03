class Solution:
    def maxPower(self, s: str) -> int:
        mx = 1
        i = 0
        j = 1
        curr = 1
        while j < len(s):
            if s[i] != s[j]:
                i +=1
                j +=1
            while j < len(s) and s[i] == s[j]:
                i += 1
                j += 1
                curr += 1
            if curr > mx:
                mx = curr
                curr = 1
            else:
                curr = 1
        return mx
