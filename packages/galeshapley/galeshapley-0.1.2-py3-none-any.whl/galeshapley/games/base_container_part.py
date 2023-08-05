""" The HR game class and supporting functions. """
import copy
import warnings

from galeshapley import BaseGame, MultipleMatching
from galeshapley import Player as Part
from galeshapley.algorithms import base_container_part
from galeshapley.exceptions import (
    MatchingError,
    PlayerExcludedWarning,
    PreferencesChangedWarning,
)
from galeshapley.players import BaseContainer


class BaseContainerPart(BaseGame):
    """A class for solving instances of the base_container-part assignment
    problem (HR).

    In this case, a blocking pair is any part-base_container pair that satisfies
    **all** of the following:

        - They are present in each other's preference lists;
        - either the part is unmatched, or they prefer the base_container to their
          current match;
        - either the base_container is under-subscribed, or they prefer the part
          to at least one of their current matches.

    Parameters
    ----------
    parts : list of Player
        The parts in the matching game. Each part must rank a subset of
        those in :code:`base_containers`.
    base_containers : list of BaseContainer
        The base_containers in the matching game. Each base_container must rank all of (and
        only) the parts which rank it.
    clean : bool
        Indicator for whether the players of the game should be cleaned.
        Cleaning is reductive in nature, removing players from the game and/or
        other player's preferences if they do not meet the requirements of the
        game.

    Attributes
    ----------
    matching : Matching or None
        Once the game is solved, a matching is available as a :code:`Matching`
        object with the base_containers as keys and their part matches as values.
        Initialises as :code:`None`.
    blocking_pairs : list of (Player, BaseContainer) or None
        Initialises as `None`. Otherwise, a list of the part-base_container
        blocking pairs.
    """

    def __init__(self, parts, base_containers, clean=False):

        parts, base_containers = copy.deepcopy([parts, base_containers])
        self.parts = parts
        self.base_containers = base_containers
        self.clean = clean

        self._all_parts = parts
        self._all_base_containers = base_containers

        super().__init__(clean)
        self.check_inputs()

    @classmethod
    def create_from_dictionaries(
        cls, part_prefs, base_container_prefs, capacities, clean=False
    ):
        """Create an instance of :code:`BaseContainerPart` from two preference
        dictionaries and capacities. If :code:`clean=True` then remove players
        from the game and/or player preferences if they do not satisfy the
        conditions of the game."""

        parts, base_containers = _make_players(
            part_prefs, base_container_prefs, capacities
        )
        game = cls(parts, base_containers, clean)

        return game

    def solve(self, optimal="part"):
        """Solve the instance of HR using either the part- or
        base_container-oriented algorithm. Return the galeshapley."""

        self.matching = MultipleMatching(
            base_container_part(self.parts, self.base_containers, optimal)
        )
        return self.matching

    def check_validity(self):
        """ Check whether the current matching is valid. """

        unacceptable_issues = self._check_for_unacceptable_matches(
            "parts"
        ) + self._check_for_unacceptable_matches("base_containers")

        oversubscribed_issues = self._check_for_oversubscribed_players(
            "base_containers"
        )

        if unacceptable_issues or oversubscribed_issues:
            raise MatchingError(
                unacceptable_matches=unacceptable_issues,
                oversubscribed_base_containers=oversubscribed_issues,
            )

        return True

    def _check_for_unacceptable_matches(self, party):
        """Check that no player in `party` is matched to an unacceptable
        player."""

        issues = []
        for player in vars(self)[party]:
            issue = player.check_if_match_is_unacceptable(unmatched_okay=True)
            if isinstance(issue, list):
                issues.extend(issue)
            elif isinstance(issue, str):
                issues.append(issue)

        return issues

    def _check_for_oversubscribed_players(self, party):
        """ Check that no player in `party` is oversubscribed. """

        issues = []
        for player in vars(self)[party]:
            issue = player.check_if_oversubscribed()
            if issue:
                issues.append(issue)

        return issues

    def check_stability(self):
        """Check for the existence of any blocking pairs in the current
        matching, thus determining the stability of the galeshapley."""

        blocking_pairs = []
        for part in self.parts:
            for base_container in self.base_containers:
                if (
                    _check_mutual_preference(part, base_container)
                    and _check_part_unhappy(part, base_container)
                    and _check_base_container_unhappy(part, base_container)
                ):
                    blocking_pairs.append((part, base_container))

        self.blocking_pairs = blocking_pairs
        return not any(blocking_pairs)

    def check_inputs(self):
        """Give out warnings if any of the conditions of the game have been
        broken. If the :code:`clean` attribute is :code:`True`, then remove any
        such situations from the game."""

        self._check_inputs_player_prefs_unique("parts")
        self._check_inputs_player_prefs_unique("base_containers")

        self._check_inputs_player_prefs_all_in_party("parts", "base_containers")
        self._check_inputs_player_prefs_all_in_party("base_containers", "parts")

        self._check_inputs_player_prefs_all_reciprocated("base_containers")
        self._check_inputs_player_reciprocated_all_prefs(
            "base_containers", "parts"
        )

        self._check_inputs_player_prefs_nonempty("parts", "base_containers")
        self._check_inputs_player_prefs_nonempty("base_containers", "parts")

        self._check_inputs_player_capacity("base_containers", "parts")

    def _check_inputs_player_prefs_all_reciprocated(self, party):
        """Make sure that each player in :code:`party` has ranked only those
        players that have ranked it."""

        for player in vars(self)[party]:

            for other in player.prefs:
                if player not in other.prefs:
                    warnings.warn(
                        PreferencesChangedWarning(
                            f"{player} ranked {other} but they did not."
                        )
                    )
                    if self.clean:
                        player._forget(other)

    def _check_inputs_player_reciprocated_all_prefs(self, party, other_party):
        """Make sure that each player in :code:`party` has ranked all those
        players in :code:`other_party` that have ranked it."""

        players = vars(self)[party]
        others = vars(self)[other_party]
        for player in players:

            others_that_ranked = [
                other for other in others if player in other.prefs
            ]
            for other in others_that_ranked:
                if other not in player.prefs:
                    warnings.warn(
                        PreferencesChangedWarning(
                            f"{other} ranked {player} but they did not."
                        )
                    )
                    if self.clean:
                        other._forget(player)

    def _check_inputs_player_capacity(self, party, other_party):
        """Check that each player in :code:`party` has a capacity of at least
        one. If the :code:`clean` attribute is :code:`True`, remove any base_container
        that does not have such a capacity from the game."""

        for player in vars(self)[party]:
            if player.capacity < 1:
                warnings.warn(PlayerExcludedWarning(player))

                if self.clean:
                    self._remove_player(player, party, other_party)


