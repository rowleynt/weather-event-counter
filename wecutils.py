import os
import datetime
from pathlib import Path
from openpyxl import load_workbook


# ---------------------------- Math ------------------------------ #
def total_all(cal):
    """Returns a dictionary containing each event with a corresponding running total computed from the
    given Excel sheets."""
    total_all_dict = build_event_dict()
    for year in cal:
        for month in year:
            for event in month.event_dict:
                total_all_dict[event] += month.event_dict[event]
    return total_all_dict


def total_byyear(cal):
    """Returns a dictionary containing each year represented in the data from the given Excel sheets. Each year
    is mapped to a dictionary containing totals for each event from that year."""
    total_byyear_dict = {}
    for year in cal.years:
        temp_dict = build_event_dict()
        total_byyear_dict[year.year] = temp_dict
        for month in year.months:
            for event in month.event_dict:
                total_byyear_dict[year.year][event] += month.event_dict[event]
    return total_byyear_dict


def total_bymonth(cal):
    """Returns a dictionary containing each month represented in the data from the given Excel sheets. Each month
    is mapped to a dictionary containing totals for each event from that month."""
    total_bymonth_dict = {}
    # create initial dictionary
    for month in cal.years[0].months:
        total_bymonth_dict[month.get_name()] = build_event_dict()
    # fill dictionary
    for year in cal.years:
        for month in year.months:
            for event in month.event_dict:
                total_bymonth_dict[month.get_name()][event] += month.event_dict[event]
    return total_bymonth_dict


def avg_bymonth(cal):
    """Computes the average number of events in each month and returns the results as a dictionary."""
    curr_month = datetime.datetime.now().month
    avg_bymonth_dict = total_bymonth(cal)
    for month in avg_bymonth_dict:
        for event in avg_bymonth_dict[month]:
            # checking for current month for more precise averages
            if map_to_num(month) <= curr_month:
                avg_bymonth_dict[month][event] = avg_bymonth_dict[month][event] / len(cal.years)
            else:
                avg_bymonth_dict[month][event] = avg_bymonth_dict[month][event] / (len(cal.years) - 1)
    return avg_bymonth_dict


def percent_total(ta):
    """Computes a sum total of all events and computes the percentage of each event against that total."""
    total_events = 0
    percent_total_dict = {}
    for event in ta:
        total_events += ta[event]
    for event in ta:
        percent_total_dict[event] = (ta[event] / total_events) * 100
    return percent_total_dict


def percent_bytime(tby):
    """Computes a sum total of all events in each year and computes the percentage of each event against that total."""
    percent_byyear_dict = {}
    for year in tby:
        total_events = 0
        percent_byyear_dict[year] = build_event_dict()
        for event in tby[year]:
            total_events += tby[year][event]
        for event in tby[year]:
            percent_byyear_dict[year][event] += (tby[year][event] / total_events) * 100
    return percent_byyear_dict
# ---------------------------------------------------------------- #


# ----------------------- Event Handling ------------------------- #
def build_event_dict():
    """Builds the dictionary containing the weather events based on the events contained within the
    events.txt file."""
    event_dict = {}
    f = open(str(Path(os.getcwd()).parent) + "\\events\\events.txt", "r")
    for line in f:
        event_dict[line.split("\n")[0].upper()] = 0
    f.close()
    return event_dict


def map_to_alias(event_name):
    """Maps a given event name to a corresponding name within the 'aliases.txt' file"""
    alias_dict = read_alias_file()
    if alias_dict.get(event_name) is not None:
        mapped_name = alias_dict[event_name]
        return mapped_name
    else:
        return None


def read_alias_file():
    """Reads the aliases.txt file and parses out each given alias. Returns a dictionary."""
    aliases = {}
    block = []
    f = open(str(Path(os.getcwd()).parent) + "\\events\\aliases.txt", "r")
    for line in f:
        block.append(line)
        if line == "}\n" or line == "}":
            # index 0 will always be the event that is being aliased to
            # 2 indexes will be { and }
            # only need to work with length of block - 3
            for i in range(len(block) - 3):
                temp = block[i + 2].split("\n")[0].split("\t")[1]
                aliases[temp.upper()] = block[0].split("\n")[0].upper()
            block = []
    return aliases
