"""Hand of whist"""

from whist.core.cards.deck import Deck
from whist.core.error.hand_error import HandAlreadyDealtError
from whist.core.game.play_order import PlayOrder
from whist.core.game.player_at_table import PlayerAtTable
from whist.core.game.trick import Trick
from whist.core.game.warnings import TrickNotDoneWarning
from whist.core.user.player import Player


class Hand:
    """
    Hand of whist.
    """

    def __init__(self, play_order: PlayOrder):
        self._tricks: list[Trick] = []
        self._current_play_order: PlayOrder = play_order
        self._trump = None

    @property
    def done(self) -> bool:
        """
        Check if the hand is done.
        :return: True if the hand is done, else False
        :rtype: bool
        """
        return len(self._tricks) == 13 and self._tricks[-1]

    @property
    def next_play_order(self) -> PlayOrder:
        """
        Returns the next order of player for next hand.
        :rtype: PlayOrder
        """
        return self._current_play_order.next_order()

    @property
    def current_trick(self):
        """
        Returns the current trick.
        """
        if len(self._tricks) == 0:
            self.deal()
        return self._tricks[-1]

    def deal(self) -> Trick:
        """
        Deals the hand and starts the first trick.
        :return: the first trick
        :rtype: Trick
        """
        if len(self._tricks) != 0:
            raise HandAlreadyDealtError()
        deck = Deck.full()
        while len(deck) > 0:
            player = self._current_play_order.next_player()
            card = deck.pop_random()
            if len(deck) == 1:
                self._trump = card.suit
            player.hand.add(card)
        if self._trump is None:
            raise ValueError
        first_trick = Trick(list(self._current_play_order), self._trump)
        self._tricks.append(first_trick)
        return first_trick

    def next_trick(self) -> Trick:
        """
        Starts the next trick.
        :return: the next trick
        :rtype: Trick
        """
        if not self._tricks[-1].done:
            raise TrickNotDoneWarning()
        self._winner_plays_first_card()
        next_trick = Trick(list(self._current_play_order), trump=self._trump)
        self._tricks.append(next_trick)
        return next_trick

    def get_player(self, player: Player) -> PlayerAtTable:
        """
        Retrieves the PlayerAtTable for the player given.
        :param player: who needs it's counterpart at the table
        :return: the player at table
        """
        return self._current_play_order.get_player(player)

    def _winner_plays_first_card(self):
        winner: PlayerAtTable = self._tricks[-1].winner
        self._current_play_order.rotate(winner)
