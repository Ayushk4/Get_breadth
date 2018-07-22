from bs4 import BeautifulSoup
import json
import re

def html2json():
    with open("html_page.html") as fp:
        soup = BeautifulSoup(fp,"html.parser")

    i = 0
    courses = soup.find_all('tr')

    dataBreadth = {}

    while (i<len(courses)):
        rows = courses[i].find_all('td')

        if len(rows)>3:
            regex = r"[a-zA-Z]{2}\d{5}"

            #The following code gets table headings for each row into a list
            matches = re.findall(regex, str(rows[0]), re.MULTILINE)
            dataBreadth [matches[0]] = {}        
            dataBreadth [matches[0]]["name"] = rows[1].string
            dataBreadth [matches[0]]["id"] = matches[0]

            #while (j<len(rows)):
            #   dataBreadth [keys[j]] = rows[j].string
            #    print(rows[j])
            #    print(keys[j-1])
            #   j = j+1

        i = i+1

    print(dataBreadth)
    print(len(dataBreadth))
    json_file_main = open("breadth_course.json", "w+")
    json_file_main.write(json.dumps(dataBreadth))
    json_file_main.close()

#html2json()