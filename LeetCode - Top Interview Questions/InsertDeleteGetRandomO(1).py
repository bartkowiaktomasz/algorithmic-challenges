import random

class RandomizedSet:

    def __init__(self):
        self.nums, self.idxs = [], {}

    def insert(self, val: int) -> bool:
        if val in self.idxs:
            return False
        else:
            self.nums.append(val)
            self.idxs[val] = len(self.nums) - 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.idxs:
            return False
        else:
            pos = self.idxs[val]
            last = self.nums[-1]
            self.nums[pos] = last
            self.idxs[last] = pos
            self.nums.pop()
            del self.idxs[val]
            return True


    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()