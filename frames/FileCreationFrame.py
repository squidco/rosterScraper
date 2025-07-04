# Modules
import customtkinter as ctk

# Utils
from utils.clearFrame import clearFrame
from utils.createTreeView import createTreeView

# Custom Modules
import tableScraper


class FileCreationFrame(ctk.CTkFrame):
    def __init__(self, parent, table, createExcelSheet, headingClick):
        super().__init__(parent)

        # Variables
        self.columnData = tableScraper.ColumnData()
        self.table = table

        # Functions
        self.headingClick = headingClick

        # Widgets
        self.tableFrame = ctk.CTkFrame(self)
        self.tableFrame.pack(fill="both", expand=True)

        self.createButton = ctk.CTkButton(
            self, text="Create File", command=lambda: createExcelSheet()
        )
        self.createButton.pack(pady=1, side="bottom")

    # Overrides the pack method so every time this widget is packed it tries to create a table
    def pack(self, table=None, **kwargs):
        if table is not None:
            self.table = table
        if self.table is not None:
            self.createTable()
        super().pack(**kwargs)

    def fileClick(self):
        df = tableScraper.createDfFromData(self.columnData, self.data)
        tableScraper.create_excel(df)

    def createTable(self):
        clearFrame(self.tableFrame)

        createTreeView(self.tableFrame, self.table, self.headingClick)
