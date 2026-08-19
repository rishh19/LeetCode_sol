class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp={}

        for ch in s:
            #store chars in map
            mp[ch] =mp.get(ch,0)+1

        #check for unique count
        for i in range(len(s)):
             if mp[s[i]] == 1:
                return i
        return -1