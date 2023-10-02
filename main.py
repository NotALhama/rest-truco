import requests as r
import json
#import flask


valid_cards = ["AS,AD,AC,AH,4S,4D,4C,4H,5S,5D,5C,5H,6S,6D,6C,6H,7S,7D,7H,JS,JD,JR,QS,QD,QC,QH,KS,KD,KH"].split(",")

class Server:
    url = "https://deckofcardsapi.com"
    players = []
    
    def _init_(self):
        self.deck_id = ""

    def genDeck(self):
        response = r.get(self.url+"/api/deck/new/shuffle/?cards=AS,AD,AC,AH,4S,4D,4C,4H,5S,5D,5C,5H,6S,6D,6C,6H,7S,7D,7H,JS,JD,JR,QS,QD,QC,QH,KS,KD,KH")
        self.deck_id = response.json()["deck_id"]
        return self.deck_id
    
    def addPlayer(self):
        pass


class Team:
    players = []
    points = 0
    
    def __init__(self, players):
        self.players = players

class Client:
    url = "https://deckofcardsapi.com"
    deck_id = ""
    num = 0
    team = 0
    name = ""
    hand = []
    burn_counter = 0
    
    def _init_(self, id):
        self.deck_id = id
    
    def draw(self):
        response = r.get(self.url+"/api/deck/%s/draw/?count=3" % self.deck_id)
        cards = response.json()["cards"]
        self.hand = [cards[i]["code"] for i in range(3)]

    def burn(self):
        old_hand = hand
        self.hand = []
        self.draw()
        self.burn_counter += 1

    def play(self, card):
        if card not in range(len(self.hand)):
            return -1
        else:
            self.hand.remove(self.hand[card])
            return 0
            



server = Server()
print(server.genDeck())
