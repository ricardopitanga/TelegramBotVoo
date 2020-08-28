import requests
import time
import json
from bs4 import BeautifulSoup

# Acesso ao site dos dados dos voos
#https://pt.flightaware.com/live/flight/GLO1906


#voo = text
res = requests.get ("https://pt.flightaware.com/live/flight/GLO1906/")
#res.encoding ="utf-8"
soup = BeautifulSoup(res.content, 'html.parser')
resultado = xpath.get_updates('.flightPageSummaryMap .flightPageFriendlyIdentLbl h1')
print (resultado)
