# Modules
import tkinter as tk
import customtkinter as ctk

# Utils
from utils.createTreeView import createTreeView

# Services
from services.templateService import TemplateService

# Custom Module
import tableScraper


class SearchFrame(ctk.CTkFrame):
    def __init__(
        self, parent, url: tk.StringVar, tableIndex: tk.IntVar, changeFrame, importTable
    ):
        super().__init__(parent)

        # Services
        self.ts = TemplateService()

        # Window config
        self.parent = parent

        # Variables
        self.tables = None
        self.tableIndex = tableIndex
        self.url = url

        # Functions
        self.changeFrame = changeFrame
        self.importTable = importTable

        self.createWidgets()
        self.pack(fill="both", expand=True)

    def pack(self, table=None, **kwargs):
        super().pack(**kwargs)

    def createWidgets(self):
        # Create the widgets for the search frame
        self.searchBar = ctk.CTkFrame(self)
        self.searchBar.pack(side="left", fill="y")

        ## URL group
        urlLabel = ctk.CTkLabel(self.searchBar, text="Input the URL of webpage:")
        urlLabel.pack(padx=1)

        urlEntry = ctk.CTkEntry(self.searchBar, textvariable=self.url)
        urlEntry.pack(padx=1)

        ## Search button
        searchButton = ctk.CTkButton(
            self.searchBar,
            text="Scrape",
            command=lambda: self.scrapeButtonClick(self.url.get()),
        )
        searchButton.pack()

        self.importButton = ctk.CTkButton(
            self.searchBar,
            text="Import Table",
            command=lambda: self.handleImportButton(),
        )

        self.tableContainer = ctk.CTkScrollableFrame(self)
        self.tableContainer.pack(side="left", fill="both", expand=True)

    def createTableSelectionWindow(self):
        # Clear any existing frames in `self.tableFrames`

        # Create table frames
        for i, table in enumerate(self.tables):
            tableFrame = ctk.CTkFrame(self.tableContainer)
            radio = ctk.CTkRadioButton(
                tableFrame, value=i, text="", variable=self.tableIndex
            )
            radio.pack(fill="x", expand=True)

            createTreeView(tableFrame, table)
            tableFrame.pack()

    def scrapeButtonClick(self, url):
        self.tables = tableScraper.url_get_content(url).tables
        self.importButton.pack(side="bottom")
        self.createTableSelectionWindow()

        # Update last search template
        self.ts.updateLast(url=self.url.get())

    def handleImportButton(self):
        table = self.tables[self.tableIndex.get()]
        self.importTable(table)

        # Update last search template
        self.ts.updateLast(selectedTable=self.tableIndex.get())
