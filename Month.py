from wecutils import map_to_name, map_to_alias, log_error


class Month(object):
    def __init__(self, month_num, event_dict=None):
        #  month has the attributes: event_dict, month_num, name
        if event_dict is None:
            self.event_dict = {}
        else:
            self.event_dict = event_dict.copy()
        self.month_num = month_num
        self.name = map_to_name(month_num)

    def add(self, event_name):
        if event_name is not None:
            try:
                self.event_dict[event_name.upper()] += 1
                return "Success"
            except:  # eventually print error to log file here
                if map_to_alias(event_name.upper()) is not None:
                    self.event_dict[map_to_alias(event_name.upper())] += 1
                    return "Success"
                else:
                    return event_name, self.month_num
        else:
            return "Success"

    def get_name(self):
        return self.name

    def get_num(self):
        return self.month_num

    def __str__(self):
        return f"Month: {self.month_num} ({self.name})\nEvents: {self.event_dict}"
