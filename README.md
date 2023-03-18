# weather event counter
weather event counter

## Initial Setup
Before running, `openpyxl` must be installed using `pip`. To do so, navigate to the folder containing the python files within the command line and enter the following command:

```pip install -r requirements.txt```

### First Run

The script must be run one time to set itself up before it can be used. To do so, navigate to the folder containing the python files and run the main script with the command:

```python event_counter.py``` or ```python3 event_counter.py``` if multiple versions of Python are installed.

This first run will generate the following folders: `data`, `logs`, and `output`, along with `aliases.txt`

### Generated Files

The `data` folder will contain the user-provided Excel sheet(s) to be processed. The `aliases.txt` file is used for event name aliases (see **Events and Aliases** section below)

The `logs` and `output` folder are used by the program for outputting the logs and formatted output data for each run respectively.

### Input Data

This script is designed to work with local storm report data obtained from http://mesonet.agron.iastate.edu/lsr/. Enter the WFO code(s) for the desired office or offices and the start/end dates and use the Excel download option. For best results, select 12:00AM on the 1st day of the first month to be counted. **Important: This tool has a limit to how long the given Excel sheets can be. If you are processing more data than can fit into one sheet, end the first sheet at 11:59PM and begin the next sheet at 12:00AM on the next day.**

Place the Excel sheet(s) into the `data` folder.

### Events and Aliases

The event names that are counted are dynamically created while reading the data. This means that only events which are present in the data will be represented in the data and also serves to reduce the setup time for the user. However, this also means that any events that have been entered incorrectly and/or have had their names changed over the period of time which is represented in the data will be counted as separate events, which will reduce the accuracy of the output. This problem can be alleviated using *aliases*.

A file named `aliases.txt` can be found in the main directory after the initial setup. This file can be used to map multiple different event names found in the input data to a single event name to be counted instead.

The file will initially be empty, and must be updated with desired aliases. The format of an alias is as:
```
<name1 from input>=<event name to be counted>
<name2 from input>=<event name to be counted>
<name3 from input>=<event name to be counted>
etc.
```
*The aliases file is case insensitive, but the format `<alias>=<name>` must be matched to work properly.*

Example `aliases.txt` file:
```
waterspout=water spout
```
This allows events in the Excel sheet(s) labeled as *waterspout* to be considered as instances of the *water spout* event. Events may be given multiple aliases by listing multiple names equalling the desired event name.

Example:
```
waterspout=water spout
water-spout=water spout
water_spout=water spout
```
*waterspout*, *water-spout*, *water_spout* will all be counted as instances of *water spout* when encountered.

## Running

After completing the first time setup, run the script again with the command ```python event_counter.py```. An output file is created within the `output` folder in the form of an Excel spreadsheet. The output file contains the following fields:
```
Total Events By Year: Tally of the total number of each event in each year, starting from the earliest date and ending at the latest date within the input data

Total Events By Month: Tally of the total number of each event that occured in each month (JAN-DEC)

Total Events Overall: Tally of the total number of each event that occured over the period of time defined by the input data

Average Events By Month: The average number of each event that occured in each month (JAN-DEC). This is the total number of events in each month divided by the number of months elapsed

Percentage of Events By Year: The percentage of each event out of the total that occured in each year

Percentage of Events By Month: The percentage of each event out of the total that occured in each month

Percentage of Events Overall: The percentage of each event out of the total of all events
```

The script will also generate a log file within the `logs` folder. This log file will contain an error detailing each event found within the input data that was not represented within the `events.txt` file. These specific occurrences can either be added to the events file or to the `aliases.txt` file to be counted if the script is run again.
