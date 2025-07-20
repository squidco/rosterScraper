# Modules
import tkinter as tk
import customtkinter as ctk

# Classes
from classes.Template import Template

# Utils
from utils.createTreeView import createTreeView

# Custom Module
import tableScraper

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

    def pack(self, **kwargs):
        self.updateTemplates()
        self.displayTemplateTree()
        super().pack(**kwargs)

    def displayTemplateTree(self):
        headings = ["Name", "URL", "Date"]

        data = [headings]
        for template in self.templateList:
            tData = []
            tData.append(template.name)
            tData.append(template.url)
            tData.append(template.dateCreated)
            data.append(tData)
            
        createTreeView(self, data=data)

    def updateTemplates(self):
        self.templateList = self.ts.listTemplates()
        print(self.templateList)

