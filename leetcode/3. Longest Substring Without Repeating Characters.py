class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        maxLen=0
        sett=set()
        left=0
        for right in range(n):
            if s[right] not in sett:
                sett.add(s[right])
                maxLen=max(maxLen,right-left+1)
            else:
                while s[right] in sett:
                    sett.remove(s[left])
                    left+=1
                sett.add(s[right])
        return maxLen

        
