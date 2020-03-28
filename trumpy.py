# Copyright (c) 2020, Fumiya Watanabe

import random

class trump:
    deck = []
    hand = []
    discard = []
    
    def __init__(self):
        self.deck = []
        self.hand = []
        self.discard = []
        for k in range(13):
            if(k == 0):
                num = "A"
            elif(k == 10):
                num = "J"
            elif(k == 11):
                num = "Q"
            elif(k == 12):
                num = "K"
            else:
                num = str(k + 1)
            self.deck.append("C"+num)
            self.deck.append("S"+num)
            self.deck.append("D"+num)
            self.deck.append("H"+num)
        self.deck.append("Joker")
    
    def set_number_of_players(self, num):
        for k in range(num):
            self.hand.append([])

    def shuffle(self):
        random.shuffle(self.deck)

    def get_cards(self, hand_id, num):
        for k in range(num):
            if(not self.deck): # if deck is empty, reload deck from discard and shuffle
                self.deck = self.discard
                self.shuffle()

            self.hand[hand_id].append(self.deck.pop(0))

    def discard_hand(self, hand_id):
        for k in range(len(self.hand[hand_id])):
            self.discard.append(self.hand[hand_id].pop(0))
