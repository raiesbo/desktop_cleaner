import os



desktop = f"C:\\Users\\usuario\\Desktop"

class files:
    def __init__(self, extension):
        self.extension = extension
        self.files = os.listdir(desktop)
    
    def create_folder(self):
        for file in self.files:
            file_list = file.split(".", 1)
            if  len(file_list) = 2 and file_list[1] not in desktop:
                os.makedir(desktop + "//" + file_list[1])
            os.rename(desktop + "//" + "file", desktop + "//" + file_list[1] + "//" + "file")
