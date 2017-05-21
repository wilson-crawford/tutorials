# get all links in a web page
import re, urllib
htmlSource = urllib.urlopen("http://www.refdesk.com/").read(200000)
linksList = re.findall('<a href=(.*?)>.*?</a>',htmlSource)
for link in linksList:
    print link
