from canvasapi import Canvas
import json

api_url = "https://gatech.instructure.com/"
api_key = "2096~w2GsDFAC1Txmj3NGtf93Aq1zaL7UiIfpFBVMgFx3yNhi6qFbbiDoaSVmfKrS7WYP"

class File:
    def __init__(self, id, filename, display_name, size):
        self.id = id
        self.filename = filename
        self.display_name = display_name
        self.size = size

    def __eq__(self, other):
        if self.filename == other.filename:
            return True
        else:
            return False

    def __str__(self):
        return self.filename

def main():
    canvas = Canvas(api_url, api_key)
    course = canvas.get_course("284188")

    #getting all files
    files = []
    for file in course.get_files():
            f = File(file.id, file.filename, file.display_name, file.size)
            files.append(f)

    dups = []
    for file in files:
        if files.count(file) > 1 and file not in dups:
            dups.append(file)
            print(f"{file} ..count:{files.count(file)}")
    
if __name__ == "__main__":
    main()