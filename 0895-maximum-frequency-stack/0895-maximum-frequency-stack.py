class FreqStack:

    def __init__(self):
        self.cnt = {}                  # val -> current frequency
        self.maxCnt = 0                # maximum frequency of any value
        self.stk = {}                  # frequency -> stack of values

    def push(self, val: int) -> None:
        valCnt = 1 + self.cnt.get(val, 0)   # increase frequency of val
        self.cnt[val] = valCnt              # store updated frequency

        if valCnt > self.maxCnt:             # if val has highest frequency
            self.maxCnt = valCnt             # update maximum frequency
            self.stk[valCnt] = []            # create stack for this frequency

        self.stk[valCnt].append(val)        # add val to its frequency stack

    def pop(self) -> int:
        res = self.stk[self.maxCnt].pop()   # remove most recent value with max frequency
        self.cnt[res] -= 1                  # decrease its frequency

        if not self.stk[self.maxCnt]:       # if max-frequency stack becomes empty
            self.maxCnt -= 1                # decrease maximum frequency

        return res                          # return the removed value
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()