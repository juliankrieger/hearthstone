import json
from deck import Deck
from card import Card

def loadData():
    file = __file__.replace("cardparser.pyc", "").replace("cardparser.py", "") + "cards.json"

    cards = []

    with open(file, "r") as jsonfile:
        card_data = json.load(jsonfile)


        for entry in card_data:
            cards.append(Card(**entry))

    return cards

def main():

    all_cards = loadData()

    for card in all_cards:
        if card.name:
            if "ice" in card.name.lower():
                print()
                print(card.name)
                print(card.cost)
                print(card.type)
                print(card.attack)
                print(card.health)




if __name__ == '__main__':
    main()
