""" The SA game class and supporting functions. """
import copy
import warnings

from galeshapley import MultipleMatching
from galeshapley import Player as Player
from galeshapley.algorithms import player_allocation
from galeshapley.exceptions import (
    CapacityChangedWarning,
    MatchingError,
    PreferencesChangedWarning,
)
from galeshapley.games import BaseContainerPart
from galeshapley.players import Resource, Container


class PlayerAllocation(BaseContainerPart):
    """A class for solving instances of the player-allocation problem (SA)
    using an adapted Gale-Shapley algorithm.

    In this case, a blocking pair is defined as any player-resource pair that
    satisfies **all** of the following:

    1. The player has a preference of the resource.
    2. Either the player is unmatched, or they prefer the resource to their
       current resource.
    3. At least one of the following:

       - The resource or its container is under-subscribed.
       - The resource is under-subscribed and the container is at capacity, and
         the player is matched to a resource offered by the container or the
         container prefers the player to its worst currently matched player.
       - The resource is at capacity and its container prefers the player to
         its worst currently matched player.

    Parameters
    ----------
    players : list of Player
        The players in the game. Each player must rank a subset of the
        resources.
    resources : list of Resource
        The resources in the game. Each resource has a container associated
        with it that governs its preferences.
    containers : list of Container
        The containers in the game. Each container oversees a unique subset
        of ``resources`` and ranks all of those players that have ranked at
        least one of its resources.
    clean : bool
        An indicator as to whether the players passed to the game should be
        cleaned in a reductive fashion. Defaults to :code:`False`.

    Attributes
    ----------
    matching : Matching or None
        Once the game is solved, a matching is available. This ``Matching``
        object behaves much like a dictionary that uses the elements of
        ``resources`` as keys and their player matches as values. Initialises as
        ``None``.
    blocking_pairs : list of (Player, Resource)
        Initialises as None. Otherwise, a list of the player-resource blocking
        pairs.
    """

    def __init__(self, players, resources, containers, clean=False):
        
        players, resources, containers = copy.deepcopy(
            [players, resources, containers]
        )
        self.players = players
        self.resources = resources
        self.containers = containers

        self._all_players = players
        self._all_resources = resources
        self._all_containers = containers

        self.clean = clean

        super().__init__(players, resources, clean)
        self.check_inputs()

    def _remove_player(self, player, player_party, other_party=None):
        """Remove players from the game normally unless the player is a
        container."""

        if player_party == "containers":
            self.containers.remove(player)
            for resource in player.resources:
                try:
                    super()._remove_player(resource, "resources", "players")
                except ValueError:
                    pass

        else:
            super()._remove_player(player, player_party, other_party)

    @classmethod
    def create_from_dictionaries(
        cls,
        player_prefs,
        container_prefs,
        resource_containers,
        resource_capacities,
        container_capacities,
        clean=False,
    ):
        """Create an instance of SA from two preference dictionaries,
        affiliations and capacities."""

        players, resources, containers = _make_players(
            player_prefs,
            container_prefs,
            resource_containers,
            resource_capacities,
            container_capacities,
        )
        game = cls(players, resources, containers, clean)

        return game

    def solve(self, optimal="player"):
        """Solve the instance of SA using either the player- or
        container-optimal algorithm."""

        self.matching = MultipleMatching(
            player_allocation(
                self.players, self.resources, self.containers, optimal
            )
        )
        return self.matching

    def check_validity(self):
        """Check whether the current matching is valid. Raise a `MatchingError`
        detailing the issues if not."""

        unacceptable_issues = (
            self._check_for_unacceptable_matches("players")
            + self._check_for_unacceptable_matches("resources")
            + self._check_for_unacceptable_matches("containers")
        )

        oversubscribed_issues = self._check_for_oversubscribed_players(
            "resources"
        ) + self._check_for_oversubscribed_players("containers")

        if unacceptable_issues or oversubscribed_issues:
            raise MatchingError(
                unacceptable_matches=unacceptable_issues,
                oversubscribed_players=oversubscribed_issues,
            )

        return True

    def check_stability(self):
        """Check for the existence of any blocking pairs in the current
        matching, thus determining the stability of the galeshapley."""

        blocking_pairs = []
        for player in self.players:
            for resource in self.resources:
                if (
                    resource in player.prefs
                    and _check_player_unhappy(player, resource)
                    and _check_resource_unhappy(resource, player)
                ):
                    blocking_pairs.append((player, resource))

        self.blocking_pairs = blocking_pairs
        return not any(blocking_pairs)

    def check_inputs(self):
        """Give out warnings if any of the conditions of the game have been
        broken. If the :code:`clean` attribute is :code:`True`, then remove any
        such situations from the game."""

        self._check_inputs_player_prefs_unique("players")
        self._check_inputs_player_prefs_unique("resources")
        self._check_inputs_player_prefs_unique("containers")

        self._check_inputs_player_prefs_all_in_party("players", "resources")
        self._check_inputs_player_prefs_nonempty("players", "resources")

        self._check_inputs_player_prefs_all_in_party("containers", "players")
        self._check_inputs_player_prefs_nonempty("containers", "players")

        self._check_inputs_player_prefs_all_reciprocated("resources")
        self._check_inputs_player_reciprocated_all_prefs("resources", "players")
        self._check_inputs_player_prefs_nonempty("resources", "players")

        self._check_inputs_player_prefs_all_reciprocated("containers")
        self._check_inputs_player_reciprocated_all_prefs(
            "containers", "players"
        )
        self._check_inputs_player_prefs_nonempty("containers", "players")

        self._check_inputs_player_capacity("resources", "players")
        self._check_inputs_player_capacity("containers", "players")
        self._check_inputs_container_capacities_sufficient()
        self._check_inputs_container_capacities_necessary()

    def _check_inputs_player_prefs_all_reciprocated(self, party):
        """Check that each player in :code:`party` has ranked only those
        players that have ranked it, directly or via a resource."""

        if party == "containers":
            for container in self.containers:
                for player in container.prefs:
                    player_prefs_containers = {
                        p.container for p in player.prefs
                    }
                    if container not in player_prefs_containers:
                        warnings.warn(
                            PreferencesChangedWarning(
                                f"{container} ranked {player} but they did "
                                "not rank any of their resources."
                            )
                        )

                        if self.clean:
                            for resource in container.resources:
                                resource._forget(player)

        else:
            super()._check_inputs_player_prefs_all_reciprocated(party)

    def _check_inputs_player_reciprocated_all_prefs(self, party, other_party):
        """Check that each player in :code:`party` has ranked all those players
        in :code:`other_party` that ranked it, directly or via a resource."""

        if party == "containers":
            for container in self.containers:

                players_that_ranked = [
                    player
                    for player in self.players
                    if any(
                        resource in player.prefs
                        for resource in container.resources
                    )
                ]

                for player in players_that_ranked:
                    if player not in container.prefs:
                        warnings.warn(
                            PreferencesChangedWarning(
                                f"{player} ranked a resource provided by "
                                f"{container} but they did not."
                            )
                        )

                        if self.clean:
                            for resource in set(container.resources) & set(
                                player.prefs
                            ):
                                player._forget(resource)

        else:
            super()._check_inputs_player_reciprocated_all_prefs(
                party, other_party
            )

    def _check_inputs_container_capacities_sufficient(self):
        """Check that each container has the capacity to support its largest
        resource(s)."""

        for container in self.containers:

            for resource in container.resources:
                if resource.capacity > container.capacity:
                    warnings.warn(
                        CapacityChangedWarning(
                            f"{resource} has a capacity of {resource.capacity} "
                            "but its container has a capacity of "
                            f"{container.capacity}."
                        )
                    )

                    if self.clean:
                        resource.capacity = container.capacity

    def _check_inputs_container_capacities_necessary(self):
        """Check that each container has at most the necessary capacity for
        all of their resources."""

        for container in self.containers:

            total_resource_capacity = sum(
                p.capacity for p in container.resources
            )

            if container.capacity > total_resource_capacity:
                warnings.warn(
                    CapacityChangedWarning(
                        f"{container} has a capacity of {container.capacity} "
                        "but their resources have a capacity of "
                        f"{total_resource_capacity}"
                    )
                )

                if self.clean:
                    container.capacity = total_resource_capacity


