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
