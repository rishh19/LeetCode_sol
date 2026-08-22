class Solution:
    def calPoints(self, ops: List[str]) -> int:
        st=[]

        for op in ops:
            if op=="C":
                st.pop()
            elif op=="D":
                score=st[-1]
                st.append(score*2)
            elif op=="+":
                last=st[-1]
                sec_last=st[-2]
                st.append(last+sec_last)
            else:
                score=int(op)
                st.append(score)
        return sum(st)