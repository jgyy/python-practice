"""Blackjack Script"""
import random

SUITS = ('Hearts', 'Diamond', 'Spades', 'Clubs')
RANKS = ('Two', 'Three', 'Four', 'Five',
         'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')
VALUES = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,
          'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
PLAYING = True


class Card:
    """Class for all card attributes"""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

    def text(self):
        """:return: to return rank and suit as text"""
        return self.rank + " of " + self.suit


class Deck:
    """Start with an empty list"""

    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        """Shuffle the whole deck"""
        random.shuffle(self.deck)

    def deal(self):
        """Deal the whole deck"""
        return self.deck.pop()


class Hand:
    """
    Start with an empty list as we did in the Deck class
    Start with zero value
    Add an attribute to keep track of aces
    """

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        """
        from Deck.deal() ==> single Card(suit, rank)
        :param card: card passed in
        track aces
        """
        self.cards.append(card)
        self.value += VALUES[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        """
        IF TOTAL VALUE > 21 AND I STILL HAVE AN ACE
        THAN CHANGE MY ACE TO BE A 1 INSTEAD OF AN 11
        """
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class Chips:
    """The total can be set to a default value or supplied by a user input"""

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        """Calculate the bet won"""
        self.total += self.bet

    def lose_bet(self):
        """Calculate the losing bet"""
        self.total -= self.bet


def take_bet(chips):
    """Function to take bets"""
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Sorry, please provide an integer.")
        else:
            if chips.bet > chips.total:
                print(f"Sorry, you do not have enough chips! You have: {chips.total}")
            else:
                break


def hit(decks, hand):
    """
    :param decks:
    :param hand:
    """
    single_card = decks.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(decks, hand, play):
    """
    HIT hh stand
    :param decks:
    :param hand:
    :param play: use this local variable instead of using global
    :return: To control an upcoming while loop
    """
    while True:
        input_x = input('\nHit or Stand? Enter h or s ')
        if input_x[0].lower() == 'h':
            hit(decks, hand)
        elif input_x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            play = False
        else:
            print("Sorry, I did no understand that, Please enter h or s only!")
            continue
        break
    return play


def show_some(player, dealer):
    """
    :param player:
    :param dealer:
    """
    print("\nDEALERS HAND: \none card hidden!")
    print(dealer.cards[1])
    print("\n\nPLAYERS HAND: ")
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    """
    :param player:
    :param dealer:
    """
    print("\nDEALERS HAND: ")
    for card in dealer.cards:
        print(card)
    print("\n\nPLAYERS HAND: ")
    for card in player.cards:
        print(card)


def player_bust(chips):
    """busted player"""
    print("\nBUST PLAYER!")
    chips.lose_bet()


def player_wins(chips):
    """player wins"""
    print("\nPLAYER WINS!")
    chips.win_bet()


def dealer_busts(chips):
    """player wins, dealer busted"""
    print("\nPLAYER WINS! DEALER BUSTED!")
    chips.win_bet()


def dealer_wins(chips):
    """Dealer Wins"""
    print("\nDEALER WINS!")
    chips.lose_bet()


def push():
    """Dealer and player tie."""
    print("\nDealer and player tie! PUSH")


if __name__ == "__main__":
    while True:
        print("WELCOME TO BLACKJACK")
        DECK = Deck()
        DECK.shuffle()
        PLAYER_HAND = Hand()
        PLAYER_HAND.add_card(DECK.deal())
        PLAYER_HAND.add_card(DECK.deal())

        DEALER_HAND = Hand()
        DEALER_HAND.add_card(DECK.deal())
        DEALER_HAND.add_card(DECK.deal())
        PLAYER_CHIPS = Chips()
        take_bet(PLAYER_CHIPS)
        show_some(PLAYER_HAND, DEALER_HAND)

        while PLAYING:
            PLAYING = hit_or_stand(DECK, PLAYER_HAND, PLAYING)
            show_some(PLAYER_HAND, DEALER_HAND)
            if PLAYER_HAND.value > 21:
                player_bust(PLAYER_CHIPS)
                break
        if PLAYER_HAND.value <= 21:
            while DEALER_HAND.value < 17:
                hit(DECK, DEALER_HAND)
            show_all(PLAYER_HAND, DEALER_HAND)
            if DEALER_HAND.value > 21:
                dealer_busts(PLAYER_CHIPS)
            elif DEALER_HAND.value > PLAYER_HAND.value:
                dealer_wins(PLAYER_CHIPS)
            elif DEALER_HAND.value < PLAYER_HAND.value:
                player_wins(PLAYER_CHIPS)
            else:
                push()

        print("\nPlayer total chips are at: {}".format(PLAYER_CHIPS.total))
        NEW_GAME = input("Would you like to play another hand? y/n: ")
        if NEW_GAME[0].lower() == 'y':
            PLAYING = True
            continue
        else:
            print('Thank you for playing!')
            break