# ---------------------------------------------------------------- #


# ------------------------ Error Logging ------------------------- #
temp_error_log = []


def log_error(e, year, cal_name):
    """Adds the given error to the temp_error_log list"""
    temp_error_log.append(f"{str(datetime.datetime.now())} | Error in Calendar '{cal_name}': "
                          f"Failed to add event '{e[0]}' in month '{e[1]}' ({map_to_name(e[1])}) in year '{year}' \n")


def log_name(now):
    """Returns string representation of today's date in the format: mmddyyyy-time"""
    day = str(now.day)
    month = str(now.month)
    year = str(now.year)
    time = str(now.hour) + str(now.minute) + str(now.second) + str(now.microsecond)
    return month + day + year + "-" + time


def write_log():
    """Prints temp_error_list to a .txt file with a name defined by log_name"""
    currf = os.getcwd()
    os.chdir(str(Path(os.getcwd()).parent) + "\\logs")
    f = open(f"{log_name(datetime.datetime.now())}.txt", "a")
    for e in temp_error_log:
        f.write(e)
    f.close()
    os.chdir(currf)
# ---------------------------------------------------------------- #


# --------------------- Reading excel sheets --------------------- #
def read_xlsx(infile, calendar):
    """Navigates to the data folder and reads the .xlsx files located there."""
    data = load_workbook(infile)
    sheet = data.active
    for row in sheet.iter_rows(min_row=2, min_col=2, max_col=7):
        year = parse_year(row[0].value)
        month = parse_month(row[0].value)
        event = row[5].value
        calendar.add_event(event, year, month)


def parse_month(val):
    """Method for parsing the month out of the given column from the Excel sheet."""
    month = val.split(" ")[0].split("/")[1]
    return month


def parse_year(val):
    """Method for parsing the year out of the given column from the Excel sheet."""
    year = val.split(" ")[0].split("/")[0]
    return int(year)
# ---------------------------------------------------------------- #


# ---------------------------- Setup ----------------------------- #
def setup(curdir):
    """Called once in main file if directories do not exist (first run of script)"""
    create_directories(curdir)


def create_directories(curdir):
    """Creates directories within the folder containing the event_counter.py file if they do not
    already exist."""
    os.chdir(curdir)
    if not os.path.exists(".\\logs"):
        os.mkdir(".\\logs")
    if not os.path.exists(".\\output"):
        os.mkdir(".\\output")
    if not os.path.exists(".\\events"):
        os.mkdir(".\\events")
        os.chdir(".\\events")
        f1 = open("events.txt", "w")
        f2 = open("aliases.txt", "w")
        f1.close()
        f2.close()
        os.chdir(curdir)
    if not os.path.exists(".\\data"):
        os.mkdir(".\\data")
# ---------------------------------------------------------------- #


# ---------------------------- Misc ------------------------------ #
def map_to_name(month_num):
    """Maps a given month number code to that month's name."""
    name_dict = {
        "01": "JANUARY",
        "02": "FEBRUARY",
        "03": "MARCH",
        "04": "APRIL",
        "05": "MAY",
        "06": "JUNE",
        "07": "JULY",
        "08": "AUGUST",
        "09": "SEPTEMBER",
        "10": "OCTOBER",
        "11": "NOVEMBER",
        "12": "DECEMBER"
    }
    return name_dict[month_num]


def map_to_num(month_name):
    """Maps a given month name to that month's number code"""
    num_dict = {
        "JANUARY": 1,
        "FEBRUARY": 2,
        "MARCH": 3,
        "APRIL": 4,
        "MAY": 5,
        "JUNE": 6,
        "JULY": 7,
        "AUGUST": 8,
        "SEPTEMBER": 9,
        "OCTOBER": 10,
        "NOVEMBER": 11,
        "DECEMBER": 12
    }
    return num_dict[month_name]
# ---------------------------------------------------------------- #
