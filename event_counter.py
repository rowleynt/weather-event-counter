import os
from OutputHandler import OutputHandler
from wecutils import read_xlsx, write_log, read_alias_file


def main():
    os.chdir(".\\data")  # change working directory to 'data' folder
    files = os.listdir()  # list of all files in 'data' folder
    aliases = read_alias_file()
    data = read_xlsx([file for file in files if ".xlsx" in file], aliases)
    print(OutputHandler(data))

    # write_log()


if __name__ == "__main__":
    main()
