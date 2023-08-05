""" Functions for the HR algorithms. """

from .util import _delete_pair, _match_pair


def _unmatch_pair(part, base_container):
    """ Unmatch a (part, base_container)-pair. """

    part._unmatch()
    base_container._unmatch(part)


def _check_available(base_container):
    """ Check whether a base_container is willing and able to take an applicant. """

    return len(base_container.matching) < base_container.capacity and set(
        base_container.prefs
    ).difference(base_container.matching)


def base_container_part(parts, base_containers, optimal="part"):
    """Solve an instance of HR using an adapted Gale-Shapley algorithm
    :cite:`Rot84`. A unique, stable and optimal matching is found for the given
    set of parts and base_containers. The optimality of the matching is found with
    respect to one party and is subsequently the worst stable matching for the
    other.

    Parameters
    ----------
    parts : list of Player
        The parts in the game. Each part must rank a non-empty subset
        of the elements of ``base_containers``.
    base_containers : list of BaseContainer
        The base_containers in the game. Each base_container must rank all the parts
        that have ranked them.
    optimal : str, optional
        Which party the matching should be optimised for. Must be one of
        ``"part"`` and ``"base_container"``. Defaults to the former.

    Returns
    -------
    matching : Matching
        A dictionary-like object where the keys are the members of
        ``base_containers``, and the values are their matches ranked by preference.
    """

    if optimal == "part":
        return part_optimal(parts, base_containers)
    if optimal == "base_container":
        return base_container_optimal(base_containers)


def part_optimal(parts, base_containers):
    """Solve the instance of HR to be part-optimal. The algorithm is as
    follows:

        0. Set all parts to be unmatched, and all base_containers to be totally
        unsubscribed.

        1. Take any unmatched part with a non-empty preference list,
        :math:`r`, and consider their most preferred base_container, :math:`h`. Match
        them to one another.

        2. If, as a result of this new matching, :math:`h` is now
        over-subscribed, find the worst part currently assigned to
        :math:`h`, :math:`r'`. Set :math:`r'` to be unmatched and remove them
        from :math:`h`'s galeshapley. Otherwise, go to 3.

        3. If :math:`h` is at capacity (fully subscribed) then find their worst
        current match :math:`r'`. Then, for each successor, :math:`s`, to
        :math:`r'` in the preference list of :math:`h`, delete the pair
        :math:`(s, h)` from the game. Otherwise, go to 4.

        4. Go to 1 until there are no such parts left, then end.
    """

    free_parts = parts[:]
    while free_parts:

        part = free_parts.pop()
        base_container = part.get_favourite()

        if len(base_container.matching) == base_container.capacity:
            worst = base_container.get_worst_match()
            _unmatch_pair(worst, base_container)
            free_parts.append(worst)

        _match_pair(part, base_container)

        if len(base_container.matching) == base_container.capacity:
            successors = base_container.get_successors()
            for successor in successors:
                _delete_pair(base_container, successor)
                if not successor.prefs:
                    free_parts.remove(successor)

    return {r: r.matching for r in base_containers}


def base_container_optimal(base_containers):
    """Solve the instance of HR to be base_container-optimal. The algorithm is as
    follows:

        0. Set all parts to be unmatched, and all base_containers to be totally
        unsubscribed.

        1. Take any base_container, :math:`h`, that is under-subscribed and whose
        preference list contains any part they are not currently assigned
        to, and consider their most preferred such part, :math:`r`.

        2. If :math:`r` is currently matched, say to :math:`h'`, then unmatch
        them from one another. In any case, match :math:`r` to :math:`h` and go
        to 3.

        3. For each successor, :math:`s`, to :math:`h` in the preference list of
        :math:`r`, delete the pair :math:`(r, s)` from the game.

        4. Go to 1 until there are no such base_containers left, then end.
    """

    free_base_containers = base_containers[:]
    while free_base_containers:

        base_container = free_base_containers.pop()
        part = base_container.get_favourite()

        if part.matching:
            current_match = part.matching
            _unmatch_pair(part, current_match)
            if current_match not in free_base_containers:
                free_base_containers.append(current_match)

        _match_pair(part, base_container)
        if _check_available(base_container):
            free_base_containers.append(base_container)

        successors = part.get_successors()
        for successor in successors:
            _delete_pair(part, successor)
            if not _check_available(successor) and successor in free_base_containers:
                free_base_containers.remove(successor)

    return {r: r.matching for r in base_containers}
