"""Checks the legality of a move."""
from typing import Optional

from whist.core.cards.card import Card
from whist.core.cards.hand import Hand


# pylint: disable=too-few-public-methods
class LegalChecker:
    """
    Static legal checker.
    """

    @staticmethod
    def check_legal(hand: Hand, card: Card, lead: Optional[Card]) -> bool:
        """
        Checks if move is legal.
        :param hand: of the current player
        :type hand: Hand
        :param card: the card which should be played next
        :type card: Card
        :param lead: the first played card, can be None if no card has been played
        :type lead: Card
        :return: True if legal else false
        :rtype: bool
        """
        first_card_played = lead is not None
        if not first_card_played:
            return True
        if card.suit == lead.suit:
            return True
        return not hand.contains_suit(lead.suit)
