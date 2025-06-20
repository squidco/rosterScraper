from tkinter import *
from tkinter.ttk import *
from components.MenuBar import MenuBar
from components.SearchWindow import SearchWindow
from utils.clearFrame import clearFrame
from utils.createTreeView import createTreeView

import tableScraper


class App(Tk):
    def __init__(self):
        super().__init__()
        self.data = None

        # Window config
        self.title("Roster Scraper")
        self.geometry("600x400")
        self.option_add("*tearOff", False)

        # widgets
        ## Menubar
        self.menubar = MenuBar(self)
        self["menu"] = self.menubar

        ## Table
        self.tableFrame = Frame(self)
        self.columnData = tableScraper.ColumnData()

        ## Create excel button
        self.createButton = Button(
            self, text="Create File", command=lambda: self.fileClick()
        )
        self.tableFrame.pack(side=TOP, padx=1, pady=1)
        self.createButton.pack(side=BOTTOM, pady=1)

    def openScrapeWindow(self):
        # Clear the window and create a new search window
        self.searchWindow = SearchWindow(self)

    def headingClick(self, column):
        if column in self.columnData.columns:
            self.columnData.columns.remove(column)
        else:
            self.columnData.columns.append(column)
        print(self.columnData.columns)

    def fileClick(self):
        print(self.columnData.columns)
        df = tableScraper.createDfFromData(self.columnData, self.data)
        tableScraper.create_excel(df)

    def importTable(self, data):
        clearFrame(self.tableFrame)
        
        self.data = data

        createTreeView(self, data, self.headingClick)

# TODO work with pack more to get a decent layout
# TODO refactor any repeated code into its own function
# TODO try to rename variables and arguments to be clear
# TODO give arguments datatypes (arg: type)
# TODO add option to name the output file
# TODO detect if name/hometown columns are selected
# TODO add comments to functions that need them
# TODO use explicit imports instead of star imports
# TODO add menu options
## - file: show excel files
## - help: show an explanation of how to use the app
## - scrape: website (rename other option)
##           template (scrapes using preset options)
# TODO create template functionality
# TODO allow renaming of columns
# TODO auto-generate headshot paths
# (C:\ProgramData\AJT Systems\MAM\ESPN\LeagueAssets\NCAA\Headshots\lastname_firstname.png)
