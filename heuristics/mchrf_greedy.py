from math import ceil
from random import choice
from heapq import nlargest


def mchrf_greedy(facilities: list, towns: list, randomness: bool = False) -> bool:
    """
    The following function implement a greedy heuristic that open enough facility to manage the total amount of garbage
    produced by every city. The name of the greedy mhf stands for Minimum Capacity/Hazard Ratio Facility.
    -Best criteria: open first the facility that have the maximum capacity/hazard ratio
    -Ind criteria: every town must use a facility

    :param facilities: list of the problem instance's facilities
    :param towns: list of the problem instance's towns
    :param randomness: whether the greedy is random or not
    :return: bool representing success/failure
    """

    success = False

    # initial empty solution
    temp_facilities = facilities.copy()
    temp_towns = towns.copy()

    while True:
        # selection of facility that cause least total risk
        if randomness:
            k_facilities = nlargest(ceil(len(facilities) * 0.15), temp_facilities,
                                    key=lambda facility: facility.capacity/facility.total_hazard)
            current_facility = choice(k_facilities)
        else:
            current_facility = min(temp_facilities, key=lambda facility: facility.total_hazard)
        current_capacity = current_facility.capacity

        for temp_town in temp_towns:
            if temp_town.garbage <= current_capacity:
                # decreasing current facility capacity by the garbage produced by the town
                current_capacity -= temp_town.garbage
                # remove the current town from the temp towns list
                temp_towns.pop(temp_towns.index(temp_town))
                # assign the facility to the current town
                towns[towns.index(temp_town)].facility = current_facility

        if current_capacity < current_facility.capacity:
            # open the current facility
            facilities[facilities.index(current_facility)].is_open = True

        # remove current facility from temp facilities list
        temp_facilities.pop(temp_facilities.index(current_facility))

        # exit from loop if all towns have been assigned
        if not temp_towns:
            success = True
            break
        # exit from loop if there are no more facilities
        elif not temp_facilities:
            break

    return success
