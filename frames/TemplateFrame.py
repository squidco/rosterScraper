# Modules
import customtkinter as ctk

# Components
from components.customTreeview import customTreeView

# Classes
from classes.Template import Template

# Services
from services.templateService import TemplateService

# Utils
from tableScraper import createExcelFromTemplate


class TemplateFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Services
        self.ts = TemplateService()

        # Variables
        self.template = Template()
        self.templateList = self.ts.listTemplates()

        # Widgets
        self.tree = customTreeView(
            self, columns=["Name", "URL", "Date"], show="headings"
        )
        self.tree.bind("<Double-1>", self.onDoubleClick)

    def pack(self, **kwargs):
        self.updateTemplates()
        self.displayTemplateTree()
        super().pack(**kwargs)

    def displayTemplateTree(self):
        headings = ["Name", "URL", "Date"]

        items = []
        for i in range(len(self.templateList)):
            template = self.templateList[i]
            iData = []

            iData.append(template.name)
            iData.append(template.url)
            iData.append(template.dateCreated)
            items.append(iData)

        self.tree.headings(headings)
        self.tree.bulkInsert(items)
        self.tree.pack(fill="both", expand=True)

    def updateTemplates(self):
        self.templateList = self.ts.listTemplates()

    def onDoubleClick(self, event):
        selection = self.tree.selection()[0]
        index = self.tree.index(selection)

        createExcelFromTemplate(self.templateList[index])
        print(f"INDEX {index}")
