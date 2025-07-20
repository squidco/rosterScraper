import tkinter.ttk as ttk

class customTreeView(ttk.Treeview):
    def __init__(self, parent, columns):
        super().__init__(parent, columns=columns, show="headings")

        # Horizontal Scrollbar
        hsb = ttk.Scrollbar(parent, orient="horizontal", command=self.xview)
        self.configure(xscrollcommand=hsb.set)
        
        hsb.pack(side="bottom", fill="x")

    def headings(self, headings: list[str], callback=print):
        for i, value in enumerate(headings):
            self.column(value, minwidth=5)
            self.heading(
                value,
                text=value,
                command=lambda dataTuple=(i, value): callback(dataTuple),
            )

    def bulkInsert(self, data: list[list[any]]):
        for r, row in enumerate(data):
            self.insert(parent="", index=r, values=row)
