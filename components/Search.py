from tkinter import *
from tkinter.ttk import *

import tableScraper

class Search(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # Vars
        self.url = StringVar()
        self.tables = None
        self.selectedTable = parent.selectedTable

        # Widgets and layout
        self.createWidgets()

        self.selectionFrame = Frame(self)
        
    def createWidgets(self):
        # Create the widgets for the search frame
        self.searchBarFrame = Frame(self)
        
        ## URL group
        self.urlLabel = Label(self.searchBarFrame, text="Input the URL of the webpage:")
        self.urlEntry = Entry(self.searchBarFrame, textvariable=self.url)

        ## Search button
        self.searchButton = Button(
            self.searchBarFrame,
            text="Scrape",
            default=ACTIVE,
            command=lambda: self.scrapeButtonClick(self.url.get()),
        )

        self.importButton = Button(
            self.searchBarFrame,
            text="Import Table",
            default=ACTIVE,
            command=lambda: self.parent.handleImportButton(self.selectedTable),
        )

        # Place the widgets in frame
        self.urlLabel.pack(side=LEFT, padx=1)
        self.urlEntry.pack(side=LEFT, ipadx=1)
        self.searchButton.pack(side=LEFT)
        self.searchBarFrame.pack(side=LEFT, ipadx=1, ipady=1)

    def scrapeButtonClick(self, url):
        tables = tableScraper.url_get_content(url).tables
        self.importButton.pack(side=BOTTOM)
        self.parent.createTableSelectionWindow(tables)
        self.selectionFrame.pack(RIGHT)