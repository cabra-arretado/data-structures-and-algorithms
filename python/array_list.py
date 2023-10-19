from array import array


class ArrayList:
    capacity = None
    size = None
    array = None

    def __init__(self, capacity=5):
        self.capacity = capacity
        # For the sake of using arra.array, we'll use -1 as a sentinel value
        self.array = array('i', [-1] * self.capacity)
        self.length = 0

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        self.get(index)

    def append(self, val):
        if self.length == self.capacity:
            self.capacity *= 2
            new_array = [None] * self.capacity
            new_array[:self.length] = self.array
            self.array = new_array
            self.array[self.length] = val
            self.length += 1
            return
        self.array[self.length] = val
        self.length += 1

    def prepend(self, val):
        if self.length == self.capacity:
            self.capacity *= 2
            new_array = [None] * self.capacity
            new_array[:self.length] = self.array[1:self.length + 1]
        else:
            array[1:self.length + 1] = array[:self.length]
        self.length += 1
        new_array[0] = val

    def insert_at(self, index, val):
        pass

    def remove_at(self, index):
        pass

    def remove(self, val):
        if not self.array:
            return False
        for i in range(self.length):
            if self.array[i] == val:
                if len(self) == 1:
                    self.length = 0
                    self.array[0] = -1
                    return True
                self.array[i:] = self.array[i+1:]
                return True

    def get(self, index):

        if index >= self.length or index < 0:
            raise IndexError
        return self.array[index]
