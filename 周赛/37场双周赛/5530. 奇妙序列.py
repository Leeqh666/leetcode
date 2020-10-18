class Fancy:

    def __init__(self):
        self.mul = 1
        self.add = 0
        self.my_list = []
        self.re = []
        self.re_m = []


    def append(self, val: int) -> None:
        self.my_list.append((val - self.add) / self.mul)

    def addAll(self, inc: int) -> None:
        self.add += inc

    def multAll(self, m: int) -> None:
        self.add *= m
        self.mul *= m

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.my_list):
            return -1
        return (self.my_list[idx] * self.mul + self.add) % (1e9 + 7)



# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)