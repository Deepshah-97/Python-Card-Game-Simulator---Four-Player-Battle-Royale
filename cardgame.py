# The card game rules are as follows
#1) First there are 4 players playing the game, in which they will be randomly dealt 13 cards to each players.
#2) Each player will randomly pop a card from their respective hands and use them to play.
#3) So there will be 4 cards in total in the played cards pile
#4) Now we compare these 4 cards and denote winner card to the card with highest value. And discard all the cards that are played.
#5) The Player that had played the winner card will get 1 point.
#6) We repeat this process until all the cards are played.
#7) And finally we calculate how many times a player has won.

class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["None", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f" {Card.ranks[self.rank]}{Card.suits[self.suit]}"

    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit < other.suit
        else:
            return self.rank < other.rank

    def __gt__(self, other):
        if self.suit > other.suit:
            return True
        elif self.suit == other.suit:
            if self.rank > other.rank:
                return True
        return False

    def __eq__(self, other):
        return (self.rank == other.rank and self.suit == other.suit)   # this class is assigning the cards and its value.


c1 = Card(1, 3)
print(c1)

import random


class Deck:
    def __init__(self):
        self.deck = []
        for suit in range(4):
            for rank in range(1, 14):
                self.deck.append(Card(suit, rank))
        self.shuffle()

    def __str__(self):
        s = ""
        for i in range(len(self.deck)):  # You can put 52 but you can have multiple decks
            s += i * " " + str(self.deck[i]) + "\n"
        return s

    def __len__(self):
        return len(self.deck)

    def add_card(self, card):
        self.deck.append(card)

    def pop_card(self):
        return self.deck.pop()

    def shuffle(self):
        n_cards = len(self.deck)
        for i in range(n_cards):
            j = random.randrange(0, n_cards)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]   #this class represents the deck that we need for 52 cards

    def is_empty(self):
        return len(self.cards) == 0

    def deal(self, hands, n_cards=52):
        n_players = len(hands)
        for i in range(n_cards):
            if self.is_empty():  # self is the deck
                break
            card = self.pop_card()
            current_player = i % n_players
            hands[current_player].add_card(card)


class Hand(Deck):
    def __init__(self, name):
        self.deck = []
        self.name = name
        self.win_count = 0

    def __str__(self):
        # input()
        return self.name + ' -> ' + ' '.join([str(card) for card in self.deck])   #this class is for players hand

        # return self.label.join([str(card) for card in self.deck])

    # def __str__(self):
    # s = "Hand of " + self.label
    # if self.is_empty():
    # return s + " is empty"
    # s += " Contains \n" + Deck.__str__(self)        # override the class deck str
    # return s

    def label(self):
        return self.name

    def wincount(self):
        return self.win_count

    def roundwinner(self):
        self.win_count = self.win_count + 1


import time
import pandas as pd
import numpy as np

deck = Deck()

hands = []
players = ['Deep', 'Dilip', 'Dhruv', 'Nancy']
for i in players:
    hands.append(Hand(f'{i}'))

while len(deck) > 0:
    for hand in hands:
        hand.add_card(deck.pop_card())

# print(hands[0])
fd = []

for i in range(13):  # range is 13 if you want to complete all the cards
    # input()
    # time.sleep(1)
    pcards = []  # append the list with playerd cards
    for hand in hands:
        pcards.append(hand.pop_card())
        # print(pcards)

    wincard = max(pcards)

    whand = hands[pcards.index(wincard)]
    print(whand)
    whand.roundwinner()
    whand.wincount()

    print(f"\nRound{i}: " + ' '.join([str(card) for card in pcards]) + f' Winner:{whand.label()} {str(wincard)}'"\n")

    d1 = []
    for hand in hands:
        print(f"Score for {hand.label()}: {hand.wincount()}")
        d1.append(hand.wincount())

    # print(d1)
    fd.append(d1)
    # df=pd.DataFrame.from_dict(fd, orient='index', columns=['total win'])
    # print(df)
    # print(fd)

data = np.array(fd)

d_dataset = {}              # creating a data set which will have the result stored.

for d in enumerate(players):
    d_dataset[d[1]] = data[:, d[0]]

dataset = pd.DataFrame(d_dataset)
# print(fd[-1])



import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
students =fd[-1]
ax.bar(players,students)
plt.show()

plt.pie(fd[-1],labels = players)
plt.show()

#%matplotlib inline
# dataset.plot(xlabel='rounds',ylabel='scores',figsize=(12,8))


