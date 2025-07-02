import tkinter as tk
from services.templateService import TemplateService

# Want to find a solution that is not "drilling" the template service all the way down here

class TemplateMenu(tk.Menu):
    def __init__(self, parent: tk.Menu):
        super().__init__(parent)
        self.ts = TemplateService()
        
        parent.add_cascade(menu=self, label="Templates")
        self.add_command(label="Create New Template", command=lambda: print("new"))
        self.add_command(
            label="Create Template from last search", command=lambda: self.ts.updateLast()
        )
