import os
import json

# reading json file:
with open("d:/Usuarios/Vicent Joan/Documents/REB/desktop_cleaner/extensions.json", 'r') as f:
    extensions = json.load(f)


# root to desktop folder, to -modify- in case it's needed 
desktop = f"C:\\Users\\usuario\\Desktop"

# class declaration:
class Files:
    def __init__(self):
        #self.extension = extension
        self.files = os.listdir(desktop)
    
    def create_folder(self):
        """ Creation of the missing folders """
        for extension in extensions["standard"]:
            if extension not in desktop:
                os.mkdir(desktop + "//" + extension)
    
    def move_files(self):
        """ Moving files to the correct folders """
        for file in self.files:
            file_list = file.split(".", 1)
            if  len(file_list) == 2 and file_list[1] in desktop:
                os.rename(desktop + "//" + "file", desktop + "//" + file_list[1] + "//" + "file")


# Object instance
fl1 = Files()

# Method calling
fl1.create_folder()
fl1.move_files()

