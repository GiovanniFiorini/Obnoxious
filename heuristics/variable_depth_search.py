import random
import math
from typing import Optional
from entity.facility import Facility
from commons.facility import facility_with_max_hazard_per_town
from commons.town import get_town_with_max_hazard


def variable_depth_search(facilities: list, towns: list, hazards: list, max_iteration: int = 50, max_improvement: int = 10) -> tuple:
    """
    Implements a local search on the solution obtained by the greedy.
    This algorithm is inspired by the Variable Depth Search.

    :param facilities: list of the problem instance's facilities
    :param towns: list of the problem instance's towns
    :param hazards: matrix of hazards caused by each facilities to the corresponding town
    :param max_iteration: limits the number of iteration
    :param max_improvement: limits the number of the improvement
    :return: a tuple with the number of iteration performed and the number of improvements obtained
    """

    attempts_per_town = 0
    improvements = 0
    iterations = 0

    best_facility = None
    best_max_hazard = 0

    # list of the opened facilities
    solutions = list(filter(lambda o_facility: o_facility.is_open, facilities.copy()))
    # list of the closed facilities
    neighborhood = list(filter(lambda c_facility: not c_facility.is_open, facilities.copy()))

    # calculate the max depth for the algorithm
    depth = math.floor(len(neighborhood) * 0.85)

    while True:
        # get the town with the maximum hazard perceived
        max_hazard_town, max_hazard = get_town_with_max_hazard(facilities, towns, hazards)

        # search the facility that cause maximum hazard to the town suffering the maximum total hazard
        swappable_facility = facility_with_max_hazard_per_town(solutions, max_hazard_town.town_id, hazards)
        # swappable_facility = random.choice(solutions)

        while attempts_per_town < depth and len(neighborhood) != 0:

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
                    best_facility, best_max_hazard = bookmark(best_facility, best_max_hazard, test_facility, new_max_hazard)
                    # invert destroy & repair the solution
                    swappable_facility.is_open = True
                    test_facility.is_open = False

                    improvements += 1
                    attempts_per_town += 1
                    neighborhood.pop(neighborhood.index(test_facility))

                else:
                    # invert destroy & repair the solution
                    swappable_facility.is_open = True
                    test_facility.is_open = False
                    attempts_per_town += 1
                    neighborhood.pop(neighborhood.index(test_facility))

            else:
                attempts_per_town += 1
                neighborhood.pop(neighborhood.index(test_facility))

        if best_facility and best_max_hazard < max_hazard:
            # APPLY SOLUTION
            best_facility.is_open = True
            swappable_facility.is_open = False
            # reassign the chosen facility to the towns whose were associated with the swappable_facility
            for town in towns:
                if town.facility == swappable_facility:
                    town.facility = best_facility
            # rebuild the solution, avoiding the inverted move
            solutions = list(filter(lambda o_facility: o_facility.is_open, facilities.copy()))
            neighborhood = list(filter(lambda c_facility: not c_facility.is_open, facilities.copy()))
            neighborhood.pop(neighborhood.index(swappable_facility))
        else:
            break

        # check the number of improvement
        if improvements == max_improvement:
            break

        iterations += 1
        # check the number of iteration
        if iterations == max_iteration:
            break

    return iterations, improvements


def bookmark(best_facility: Optional[Facility], best_hazard: int, new_facility: Facility, new_hazard: int) -> tuple:
    """
    Update if necessary the best facility and the best hazard

    :param best_facility: the previous facility that minimize the total hazard for the town with total hazard
    :param best_hazard: total hazard in the solution with best_facility
    :param new_facility: the new facility that minimize the total hazard for the town with total hazard
    :param new_hazard: the new total hazard in the solution with best_facility
    :return: the current best facility and best hazard
    """

    if best_hazard == 0 and not best_facility:
        return new_facility, new_hazard

    if new_hazard < best_hazard:
        return new_facility, new_hazard
    else:
        return best_facility, best_hazard
