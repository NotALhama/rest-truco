import requests as r
import json
 
url = "https://deckofcardsapi.com"
response = r.get(url+"/api/deck/new/shuffle/?cards=AS,AD,AC,AH,4S,4D,4C,4H,5S,5D,5C,5H,6S,6D,6C,6H,7S,7D,7H,JS,JD,JR,QS,QD,QC,QH,KS,KD,KH")
y = response.json()
print(y["deck_id"])
d_id = y["deck_id"]
 
response=r.get(url+"/api/deck/%s/draw/?count=3" % d_id)
cards = response.json()
cards = cards["cards"]
print(cards[0])
