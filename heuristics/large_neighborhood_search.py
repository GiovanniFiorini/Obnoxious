import random
from commons.town import get_town_with_max_hazard


def large_neighborhood_search(facilities: list, towns: list, hazards: list, max_iteration: int = 50, max_improvement: int = 10) -> tuple:
    """
    Implements a local search on the solution obtained by the greedy.
    This algorithm is inspired by the Large Neighborhood Search.

    :param facilities: list of the problem instance's facilities
    :param towns: list of the problem instance's towns
    :param hazards: matrix of hazards caused by each facilities to the corresponding town
    :param max_iteration: limits the number of iteration
    :param max_improvement: limits the number of the improvement
    :return: a tuple with the number of iteration performed and the number of improvements obtained
    """

    # counters
    max_attempts_per_swappable_facility = 10
    attempts_per_swappable_facility = 0
    improvements = 0
    iterations = 0

    # list of the opened facilities
    solutions = list(filter(lambda o_facility: o_facility.is_open, facilities.copy()))

    while True:

        # list of the closed facilities
        neighborhood = list(filter(lambda c_facility: not c_facility.is_open, facilities.copy()))

        # get the town with the maximum hazard perceived
        max_hazard_town, max_hazard = get_town_with_max_hazard(facilities, towns, hazards)

        # get a random opened facility to close
        swappable_facility = random.choice(solutions)

        while True:
            # get a random closed facility to test
            test_facility = random.choice(neighborhood)

            # check capacity constraint (ADMISSIBILITY)
            if test_facility.capacity >= swappable_facility.capacity:
                # destroy & repair the solution
                swappable_facility.is_open = False
                test_facility.is_open = True

                # calculate the new max hazard and the respective town
                new_max_hazard_town, new_max_hazard = get_town_with_max_hazard(facilities, towns, hazards)

                # check if the new max hazard is an improvement (SOLUTION)
                if new_max_hazard < max_hazard:
                    # reassign the chosen facility to the towns whose were associated with the swappable_facility
                    for town in towns:
                        if town.facility == swappable_facility:
                            town.facility = test_facility

                    # reset the attempts per town counter because now there is a new solution to iterate on
                    improvements += 1

                    # rebuild the solution
                    solutions = list(filter(lambda o_facility: o_facility.is_open, facilities.copy()))

                    # exit the loop because a solution was found
                    break

                else:
                    # restore of the current solution's data structures
                    swappable_facility.is_open = True
                    test_facility.is_open = False

                    # skip the chosen facility
                    neighborhood.pop(neighborhood.index(test_facility))

            else:
                # skip the chosen facility
                neighborhood.pop(neighborhood.index(test_facility))

            # increment the counter for swappable facility attempts to swap, then check the limit and maybe break
            attempts_per_swappable_facility += 1
            # forbid the current swappable facility to be taken in a count for the next iteration
            if len(neighborhood) == 0 or attempts_per_swappable_facility == max_attempts_per_swappable_facility:
                solutions.pop(solutions.index(swappable_facility))
                break

        # if there are no more facilities in solution to be taken in account, exit the loop
        if len(solutions) == 0:
            break

        # check the number of improvement
        if improvements == max_improvement:
            break

        iterations += 1
        # check the number of iteration
        if iterations == max_iteration:
            break

    return iterations, improvements
