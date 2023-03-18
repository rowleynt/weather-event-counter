class Month(object):
    def __init__(self, month):
        self.month = month
        self._index = -1
        self.lst = []

    def add(self, events):
        for event in events:
            self.lst.append(event)

    def sum(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        if self._index >= len(self.lst):
            self._index = -1
            raise StopIteration
        else:
            return self.lst[self._index]

    def __str__(self):
        return f"{self.month} : {[event.name for event in self.lst]}"
