"""DAO of session."""

from whist.core.error.table_error import TableFullError, TeamFullError, TableNotReadyError, \
    TableNotStartedError
from whist.core.game.rubber import Rubber
from whist.core.session.session import Session
from whist.core.user.player import Player


class Table(Session):
    """
    The game logics instance of a room to play Whist.
    """
    min_player: int
    max_player: int
    team_size: int = 2
    _started: bool = False
    _rubbers: list[Rubber] = []

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Configures the table class to allow private field. PrivateAttr cannot be used here as
        pylint does not detect the correct types in python 3.10.
        """
        underscore_attrs_are_private = True

    def __len__(self):
        """
        The amount of players joined.
        :return: # player
        :rtype: int
        """
        return len(self.users)

    @property
    def ready(self) -> bool:
        """
        Flag if the table is ready to start playing.
        :return Ready or not
        :rtype: boolean
        """
        return len(self.users) >= self.min_player and self.users.ready

    @property
    def started(self):
        """
        Flag if the current table has been started.
        :return: True if it has been started else False.
        """
        return self._started

    @property
    def current_rubber(self) -> Rubber:
        """
        Returns the current rubber
        :return: the latest rubber entry
        """
        if not self.started:
            raise TableNotStartedError()
        return self._rubbers[-1]

    def start(self) -> None:
        """
        Starts the table, but will check if every player is ready first.
        """
        if not self.ready:
            raise TableNotReadyError()

        self._rubbers.append(Rubber.create_random(num_teams=2, team_size=2, users=self.users))
        self._started = True

    def join(self, player: Player) -> None:
        """
        If a seat is available a player joins the table.
        :param player: who wants to join the table
        :type player: Player
        :return: None or raised an error if the table is already full.
        :rtype: None
        """
        if len(self.users) < self.max_player:
            self.users.append(player)
        else:
            raise TableFullError(f'Table with name: {self.name} is already full.')

    def leave(self, player: Player) -> None:
        """
        Remove a player from table.
        :param player: The player to remove.
        :type player: Player
        :return: None
        :rtype: None
        """
        self.users.remove(player)

    def join_team(self, player: Player, team: int) -> None:
        """
        Player joins a team.
        :param player: to join a team
        :type player: Player
        :param team: id of the new team
        :type team: int
        :return: None if successful or raises Error if team is full
        :rtype: None
        """
        if not self.users.is_joined(player):
            self.join(player)
        team_size = self.users.team_size(team)
        if team_size >= self.team_size:
            raise TeamFullError(f'Team with id: {team} is already full.')
        self.users.change_team(player, team)

    def player_ready(self, player) -> None:
        """
        Player says they is ready.
        :param player: player who is ready
        :type player: Player
        :return: None
        :rtype: None
        """
        self.users.player_ready(player)

    def player_unready(self, player) -> None:
        """
        Player says they is not ready.
        :param player: player who is not ready
        :type player: Player
        :return: None
        :rtype: None
        """
        self.users.player_unready(player)
