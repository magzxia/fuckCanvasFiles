class Folder:
    def __init__(self, id, name, full_name, files_count, folders_count):
        self.id = id
        self.name = name
        self.full_name = full_name
        self.files_count = files_count
        self.folders_count = folders_count

class Files:
    def __init__(self, id, display_name, size):
        self.id = id
        self.display_name = display_name
        self.size = size
