class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]

        for t in tokens:
            if t not in "+-*/":
                st.append(int(t))
            else:
                first=st.pop()
                second=st.pop()

                if t=="+":
                    res=second+first
                elif t=="-":
                    res=second-first
                elif t=="*":
                    res=second * first
                else:
                    res=int(second/first)

                st.append(res)
        return st[-1]