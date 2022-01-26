from canvasapi import Canvas, folder, file

api_url = "https://gatech.instructure.com/"
api_key = "2096~w2GsDFAC1Txmj3NGtf93Aq1zaL7UiIfpFBVMgFx3yNhi6qFbbiDoaSVmfKrS7WYP"

def main():
    canvas = Canvas(api_url, api_key)
    course = canvas.get_course("231224")
    for file_obj in course.get_files():
        print(file_obj)


if __name__ == "__main__":
    main()