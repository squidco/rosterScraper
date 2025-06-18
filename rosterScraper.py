# Library for opening url and creating
# requests
# import urllib.request

# pretty-print python data structures
from pprint import pprint

# for parsing all the tables present
# on the website
# from html_table_parser.parser import HTMLTableParser

# for converting the parsed data in a
# pandas dataframe
import pandas as pd

import sys
# import formatters
import tableScraper


from tkinter import *
from tkinter.ttk import *
from App import App



def main():
    # TODO Add template selection
    # Get url of website to scrape for tables
    
    url = input("Input the URL of the roster page:")
    tables = tableScraper.url_get_content(url).tables
    
    
    # Present user with options and prompt to select the table with the data they'd like to scrape
    pprint(tables)
    index = int(input("Enter the index of the table you would like to use:"))
    
    # Make a new dataframe for user specified table
    df = pd.DataFrame(tables[index])
    pprint(df.head())
    
    
    selectedColumns = tableScraper.select_columns()
    finalFrame = tableScraper.create_df(selectedColumns, df)
    finalFrame.to_excel("test.xlsx", index=False)
    


if __name__ == "__main__":
    # main()
    window = App()
    window.mainloop()
    sys.exit(0)