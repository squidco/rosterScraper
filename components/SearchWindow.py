from tkinter import *
from tkinter.ttk import *

from components.Search import Search

from utils.clearFrame import clearFrame # Use dots instead of slashes
from utils.createTreeView import createTreeView

class SearchWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Scrape")
        self.geometry("800x800")
        self.tables = None
        self.selectedTable = IntVar()
        self.url = StringVar()


        self.searchFrame = Search(self)
        self.separator = Separator(self, orient=VERTICAL) #TODO fix this
        self.tableFrames = Frame(self)

        self.searchFrame.pack()
        self.separator.pack()
        self.tableFrames.pack()

    def createTableSelectionWindow(self, tables):
        self.tables = tables

        # Clear any existing frames in `self.tableFrames`
        clearFrame(self.tableFrames)

        # Create table frames
        for i, table in enumerate(tables):
            tableFrame = Frame(self.tableFrames, relief=RIDGE, padding=5)
            radio = Radiobutton(tableFrame, value=i, variable=self.selectedTable)
            radio.pack()

            createTreeView(tableFrame, table)
            
            tableFrame.pack()

    def handleImportButton(self, table):
        self.parent.importTable(self.tables[table.get()])