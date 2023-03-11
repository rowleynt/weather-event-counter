from Month import Month
from wecutils import build_event_dict


class Year(object):
    def __init__(self, year, num_months=12):
        #  year has the attributes: year, length, event_dict, months
        self.year = year
        self.length = num_months
        self.event_dict = build_event_dict()  # eventually this should be sent in by main script
        self.months = []
        self._index = -1  # for iteration
        for i in range(1, self.length + 1):  # prepend 0s to front of single digit months
            if i < 10:
                month_num = f"0{i}"
            else:
                month_num = f"{i}"
            self.add_month(Month(month_num, self.event_dict))

    def add_month(self, month):
        self.months.append(month)

    def get_month(self, month):
        for mon in self.months:
            if mon.get_name() == month or mon.get_num() == month:
                return mon
        return None

    def indexof(self, mon):
        i = 0
        for m in self.months:
            if m.name == mon or m.month_num == mon:
                return i
            i += 1

    # --------------------------- Utility Methods --------------------------- #
    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        if self._index >= len(self.months):
            self._index = -1
            raise StopIteration
        else:
            return self.months[self._index]

    def __str__(self):
        return f"Year: {self.year}\nContains: {[f'({month.month_num}) {month.name}' for month in self.months]}"
