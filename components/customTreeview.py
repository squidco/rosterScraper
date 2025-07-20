import tkinter.ttk as ttk


class customTreeView(ttk.Treeview):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # Horizontal Scrollbar
        hsb = ttk.Scrollbar(parent, orient="horizontal", command=self.xview)
        self.configure(xscrollcommand=hsb.set)

        hsb.pack(side="bottom", fill="x")

    def headings(self, headings: list[str], callback=print):
        """
        Takes a list of strings and sets the headings for the treeview
        """
        for i, value in enumerate(headings):
            self.column(value, minwidth=5)
            self.heading(
                value,
                text=value,
                command=lambda dataTuple=(i, value): callback(dataTuple),
            )

    def bulkInsert(self, data: list[list[str]]):
        """
        Takes a list of lists of strings and inserts everything into the treeview
        """
        for r, row in enumerate(data):
            self.insert(parent="", index=r, values=row)
