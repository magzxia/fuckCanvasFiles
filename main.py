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
    course = canvas.get_course(input("Enter course id: "))

    print("Fetching files")
    files = []
    for file in course.get_files():
            files.append(File(file))

    print("Finding duplicates")
    dups = []
    counts = []
    for file in files:
        if files.count(file) > 1 and file not in dups:
            dups.append(file)
            counts.append(files.count(file))

    if dups == []:
        print("No duplicates found")
        quit()
    else:
        print("Duplicates found")

        for i in range(len(dups)):
            print("")
            print("{:<50} {:>50}".format("FILENAME", "COUNT"))
            print("{:<50} {:>50}".format("--------", "-----"))
            print("{:<50} {:>50}".format(dups[i].filename, counts[i]))
            print("")

        prompt = input("Duplicate files will now be deleted. Continue?[y/N]: ")

        if prompt == "y":
            print("Deleting duplicates")
            for file in files:
                if file in dups:
                    dup_id = dups.index(file)
                    if file.id != dups[dup_id].id:
                        print(f"deleting {file}")
                        file.delete()
        else:
            print("abort.")
            quit()            
            
    
if __name__ == "__main__":
    main()