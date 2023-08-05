""" Functions for the SA algorithm. """

from .util import _delete_pair, _match_pair


def unmatch_pair(player, resource):
    """ Unmatch a player-resource pair. """

    player._unmatch()
    resource._unmatch(player)


def player_allocation(players, resources, containers, optimal="player"):
    """Solve an instance of SA by treating it as a bi-level HR. A unique,
    stable and optimal matching is found for the given set of players, resources
    and containers. The optimality of the matching is found with respect to one
    party and is subsequently the worst stable matching for the other.

    Parameters
    ----------
    players : list of Player
        The players in the game. Each player must rank a subset of the
        elements of ``resources``.
    resources : list of Resource
        The resources in the game. Each resource is offered by a container that
        governs its preferences.
    container : list of Container
        The containers in the game. Each container offers a unique subset of
        ``resources`` and ranks all the players that have ranked at least one of
        these resources.
    optimal : str, optional
        Which party the matching should be optimised for. Must be one of
        ``"player"`` and ``"container"``. Defaults to the former.

    Returns
    =======
    matching : Matching
        A dictionary-like object where the keys are the members of ``resources``
        and their player matches are the values.
    """

    if optimal == "player":
        return player_optimal(players, resources)
    if optimal == "container":
        return container_optimal(resources, containers)


def player_optimal(players, resources):
    """Solve the instance of SA to be player-optimal. The algorithm is as
    follows:

        0. Set all players to be unassigned, and every resource (and container)
        to be totally unsubscribed.

        1. Take any player, :math:`s`, that is unassigned and has a non-empty
        preference list, and consider their most preferred resource, :math:`p`.
        Let :math:`f` denote the container that offers :math:`p`. Assign
        :math:`s` to be matched to :math:`p` (and thus :math:`f`).

        2. If :math:`p` is now over-subscribed, find its worst current match,
        :math:`s'`. Unmatch :math:`p` and :math:`s'`. Else if :math:`f` is
        over-subscribed, find their worst current match, :math:`s''`, and the
        resource they are currently subscribed to, :math:`p'`. Unmatch :math:`p'`
        and :math:`s''`.

        3. If :math:`p` is now at capacity, find their worst current match,
        :math:`s'`. For each successor, :math:`t`, to :math:`s'` in the
        preference list of :math:`p`, delete the pair :math:`(p, t)` from the
        game.

        4. If :math:`f` is at capacity, find their worst current match,
        :math:`s'`. For each successor, :math:`t`, to :math:`s'` in the
        preference list of :math:`f`, for each resource, :math:`p'`, offered by
        :math:`f` that :math:`t` finds acceptable, delete the pair
        :math:`(p', t)` from the game.

        5. Go to 1 until there are no such players left, then end.
    """

    free_players = players[:]
    while free_players:

        player = free_players.pop()
        resource = player.get_favourite()
        container = resource.container

        _match_pair(player, resource)

        if len(resource.matching) > resource.capacity:
            worst = resource.get_worst_match()
            unmatch_pair(worst, resource)
            free_players.append(worst)

        elif len(container.matching) > container.capacity:
            worst = container.get_worst_match()
            worst_resource = worst.matching
            unmatch_pair(worst, worst_resource)
            free_players.append(worst)

        if len(resource.matching) == resource.capacity:
            successors = resource.get_successors()
            for successor in successors:
                _delete_pair(resource, successor)
                if not successor.prefs:
                    free_players.remove(successor)

        if len(container.matching) == container.capacity:
            successors = container.get_successors()
            for successor in successors:

                container_resources = [
                    resource
                    for resource in container.resources
                    if resource in successor.prefs
                ]

                for resource in container_resources:
                    _delete_pair(resource, successor)
                if not successor.prefs:
                    free_players.remove(successor)

    return {p: p.matching for p in resources}


def container_optimal(resources, containers):
    """Solve the instance of SA to be container-optimal. The algorithm is as
    follows:

        0. Set all players to be unassigned, and every resource (and container)
        to be totally unsubscribed.

        1. Take any container member, :math:`f`, that is under-subscribed and
        whose preference list contains at least one player that is not
        currently matched to at least one acceptable (though currently
        under-subscribed) resource offered by :math:`f`. Consider the
        container's most preferred such player, :math:`s`, and that player's
        most preferred such resource, :math:`p`.

        2. If :math:`s` is matched to some other resource, :math:`p'`, then
        unmatch them. In any case, match :math:`s` and :math:`p` (and thus
        :math:`f`).

        3. For each successor, :math:`p'`, to :math:`p` in the preference list
        of :math:`s`, delete the pair :math:`(p', s)` from the game.

        4. Go to 1 until there are no such containers, then end.
    """

    free_containers = containers[:]
    while free_containers:

        container = free_containers.pop()
        player, resource = container.get_favourite()

        if player.matching:
            curr_match = player.matching
            unmatch_pair(player, curr_match)

        _match_pair(player, resource)

        successors = player.get_successors()
        for successor in successors:
            _delete_pair(player, successor)

        free_containers = [
            container
            for container in containers
            if container.get_favourite() is not None
        ]

    return {p: p.matching for p in resources}
