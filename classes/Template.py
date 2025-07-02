from dataclasses import dataclass
from classes.ColumnData import ColumnData


@dataclass
class Template:
    def __init__(
        self,
        url: str = "",
        selectedTable: int = -1,
        columnData: ColumnData = ColumnData(),
    ):
        self.url = url
        self.selectedTable = selectedTable
        self.columnData = columnData

    def __str__(self):
        return f"\nURL: {self.url}\nTable: {self.selectedTable}\nColumnData: {self.columnData}"
