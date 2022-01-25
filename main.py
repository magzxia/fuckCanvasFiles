import requests

token = "2096~w2GsDFAC1Txmj3NGtf93Aq1zaL7UiIfpFBVMgFx3yNhi6qFbbiDoaSVmfKrS7WYP"

def list_files(course_id="", folder_id="", content_type=""):
    if course_id != "":
        res = requests.get(f"https://gatech.instructure.com/api/v1/courses/{course_id}/files?content_types[]={content_type}", headers={"Authorization": f"Bearer {token}"})
        print(res.json())
    elif folder_id != "":
        res = requests.get(f"https://gatech.instructure.com/api/v1/folders/{folder_id}/files?content_types[]={content_type}", headers={"Authorization": f"Bearer {token}"})
        print(res.json())

def main():
    list_files(course_id="231224", content_type="image")

if __name__ == "__main__":
    main()