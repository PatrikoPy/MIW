from wprowadzenie02.file_manager import FileManager

reader = FileManager.FileManager("tekst.txt")
reader.update_file("nowy tekst")
print(reader.read_file())
