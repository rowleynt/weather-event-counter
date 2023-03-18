class Event(object):
    def __init__(self, year, month, name):
        self.year = year
        self.month = month
        self.name = name

    def __str__(self):
        return f"{self.year} : {self.month} : '{self.name}'"
