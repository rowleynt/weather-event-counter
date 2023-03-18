class Year(object):
    def __init__(self, year):
        self.year = year
        self.lst = []

    def add(self, events):
        for event in events:
            self.lst.append(event)

    def sum(self):
        pass

    def __str__(self):
        return f"{self.year} : {[[event.month, event.name] for event in self.lst]}"
