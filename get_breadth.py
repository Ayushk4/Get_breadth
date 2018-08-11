import urllib2
from extract_coursedata import html2json

cookie = '2979441BE649E9199066983994E580BF.worker3'

def getHTMLpage():
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', 'JSESSIONID={}'.format(cookie)))
    f = opener.open("https://erp.iitkgp.ac.in/Acad/central_breadth_tt.jsp")
    file = open('html_page.html', 'w')
    file.write(f.read())
    file.close()
    
getHTMLpage()
html2json()