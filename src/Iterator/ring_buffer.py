class MyRingBuffer:
    def __init__(self, size):
        self.size = size
        self.taken = 0
        self.head = 0  # the current write position
        self.tail = 0  # the current read position
        self.list = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.taken == 0:
            raise StopIteration

        result = self.list[self.tail]
        self.tail = (self.tail + 1) % self.size
        self.taken -= 1

        return result

    def add(self, data) -> None:
        if self.taken >= self.size:
            raise IndexError("Overflow")

        if len(self.list) <= self.head:
            self.list.append(data)
        else:
            self.list[self.head] = data
        self.head = (self.head + 1) % self.size
        self.taken += 1

