# Modules
import customtkinter as ctk

# Components
from components.customTreeview import customTreeView

# Classes
from classes.Template import Template

# Services
from services.templateService import TemplateService

class TemplateFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Services
        self.ts = TemplateService()

        # Variables
        self.template = Template()
        self.templateList = self.ts.listTemplates()
        
        # Widgets
        self.tree = customTreeView(self, columns=["Name", "URL", "Date"], show="headings")
        self.tree.bind("<Double-1>", self.onDoubleClick)

    def pack(self, **kwargs):
        self.updateTemplates()
        self.displayTemplateTree()
        super().pack(**kwargs)

    def displayTemplateTree(self):
        headings = ["Name", "URL", "Date"]

        data = []
        for template in self.templateList:
            tData = []
            tData.append(template.name)
            tData.append(template.url)
            tData.append(template.dateCreated)
            data.append(tData)

        self.tree.headings(headings)
        self.tree.bulkInsert(data)
        self.tree.pack(fill="both", expand=True)

        # createTreeView(self, data=data)

    def updateTemplates(self):
        self.templateList = self.ts.listTemplates()

    def onDoubleClick(self, event):
        item = self.tree.selection()[0]
        print(f"You clicked {self.tree.item(item)}")