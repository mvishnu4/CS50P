class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0
    def __str__(self):
        return "🍪"*self._size

    def deposit(self, n):
        if self._size + n <= self._capacity:
            self._size = self._size + n
        else:
            raise ValueError

    def withdraw(self, n):
        if self._size - n > 0:
            self._size = self._size - n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

