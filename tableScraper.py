# Library for opening url and creating
# requests
import urllib.request

# for parsing all the tables present
# on the website
from html_table_parser.parser import HTMLTableParser

# for converting the parsed data in a
# pandas dataframe
import pandas as pd

# Classes
from classes.ColumnData import ColumnData

# Formatters
import formatters


# Opens a website and read its
# binary contents (HTTP Response Body)
def url_get_content(url):
    # Opens a website and read its
    # binary contents (HTTP Response Body)

    # making request to the website
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)

    # defining the html contents of a URL.
    xhtml = f.read().decode("utf-8")

    # Defining the HTMLTableParser object
    p = HTMLTableParser()

    # feeding the html contents in the
    # HTMLTableParser object
    p.feed(xhtml)

    # Store the data in a dataframe
    return p


def select_columns():
    columnData = ColumnData()

    # Start collecting column input
    columnIn = input(
        "Enter the number of the column you'd like to grab (Enter 'n' to continue): "
    )

    # Appends a data object into the columns list
    while columnIn != "n":
        try:
            colDex = int(columnIn)
            columnName = input("Enter the name of the column: ")

            # Detect if a column was named "name(s)"/hometown and ask user if they would like to format it
            if columnName.lower() == "name" or columnName.lower() == "names":
                format = input(
                    "Name column detected. Would you like to format this column into: first, last,  abbreviated, and fullname? (y/n): "
                )
                if format[0].lower() == "y":
                    columnData.nameIndex = colDex
            elif columnName.lower() == "hometown":
                format = input(
                    "Hometown column detected. Would you like to format this column to drop the     previous school? (y/n): "
                )
                if format[0].lower() == "y":
                    columnData.hometownIndex = colDex
            else:
                data = (colDex, columnName)  # tuple
                columnData.columns.append(data)

        except Exception as e:
            print(
                f"Invalid input. Enter the index of a column or 'n' to continue.\n{e}"
            )
        columnIn = input(
            "Enter the number of the column you'd like to grab (Enter 'n' to continue): "
        )

    return columnData


def create_df(selectedColumns, df):
    dataFrameColumns = {}

    # Create columns for new dataframe
    for index, name in selectedColumns.columns:
        # Skipping the first value to get rid of unused header
        dataFrameColumns[name] = df[index][1:]

    # Adds the formatted names to the new columns
    if selectedColumns.nameIndex != -1:
        dataFrameColumns.update(formatters.formatNames(df[selectedColumns.nameIndex]))

    if selectedColumns.hometownIndex != -1:
        dataFrameColumns.update(
            formatters.formatHometown(df[selectedColumns.hometownIndex])
        )

    return pd.DataFrame(dataFrameColumns)


# Takes columnData type as first arg, 2D array as second arg
def createDfFromData(cd: ColumnData, table):
    """
    Returns a Pandas Dataframe made from a 2D array and columnData
    """
    # Create a dict to use for the dataframe columns arg
    dataFrameColumns = {}

    for c in cd.columns:
        header = table[0][c]
        dataFrameColumns[header] = []
        for i in range(1, len(table)):
            dataFrameColumns[header].append(table[i][c])

    return pd.DataFrame(dataFrameColumns)


def create_excel(
    columns,
):  # TODO You made a data type but this used to work off another data type
    # Create the final dataframe and excel sheet
    finalFrame = pd.DataFrame(columns)
    finalFrame.to_excel("test.xlsx", index=False)
