class Solution:
    def removeDuplicates(self, s: str) -> str:
        #empty stack
        st=[]

        for ch in s:
            #if stack is is not empty and previous (recent) ch is same
            if st and st[-1]==ch:
                st.pop()
            else:
                st.append(ch)
        return "".join(st)