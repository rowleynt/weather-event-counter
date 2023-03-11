# weather event counter (change me)
weather event counter (change me)

## Initial Setup
Before running, `openpyxl` must be installed using `pip`. To do so, navigate to the folder containing the python files within the command line and enter the following command:

```virtualenv .env && source .env/bin/activate && pip install -r requirements.txt```

### First Run

The script must be run one time to set itself up before it can be used. To do so, navigate to the folder containing the python files and run the main script with the command:

```python event_counter.py``` or ```python3 event_counter.py``` if multiple versions of Python are installed.

This first run will generate the following folders: `data`, `events`, `logs`, and `output`

### Generated Folders

The `data` folder will contain the Excel sheet(s) to be processed, the `events` folder will contain the list of weather events to be considered and a list of aliases to those events for event names that may have changed or been entered incorrectly in `events.txt` and `aliases.txt` respectively.

The `logs` and `output` folder are used by the program for outputting the logs and formatted output data for each run respectively.

### Input Data

This script is designed to work with local storm report data obtained from http://mesonet.agron.iastate.edu/lsr/. Enter the WFO code(s) for the desired office or offices and the start/end dates and use the Excel download option. For best results, select 12:00AM on January 1st of the starting year. **Important: This tool has a limit to how long the given Excel sheets can be. If you are processing more data than can fit into one sheet, end the first sheet at 11:59PM and begin the next sheet at 12:00AM on the next day.**

Place the Excel sheet(s) into the `data` folder.

### Events and Aliases

Inside of the `events` folder, there are 2 generated `.txt` files: `events.txt` and `aliases.txt`.

The `events.txt` file will contain the names of each event that you would like the script to consider while running. It uses the following format:
```
event1
event2
event3
event4
...etc
```
Where each line within the file contains the entire name of one event. The event names within this file are case insensitive but spaces and special characters (slashes, dashes, etc.) are considered

The `aliases.txt` serves to map multiple different names to a single event in the `events.txt` file. This is necessary as some event names may have changed over time or may have been entered incorrectly and these aliases allow these events to still be counted. The file uses the following format:
```
event1
{
  alias1
  alias2
  alias3
  ...etc
}
event2
{
  alias1
  alias2
  alias3
  ...etc
}
```
**The names of the events must match exactly (case insensitive) with the name of an event in `events.txt` to be correctly aliased. The aliases must be tabbed over once.**

A realistic example:
```
water spout
{
  waterspout
}
```
This allows events in the Excel sheet(s) labeled as *waterspout* to be considered as instances of the *water spout* event.
