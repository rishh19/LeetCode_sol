class MinStack:

    def __init__(self):
        self.st=[]
        self.min_st=[]

    def push(self, val: int) -> None:
        self.st.append(val)

        if len(self.min_st)==0:
            self.min_st.append(val)
        else:
            current_min = self.min_st[-1]

            if val < current_min:
                self.min_st.append(val)
            else:
                self.min_st.append(current_min)
        

    def pop(self) -> None:
        self.st.pop()
        self.min_st.pop()
        

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.min_st[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()