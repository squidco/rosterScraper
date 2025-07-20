# Modules
from datetime import datetime

# Classes
from dataclasses import dataclass
from classes.ColumnData import ColumnData


@dataclass
class Template:
    def __init__(
        self,
        name: str = "",
        url: str = "",
        selectedTable: int = -1,
        columnData: ColumnData = ColumnData(),
    ):
        self.name = name
        self.url = url
        self.selectedTable = selectedTable
        self.columnData = columnData
        self.dateCreated = datetime.now()

    def __str__(self):
        return f"\nName: {self.name}\nURL: {self.url}\nTable: {self.selectedTable}\nColumnData: {self.columnData}\nCreated on: {self.dateCreated}"

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)
