import urllib2
from extract_coursedata import html2json

cookie = 'E5623814DD36ACBD35E7C7B51F99668A.worker2'

def getHTMLpage():
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', 'JSESSIONID={}'.format(cookie)))
    f = opener.open("https://erp.iitkgp.ac.in/Acad/central_breadth_tt.jsp")
    file = open('html_page.html', 'w')
    file.write(f.read())
    file.close()
    html2json()

    
getHTMLpage()