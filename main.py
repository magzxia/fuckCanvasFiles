from canvasapi import Canvas, file
import requests

api_url = "https://gatech.instructure.com/"
api_key = "2096~w2GsDFAC1Txmj3NGtf93Aq1zaL7UiIfpFBVMgFx3yNhi6qFbbiDoaSVmfKrS7WYP"

class File(file.File):
    def __init__(self, file: file.File):
        self._requester = file._requester
        self.id = file.id
        self.filename = file.filename

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
            files.append(File(file))

    dups = []
    for file in files:
        if files.count(file) > 1 and file not in dups:
            dups.append(file)
            #print(f"{file} ..count:{files.count(file)}")

    for file in files:
        if file in dups:
            dup_id = dups.index(file)
            if file.id != dups[dup_id].id:
                print(f"deleting {file}")
                file.delete()            
            
    
if __name__ == "__main__":
    main()