import os
from Calendar import Calendar
from OutputHandler import OutputHandler
from wecutils import read_xlsx, setup, write_log


def main():
    fmain = os.getcwd()
    if os.path.exists(".\\data"):
        os.chdir(".\\data")  # change working directory to 'data' folder
        files = os.listdir()  # list of all files in 'data' folder
        calendar = Calendar()
        for file in files:  # do for every file found within 'data' folder
            if ".xlsx" in file:  # checks for valid xlsx file
                read_xlsx(file, calendar)
        print(OutputHandler(calendar))
        write_log()
    else:
        setup(fmain)
        print("Directories generated. Place .xlsx file(s) into 'data' folder and edit 'event.txt' and 'aliases.txt' in the"
              " 'events' folder before rerunning.")


if __name__ == "__main__":
    main()
