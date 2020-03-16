class ExtendedStack(list):
    def sum(self):
        self.
    def sub(self):
        a = list[-1]
        list.pop()
        b = list[-1]
        list.pop()
        list.append(a - b)

    def mul(self):
        a = list[-1]
        list.pop()
        b = list[-1]
        list.pop()
        list.append(a * b)

    def div(self):
        a = list[-1]
        list.pop()
        b = list[-1]
        list.pop()
        list.append(a // b)

def test():
    ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
    ex_stack.div()
    assert ex_stack.pop() == 2
    ex_stack.sub()
    assert ex_stack.pop() == 6
    ex_stack.sum()
    assert ex_stack.pop() == 7
    ex_stack.mul()
    assert ex_stack.pop() == 2
    assert len(ex_stack) == 0