def mhf_greedy(facilities: list, towns: list) -> bool:
    """
    The following function implement a greedy heuristic that open enough facility to manage the total amount of garbage
    produced by every city. The name of the greedy mhf stands for Minimum Hazard Facility.
    -Best criteria: open first the facility that have the minimum total risk (the sum of the hazard for every city)
    -Ind criteria: every town must use a facility and the total capacity (sum of the capacity of the opened facility)
                   must be higher than the total garbage (sum of the garbage of every town)

    :param facilities: list of facilities
    :param towns: list of towns
    :return: the lists that describe the opened/closed facility and the towns with the associated facility
    """

    success = False

    # initial empty solution
    temp_facilities = facilities.copy()
    temp_towns = towns.copy()

    while True:
        # selection of facility that cause least total risk
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
