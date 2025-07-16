# Modules
import tkinter as tk
import customtkinter as ctk
from tksheet import Sheet

# Classes
from classes.ColumnData import ColumnData

# Custom Modules
import tableScraper

# Services
from services.templateService import TemplateService


class FileCreationFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Services
        self.ts = TemplateService()

        # Variables
        self.sheetData = None
        self.sheetHeaders = None

        # Widgets
        self.tableFrame = ctk.CTkFrame(self)
        self.tableFrame.pack(fill="both", expand=True)

        self.sheet = Sheet(self.tableFrame)

        self.sheet.enable_bindings("all", "ctrl_select", "edit_header")

        # Sheet right click menu
        self.sheet.popup_menu_add_command(
            "Create Excel Sheet",
            self.createExcelSheet,
            index_menu=True,
            header_menu=True,
            empty_space_menu=False,
        )

        self.sheet.pack(fill="both")

    # Overrides the pack method so every time this widget is packed it updates the sheet
    def pack(self, table=None, **kwargs):
        if table is not None:
            self.sheetHeaders = table[0]
            self.sheetData = table[1:]
        if self.sheetHeaders is not None:
            self.updateSheet()
        super().pack(**kwargs)

    def createExcelSheet(self):
        selectedColumns = self.sheet.get_selected_columns()

        table = [self.sheet.headers(), *self.sheetData]
        columnData = ColumnData(columns=selectedColumns)

        df = tableScraper.createDfFromData(columnData, table)
        tableScraper.create_excel(df)

        self.ts.updateLast(
            columnData=columnData,
        )

    def updateSheet(self):
        self.sheet.headers(newheaders=self.sheetHeaders)

        self.sheet.set_data(data=self.sheetData)

        self.sheet.refresh()
