"""Testing Script"""
import unittest
import cap
import blackjack


class TestCap(unittest.TestCase):
    """Test cases for capital first letter word"""

    def test_one_word(self):
        """test whether the first letter is capitalised or not"""
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        """for multiple words, check if first letter is capitalized"""
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')


class TestBlackjack(unittest.TestCase):
    """Test for the blackjack script"""
    def test_suits_ranks_values(self):
        """Check if card details are correct"""
        suit = ('Hearts', 'Diamond', 'Spades', 'Clubs')
        self.assertCountEqual(blackjack.SUITS, suit)
        rank = ('Two', 'Three', 'Four', 'Five',
                'Six', 'Seven', 'Eight', 'Nine',
                'Ten', 'Jack', 'Queen', 'King', 'Ace')
        self.assertCountEqual(blackjack.RANKS, rank)
        value = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,
                 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
                 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
        self.assertCountEqual(blackjack.VALUES, value)

    def test_card(self):
        """Check the Card class"""
        card = blackjack.Card("a", "b")
        self.assertEqual(card.suit, 'a')
        self.assertEqual(card.rank, 'b')
        self.assertEqual(str(card), 'b of a')

    def test_deck(self):
        """Check the deck class"""
        deck = blackjack.Deck()
        deck_2 = blackjack.Deck()
        deck_2.shuffle()

        self.assertIn("The deck has: ", str(deck))
        self.assertNotEqual(deck, deck_2)
        self.assertIn(" of ", str(deck.deal()))
        return deck_2

    def test_hand(self):
        """Check the hand class"""
        hand = blackjack.Hand()
        self.assertEqual(hand.cards, [])
        self.assertEqual(hand.value, 0)
        self.assertEqual(hand.aces, 0)
        deck = self.test_deck()
        pull_card = deck.deal()
        hand.add_card(pull_card)
        self.assertNotEqual(hand.cards, [])

    def test_chips(self):
        """Check the Chips class"""
        chip = blackjack.Chips()
        chip.bet = 10
        self.assertEqual(chip.total, 100)
        chip.win_bet()
        self.assertEqual(chip.total, 110)
        chip.lose_bet()
        self.assertEqual(chip.total, 100)
        self.assertEqual(chip.bet, 10)
        return chip

    def test_functions(self):
        """Check all the function"""
        chip = self.test_chips()
        chip.bet = 200
        self.assertTrue(chip.bet > chip.total)

        decks = self.test_deck()
        player_hand = blackjack.Hand()
        player_hand.add_card(decks.deal())
        player_hand.add_card(decks.deal())
        dealer_hand = blackjack.Hand()
        dealer_hand.add_card(decks.deal())
        dealer_hand.add_card(decks.deal())
        blackjack.show_some(player_hand, dealer_hand)

        self.assertTrue(len(player_hand.cards) == 2)
        self.assertTrue(len(dealer_hand.cards) == 2)
        self.assertTrue(player_hand.value > 0)
        self.assertTrue(dealer_hand.value > 0)


if __name__ == '__main__':
    unittest.main()
