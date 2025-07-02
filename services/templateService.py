# Modules
import os

# Classes
from classes.Template import Template
from classes.PickleFileSystem import PickleFileSystem


class TemplateService(PickleFileSystem):
    def __init__(self):
        super().__init__("templates")
        self.lastSearchFileName = "last_search_template.pkl"

        # Check for a templates directory
        if not os.path.isdir(self.basePath):
            os.mkdir(self.basePath)

        # Check if there is a lastSearchTemplate file
        if not os.path.isfile(os.path.join(self.basePath, self.lastSearchFileName)):
            self.create(
                self.lastSearchFileName,
                Template(),
            )
            print("File successfully created")

    # Overwrites last search template file
    def updateLast(self, template):
        self.update(self.lastSearchFileName, template)


def example():
    # Create an instance of the service
    # The default location of files manipulated is the current working directory -> templates
    # ./templates/<files>

    fileName = "baseball.pkl"
    ts = TemplateService()

    # deleting example file
    if os.path.isfile(os.path.join("templates/baseball.pkl")):
        ts.delete(fileName)
        print("Deleted file")

    test = Template("url", 1, [1, 2, 3, 4])
    test2 = Template("url", 2, [4, 5, 6, 7])

    # Create file
    # Does nothing if file already exists
    print("\nAttempting to create file\n")
    ts.create(fileName, test)

    value = ts.read(fileName)
    print("Test 1", value)

    # Updating
    # Overwrites already existing file
    print("\nAttempting to update file\n")
    ts.update(fileName, test2)

    value2 = ts.read(fileName)
    print("Test 2", value2)
