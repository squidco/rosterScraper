from services.templateService import TemplateService

ts = TemplateService()

templates = ts.listTemplates()

print(templates[0])
