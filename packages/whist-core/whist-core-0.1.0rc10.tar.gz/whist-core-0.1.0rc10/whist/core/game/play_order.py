"""Ring buffer of players at the table."""
from typing import Optional

from whist.core.cards.card_container import UnorderedCardContainer
from whist.core.game.player_at_table import PlayerAtTable
from whist.core.scoring.team import Team
from whist.core.user.player import Player


class PlayOrder:
    """
    Iterates over the players at the table.
    """

    def __init__(self, teams: list[Team]):
        self._size = len(teams) * len(teams[0].players)
        self._next_player = 0
        self._play_order: list[Optional[PlayerAtTable]] = [None] * self._size
        for team_index, team in enumerate(teams):
            for player_index, player in enumerate(team.players):
                player_index = team_index + player_index * len(teams)
                self._play_order[player_index] = PlayerAtTable(
                    player,
                    UnorderedCardContainer.empty()
                )

    def __iter__(self):
        return iter(self._play_order)

    def __eq__(self, other):
        if not isinstance(other, PlayOrder):
            return False
        return self._play_order == other._play_order

    def rotate(self, player: PlayerAtTable) -> None:
        """
        Rotates the play order, so the player will be next player.
        :param player: who should be at beginning of the play order
        :return: None
        """
        order = list(self)
        rotation: int = order.index(player)
        self._next_player = rotation

    def next_order(self) -> 'PlayOrder':
        """
        Create the order for the next hand.
        :rtype: PlayOrder
        """
        return PlayOrder._new_order(self)

    def next_player(self) -> PlayerAtTable:
        """
        Retrieves the next player who's turn it is.
        :rtype: PlayOrder
        """
        player: PlayerAtTable = self._play_order[self._next_player]
        self._next_player = (self._next_player + 1) % self._size
        return player

    def get_player(self, player: Player) -> PlayerAtTable:
        """
        Retrieves the PlayerAtTable for the player given.
        :param player: who needs it's counterpart at the table
        :return: the player at table
        """
        return [table_player for table_player in self._play_order
                if table_player.player == player][0]

    # pylint: disable=protected-access
    @classmethod
    def _new_order(cls, old_order: 'PlayOrder'):
        instance = cls.__new__(cls)
        instance._play_order = old_order._play_order[1:] + old_order._play_order[:1]
        instance._size = len(instance._play_order)
        instance._next_player = 0
        return instance
