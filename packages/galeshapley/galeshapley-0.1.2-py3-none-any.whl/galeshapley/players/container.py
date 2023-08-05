""" The container class for instances of SA. """

from .base_container import BaseContainer


class Container(BaseContainer):
    """A class to represent a container in an instance of SA.

    Parameters
    ----------
    name : object
        An identifier. This should be unique and descriptive.
    capacity : int
        The maximum number of matches the container can have.

    Attributes
    ----------
    resources : list of Resource
        The resources that the container runs. Defaults to an empty list.
    prefs : list of Player
        The container's preferences. Defaults to ``None`` and is updated via
        the ``set_prefs`` method.
    pref_names : list
        A list of the names in ``prefs``. Updates with ``prefs`` via
        ``set_prefs``.
    matching : list of Player
        The current matches of the container. An empty list if currently
        unsubscribed, and updated through its resources' matching updates.
    """

    def __init__(self, name, capacity):

        super().__init__(name, capacity)
        self.resources = []

    def _forget(self, player):
        """Only forget ``player`` if it is not ranked by any of the
        container's resources."""

        if player in self.prefs and not any(
            [player in resource.prefs for resource in self.resources]
        ):
            prefs = self.prefs[:]
            prefs.remove(player)
            self.prefs = prefs

    def set_prefs(self, players):
        """Set the preference of the container, and pass those on to its
        resources."""

        self.prefs = players
        self._pref_names = [player.name for player in players]
        self._original_prefs = players[:]

        for resource in self.resources:
            acceptable = [
                player for player in players if resource in player.prefs
            ]
            resource.set_prefs(acceptable)

    def get_favourite(self):
        """Find the container's favourite player that it is not currently
        matched to, but has a preference of, one of the container's
        under-subscribed resources. Also return the player's favourite
        under-subscribed resource. If no such player exists, return ``None``.
        """

        if len(self.matching) < self.capacity:
            for player in self.prefs:
                for resource in player.prefs:
                    if (
                        resource.container == self
                        and player not in resource.matching
                        and len(resource.matching) < resource.capacity
                    ):
                        return player, resource

        return None
