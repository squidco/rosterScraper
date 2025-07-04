# Modules
import tkinter as tk
import customtkinter as ctk

# Classes
from classes.Template import Template

# Utils
from utils.createTreeView import createTreeView

# Custom Module
import tableScraper

class TemplateFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Variables
        self.template = Template()
        self.templateList = []
        
    # TODO render list of all templates
    # TODO templates need a name property
    