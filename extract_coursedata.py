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

        if len(rows)>1:
            regex = r"[a-zA-Z]{2}\d{5}"

            #The following code gets table headings for each row into a list
            matches = re.findall(regex, str(rows[0]), re.MULTILINE)
            dataBreadth [matches[0]] = {}        
            dataBreadth [matches[0]]["id"] = matches[0]
            dataBreadth [matches[0]]["name"] = rows[1].string
            dataBreadth [matches[0]]["L-T-P"] = rows[2].string
            dataBreadth [matches[0]]["prereq"] = []
            dataBreadth [matches[0]]["prereq"].append(rows[3].string)
            dataBreadth [matches[0]]["prereq"].append(rows[4].string)
            dataBreadth [matches[0]]["prereq"].append(rows[5].string)
            dataBreadth [matches[0]]["Department"] = rows[6].string
            dataBreadth [matches[0]]["Slot"] = (rows[7].string).strip(' \n\t')
            dataBreadth [matches[0]]["Room"] = (rows[8].string).strip(' \n\t')

            #while (j<len(rows)):
            #   dataBreadth [keys[j]] = rows[j].string
            #    print(rows[j])
            #    print(keys[j-1])
            #   j = j+1
            # Uncomment below to view the dictionary on console
            # print(dataBreadth)
        i = i+1


    # Create schedule list for each day, each hour
    with open('slots.json') as fin:
        slots_data = json.load(fin)
    days = 5
    hours = 9
    schedule = [[[] for _ in range(hours)] for __ in range(days)]
    for data in dataBreadth.keys():
        for slots in [dataBreadth[data]['Slot']]:
            slots = slots[1:len(slots)-1]
            slots.replace(" ","")
            if len(slots)>2:
                slots = [x for x in slots.split(',')]
            else:
                slots = [slots]
            for slot in slots:
                if len(slot)>1:
                    for week_hour in slots_data[slot]:
                        hour = int(week_hour)%10
                        day = int(int(week_hour)//10)
                        room = dataBreadth[data]['Room']
                        if any(place in room for place in ['NC', 'NR']):
                            schedule[day][hour].append(room)

    
    print(str(len(dataBreadth)) + " breadth courses scraped!")
    with open('breadth_schedule.json', 'w+') as fout:
        json.dump(schedule, fout)
    json_file_main = open("breadth_course.json", "w+")
    json_file_main.write(json.dumps(dataBreadth))
    json_file_main.close()

html2json()