import urllib2

cookie = 'A69E33F0E8877955C1BFF8A9B4396F9B.worker3'

def getHTMLpage():
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', 'JSESSIONID={}'.format(cookie)))
    f = opener.open("https://erp.iitkgp.ac.in/Acad/central_breadth_tt.jsp")
    file = open('html_page.html', 'w')
    file.write(f.read())
    file.close()
    
getHTMLpage()