def _check_player_unhappy(player, resource):
    """Determine whether ``player`` is unhappy either because they are
    unmatched or because they prefer ``resource`` to their current galeshapley."""

    return player.matching is None or player.prefers(
        resource, player.matching
    )


def _check_resource_unhappy(resource, player):
    """Determine whether ``resource`` is unhappy because either:
    - they and their container are under-subscribed;
    - they are under-subscribed, their container is full, and either
      ``player`` is in the container's matching or the container prefers
      ``player`` to their worst current matching;
    - ``resource`` is full and their container prefers ``player`` to the
      worst player in the matching of ``resource``.
    """

    container = resource.container

    resource_undersubscribed = len(resource.matching) < resource.capacity
    both_undersubscribed = (
        resource_undersubscribed
        and len(container.matching) < container.capacity
    )

    container_full = len(container.matching) == container.capacity

    swap_available = (
        player in container.matching and player.matching != resource
    ) or container.prefers(player, container.get_worst_match())

    resource_upsetting_container = len(
        resource.matching
    ) == resource.capacity and container.prefers(
        player, resource.get_worst_match()
    )

    return (
        both_undersubscribed
        or (resource_undersubscribed and container_full and swap_available)
        or resource_upsetting_container
    )


def _make_players(
    player_prefs,
    container_prefs,
    resource_containers,
    resource_capacities,
    container_capacities,
):
    """Make a set of ``Player``, ``Resource`` and ``Container`` instances,
    respectively for the players, resources and containers from the
    dictionaries given, and add their preferences."""

    player_dict, resource_dict, container_dict = _make_instances(
        player_prefs,
        resource_containers,
        resource_capacities,
        container_capacities,
    )

    for name, player in player_dict.items():
        prefs = [resource_dict[resource] for resource in player_prefs[name]]
        player.set_prefs(prefs)

    for name, container in container_dict.items():
        prefs = [player_dict[player] for player in container_prefs[name]]
        container.set_prefs(prefs)

    players = list(player_dict.values())
    resources = list(resource_dict.values())
    containers = list(container_dict.values())

    return players, resources, containers


def _make_instances(
    player_prefs,
    resource_containers,
    resource_capacities,
    container_capacities,
):
    """Create ``Player``, ``Resource`` and ``Container`` instances for the
    names in each dictionary."""

    player_dict, resource_dict, container_dict = {}, {}, {}

    for player_name in player_prefs:
        player = Player(name=player_name)
        player_dict[player_name] = player

    for resource_name, container_name in resource_containers.items():
        capacity = resource_capacities[resource_name]
        resource = Resource(name=resource_name, capacity=capacity)
        resource_dict[resource_name] = resource

    for container_name, capacity in container_capacities.items():
        container = Container(name=container_name, capacity=capacity)
        container_dict[container_name] = container

    for resource_name, container_name in resource_containers.items():
        resource = resource_dict[resource_name]
        container = container_dict[container_name]
        resource.set_container(container)

    return player_dict, resource_dict, container_dict
