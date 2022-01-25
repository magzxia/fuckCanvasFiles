import requests
import fs
import json

token = "2096~w2GsDFAC1Txmj3NGtf93Aq1zaL7UiIfpFBVMgFx3yNhi6qFbbiDoaSVmfKrS7WYP"

#TODO: replace print statements with sane return statements
def list_files(course_id="", folder_id="", content_type="", sort="name"):
    if course_id != "":
        res = requests.get(f"https://gatech.instructure.com/api/v1/courses/{course_id}/files?content_types[]={content_type}&sort={sort}", headers={"Authorization": f"Bearer {token}"})
        print(res.json())
    elif folder_id != "":
        res = requests.get(f"https://gatech.instructure.com/api/v1/folders/{folder_id}/files?content_types[]={content_type}&sort={sort}", headers={"Authorization": f"Bearer {token}"})
        print(res.json())

def list_all_folders(course_id=""):
    res = requests.get(f"https://gatech.instructure.com/api/v1/courses/{course_id}/folders", headers={"Authorization": f"Bearer {token}"})

    folders = []
    for folder in res.json():
        folders.append(fs.Folder(folder["id"], folder["name"], folder["full_name"], folder["files_count"], folder["folders_count"]))
    
    return folders

def main():
    folders = list_all_folders(course_id="231224")
    print(folders[1].__dict__)

if __name__ == "__main__":
    main()