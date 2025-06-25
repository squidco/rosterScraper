from tkinter import *
from tkinter.ttk import *
from customtkinter import *

from utils.clearFrame import clearFrame
from utils.createTreeView import createTreeView
from components.ScrollableFrame import ScrollableFrame

import tableScraper


class SearchWindow(CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # Window config
        self.parent = parent
        self.geometry("200x400")
        self.title("Scrape")

        # Variables
        self.tables = None
        self.selectedTable = IntVar()
        self.url = StringVar()

        self.createWidgets()

    def createWidgets(self):
        # Create the widgets for the search frame
        self.searchBar = CTkFrame(self)

        ## URL group
        urlLabel = CTkLabel(self.searchBar, text="Input the URL of webpage:")
        urlEntry = CTkEntry(self.searchBar, textvariable=self.url)

        ## Search button
        searchButton = CTkButton(
            self.searchBar,
            text="Scrape",
            command=lambda: self.scrapeButtonClick(self.url.get()),
        )

        self.importButton = CTkButton(
            self.searchBar,
            text="Import Table",
            command=lambda: self.handleImportButton(self.selectedTable),
        )

        # Place the searchbar in frame
        urlLabel.pack(padx=1)
        urlEntry.pack(ipadx=1)
        searchButton.pack()
        self.searchBar.pack(side=LEFT, fill=BOTH)

    def createTableSelectionWindow(self):
        # Clear any existing frames in `self.tableFrames`
        sFrame = CTkScrollableFrame(self)

        # Create table frames
        for i, table in enumerate(self.tables):
            tableFrame = CTkFrame(sFrame)
            radio = CTkRadioButton(tableFrame, value=i, text="", variable=self.selectedTable)
            radio.pack()

            createTreeView(tableFrame, table)
            tableFrame.pack()

        sFrame.pack(fill=BOTH, expand=True)

    def scrapeButtonClick(self, url):
        self.tables = tableScraper.url_get_content(url).tables
        self.importButton.pack(side=BOTTOM)
        self.createTableSelectionWindow()

    def handleImportButton(self, table):
        self.parent.importTable(self.tables[table.get()])
