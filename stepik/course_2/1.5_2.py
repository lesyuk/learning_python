class Buffer:
    def __init__(self):
        self.list = []
        self.sum = 0

    def add(self, *a):
        self.list += a
        while len(self.list) >= 5:
            for i in range(5):
                self.sum += self.list[i]
            del self.list[:5]
            print(self.sum)
            self.sum = 0

    def get_current_part(self):
        return self.list

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # [1, 2, 3]
buf.add(4, 5, 6) # 15
buf.get_current_part() # [6]
buf.add(7, 8)
buf.add(9)
buf.get_current_part() # [6, 7, 8, 9]
buf.add(10) # 40
buf.get_current_part() # []
buf.add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11) # 15, 40
buf.get_current_part() # [11]