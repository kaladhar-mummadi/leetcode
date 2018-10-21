import sys
class MinStack:
    def __init__(self):
        self.values = []
        self.min_val = sys.maxsize
    def push(self, x):
        self.values.append(x)
        if self.min_val > x:
            self.min_val = x
    def pop(self):
        val = self.values.pop()
        if self.min_val == val:
            if len(self.values) > 0:
                self.min_val = min(self.values)
            else:
                self.min_val = sys.maxsize
        return val
    def top(self):
        return self.values[-1]

    def getMin(self):
        return self.min_val