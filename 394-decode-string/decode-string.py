class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        current=""
        n=0

        for ch in s:
            if ch.isdigit():
                n=n*10 + int(ch)  # build the number

            elif ch == "[":
                st.append((current,n))  # save previous string and repeat number
                current=""              # start a new string inside brackets
                n=0                      # reset number

            elif ch == "]":
                prev_str, repeat_number = st.pop()  # get previous string and repeat number
                current = prev_str + current * repeat_number  # repeat current and combine

            else:
                current+=ch  # add the current character to the string

        return current  # return the decoded string