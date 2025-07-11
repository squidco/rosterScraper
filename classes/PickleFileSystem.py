# Modules
import os
import re
import pickle


class PickleFileSystem:
    def __init__(self, folder):
        self.basePath = os.path.join(folder)

    # Creates a new file; does nothing if file already exists
    def create(self, fileName: str, data):
        """
        Creates a new file. Does nothing if file already exists.
        """
        if not validateFileName(fileName):
            fileName += ".pkl"

        filePath = os.path.join(self.basePath, fileName)

        if not os.path.isfile(filePath):
            file = open(filePath, "wb")
            pickle.dump(data, file)
            file.close()

    # Appends data to the end of a file
    def append(self, fileName: str, data):
        """
        Appends data to the end of a file.
        """
        if not validateFileName(fileName):
            fileName += ".pkl"

        filePath = os.path.join(self.basePath, fileName)
        file = open(filePath, "ab")
        pickle.dump(data, file)
        file.close()

    # Overwrites existing file
    def update(self, fileName: str, data):
        """
        Overwrites an existing file.
        """
        if not validateFileName(fileName):
            fileName += ".pkl"

        filePath = os.path.join(self.basePath, fileName)
        file = open(filePath, "wb")
        pickle.dump(data, file)
        file.close()

    # Deletes a file
    def delete(self, fileName: str):
        """
        Deletes a file.
        """
        if not validateFileName(fileName):
            fileName += ".pkl"

        filePath = os.path.join(self.basePath, fileName)
        os.remove(filePath)

    # Reads a pickled file and returns its value
    def read(self, fileName: str):
        """
        Reads a pickled file and returns its value.
        """
        if not validateFileName(fileName):
            fileName += ".pkl"

        filePath = os.path.join(self.basePath, fileName)
        with open(filePath, "rb") as file:
            temp = pickle.load(file)
            return temp


# Checks that file names end with pkl; If not it will be added
def validateFileName(input_text):
    pattern = re.compile(r"\.pkl$")
    return pattern.search(input_text)
