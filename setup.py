import os


desktop = f"C:\\Users\\usuario\\Desktop"


class Files:
    def __init__(self):
        #self.extension = extension
        self.files = os.listdir(desktop)
    
    def create_folder(self):
        for file in self.files:
            file_list = file.split(".", 1)
            if  len(file_list) == 2 and file_list[1] not in desktop:
                os.mkdir(desktop + "//" + file_list[1])
            if  len(file_list) == 2 and len(file_list) != "exe":
                os.rename(desktop + "//" + "file", desktop + "//" + file_list[1] + "//" + "file")


fl1 = Files()

fl1.create_folder()