def _check_mutual_preference(part, base_container):
    """ Determine whether two players each have a preference of the other. """

    return part in base_container.prefs and base_container in part.prefs


def _check_part_unhappy(part, base_container):
    """Determine whether a part is unhappy because they are unmatched, or
    they prefer the base_container to their current match."""

    return part.matching is None or part.prefers(
        base_container, part.matching
    )


def _check_base_container_unhappy(part, base_container):
    """Determine whether a base_container is unhappy because they are
    under-subscribed, or they prefer the part to at least one of their
    current matches."""

    return len(base_container.matching) < base_container.capacity or any(
        [base_container.prefers(part, match) for match in base_container.matching]
    )


def _make_players(part_prefs, base_container_prefs, capacities):
    """Make a set of parts and base_containers from the dictionaries given, and
    add their preferences."""

    part_dict, base_container_dict = _make_instances(
        part_prefs, base_container_prefs, capacities
    )

    for part_name, part in part_dict.items():
        prefs = [base_container_dict[name] for name in part_prefs[part_name]]
        part.set_prefs(prefs)

    for base_container_name, base_container in base_container_dict.items():
        prefs = [part_dict[name] for name in base_container_prefs[base_container_name]]
        base_container.set_prefs(prefs)

    parts = list(part_dict.values())
    base_containers = list(base_container_dict.values())

    return parts, base_containers


def _make_instances(part_prefs, base_container_prefs, capacities):
    """Create ``Player`` (part) and ``BaseContainer`` instances for the names in
    each dictionary."""

    part_dict, base_container_dict = {}, {}
    for part_name in part_prefs:
        part = Part(name=part_name)
        part_dict[part_name] = part
    for base_container_name in base_container_prefs:
        capacity = capacities[base_container_name]
        base_container = BaseContainer(name=base_container_name, capacity=capacity)
        base_container_dict[base_container_name] = base_container

    return part_dict, base_container_dict
