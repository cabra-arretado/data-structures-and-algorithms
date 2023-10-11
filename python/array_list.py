from array import array


class ArrayList:
    capacity = None
    size = None
    array = None

    def __init__(self, capacity=5):
        self.capacity = capacity
        # For the sake of using arra.array, we'll use -1 as a sentinel value
        self.array = array('i', [-1] * self.capacity)
        self.size = 0

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if index >= self.size:
            raise IndexError
        return self.array[index]

    def append(self, val):
        if self.size == self.capacity:
            self.capacity *= 2
            new_array = [None] * self.capacity
            new_array[:self.size] = self.array
            self.array = new_array
            self.array[self.size] = val
            self.size += 1
            return
        self.array[self.size] = val
        self.size += 1

    def prepend(self, val):
        if self.size == self.capacity:
            self.capacity *= 2
            new_array = [None] * self.capacity
            new_array[:self.size] = self.array[1:self.size + 1]
        else:
            array[1:self.size + 1] = array[:self.size]
        self.size += 1
        new_array[0] = val

    def insert_at():
        pass

    def remove_at():
        pass

    def remove():
        pass

    def get():
        pass
