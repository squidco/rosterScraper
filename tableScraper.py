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
from classes.Template import Template

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


def createExcelFromTemplate(template: Template):
    # Retrieves all tables from the url, then grabs specified table
    table = url_get_content(template.url).tables[template.selectedTable]
    
    # Creates an excel sheet from the template's data
    # TODO Add name to 
    df = createDfFromData(template.columnData, table)
    
    create_excel(df)
    