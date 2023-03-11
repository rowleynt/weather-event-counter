import datetime
from Year import Year
from wecutils import log_error


class Calendar(object):
    curr_year = datetime.datetime.now().year
    curr_month = datetime.datetime.now().month

    def __init__(self, name="CALENDAR"):
        #  Calendar has the attributes: name, years
        self.name = name
        self.years = []
        self._index = -1
        for year in range(2006, self.curr_year):
            self.add_year(Year(year))
        self.add_year(Year(self.curr_year, self.curr_month))

    def add_year(self, year):
        self.years.append(year)

    def add_event(self, event, year, month):
        index_y = self.indexof(year)
        index_m = self.years[index_y].indexof(month)
        try_add_event = self.years[index_y].months[index_m].add(event)
        if not try_add_event == "Success":
            log_error(try_add_event, year, self.name)

    def indexof(self, year):
        i = 0
        for y in self.years:
            if y.year == year:
                return i
            i += 1

    # --------------------------- Utility Methods --------------------------- #
    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        if self._index >= len(self.years):
            self._index = -1
            raise StopIteration
        else:
            return self.years[self._index]

    def __str__(self):
        return f"Calendar: {self.name}\nContains years: {[year.year for year in self.years]}"
