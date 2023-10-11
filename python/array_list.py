# from array import array


class ArrayList:
    capacity = 5
    size = 0
    # for the sake of simplicity, we will use python's list, but in reality, we should use an array.array instance
    array = [None] * capacity
    def __init__(self, capacity = 5):
        self.array = []
        self.size = 0
        self.capacity = capacity

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
            new_array[0:self.size] = self.array
            self.array = new_array
            self.array[self.size] = val
            self.size += 1
            return
        self.array[self.size] = val
        self.size += 1



    def prepend():
        pass

    def insert_at():
        pass

    def remove_at():
        pass

    def remove():
        pass

    def get():
        pass

