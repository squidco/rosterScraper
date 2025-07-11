from dataclasses import dataclass


@dataclass
class ColumnData:
    def __init__(
        self, columns: set = set(), nameIndex: int = -1, hometownIndex: int = -1
    ):
        self.columns = columns
        self.nameIndex = nameIndex
        self.hometownIndex = hometownIndex
        
    # TODO expand this to include all strings and stuff
    def __str__(self):
        return f"Columns: {self.columns}"
