from canvasapi import Canvas

api_url = "https://gatech.instructure.com/"
api_key = "2096~w2GsDFAC1Txmj3NGtf93Aq1zaL7UiIfpFBVMgFx3yNhi6qFbbiDoaSVmfKrS7WYP"

def main():
    canvas = Canvas(api_url, api_key)
    course = canvas.get_course("284188")
    files = []

    for file in course.get_files():
        if file not in files:
            files.append(file)

    
        
    


if __name__ == "__main__":
    main()