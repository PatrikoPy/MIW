class FileManager():
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        with open(self.file_name) as file:
            text = file.read()
        return text

    def update_file(self, text_data):
        with open(self.file_name, 'a') as file:
            file.write(text_data + "\n")
