class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #for track s & p
        i=0 #string pointer
        j=0 #pattern pointer
        star=-1 #last star position
        match=0 # how much of string '*' has consumed

        while i < len(s):
            # Current characters match OR pattern has '?'
            # → both characters are handled, so move both pointers
            if j < len(p) and (p[j]==s[i] or p[j]=='?'):
                i+=1
                j+=1
            # We found '*'
            # → don't decide its length now
            # → remember it so we can come back if needed
            elif j<len(p) and p[j]=='*':
                star=j
                match=i
                j+=1
            # Current characters don't match,
            # BUT we have a '*' saved earlier
            # → let '*' consume ONE MORE character
            # → then try matching again
            elif star!= -1:
                j=star+1
                match+=1
                i=match
            else:
                return False
        
        while j<len(p) and p[j]=='*':
            j+=1
        return j==len(p)
