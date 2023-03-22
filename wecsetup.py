import os


def main():
    if not os.path.exists("logs"):
        create_directories(os.getcwd())
        print("Directories generated. Place .xlsx file(s) into 'data' folder before running 'event_counter.py'")
    else:
        print("Setup process has already been completed. Please use `event_counter.py`.")


def create_directories(curdir):
    """Creates directories within the folder containing the event_counter.py file if they do not
    already exist."""
    os.chdir(curdir)
    f = open("aliases.txt", "w")
    f.close()
    if not os.path.exists("logs"):
        os.mkdir("logs")
    if not os.path.exists("output"):
        os.mkdir("output")
        os.chdir(curdir)
    if not os.path.exists("data"):
        os.mkdir("data")


if __name__ == "__main__":
    main()
