import json
import urllib2
import requests
data = json.load(urllib2.urlopen('https://dog.ceo/api/breed/collie-border/images/random'))
i = 0
for key, value in data.items():
    i = i + 1
    if i == 2:
        string = value
        
print value

from IPython.display import Image
from IPython.core.display import HTML 
Image(url= value)
