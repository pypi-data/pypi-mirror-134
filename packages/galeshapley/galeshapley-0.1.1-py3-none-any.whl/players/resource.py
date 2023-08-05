""" The Resource class for use in instances of SA. """

from .base_container import BaseContainer


class Resource(BaseContainer):
    """A class to represent a resource in an instance of SA.

    Parameters
    ----------
    name : object
        An identifier. This should be unique and descriptive.
    capacity : int
        The maximum number of matches the resource can have.

    Attributes
    ----------
    container : Container
        The container that runs the resource. Defaults to ``None``.
    prefs : list of Player
        The resource's preferences. Inherited from ``container``.
    pref_names : list
        A list of the names in ``prefs``. Updates with ``prefs`` via the
        ``container.set_prefs`` method.
    matching : list of Player
        The current matches of the resource. An empty list if currently
        unsubscribed.
    """

    def __init__(self, name, capacity):

        super().__init__(name, capacity)
        self.container = None

    def _forget(self, player):
        """Remove ``player`` from the preference list of the resource and its
        container."""

        if player in self.prefs:
            prefs = self.prefs[:]
            prefs.remove(player)
            self.prefs = prefs
            self.container._forget(player)

    def _match(self, player):
        """Match the resource to ``player``, and update the resource
        container's matching to include ``player``, too."""

        self.matching.append(player)
        self.matching.sort(key=self.prefs.index)
        self.container._match(player)

    def _unmatch(self, player):
        """Break the matching between the resource and ``player``, and the
        matching between ``player`` and the resource container."""

        matching = self.matching[:]
        matching.remove(player)
        self.matching = matching
        self.container._unmatch(player)

    def set_container(self, container):
        """Set the resource's container and add the resource to their list
        of active resources."""

        self.container = container
        if self not in container.resources:
            container.resources.append(self)
