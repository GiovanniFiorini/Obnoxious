from commons.facility import least_total_hazard_facility
from commons.town import assign_facility_to_town


def mhf_greedy(facilities: list, towns: list, hazards: list) -> tuple:
    """
    The following function implement a greedy heuristic that open enough facility to manage the total amount of garbage
    produced by every city. The name of the greedy mhf stands for Minimum Hazard Facility.
    -Best criteria: open first the facility that have the minimum total risk (the sum of the hazard for every city)
    -Ind criteria: every town must use a facility and the total capacity (sum of the capacity of the opened facility)
                   must be higher than the total garbage (sum of the garbage of every town)

    :param facilities: list of facilities
    :param towns: list of towns
    :param hazards: list of list, describe every hazard for the couple (town,facility)
    :return: the lists that describe the opened/closed facility and the towns with the associated facility
    """
    # initial solution empty
    closed_facilities = facilities.copy()
    opened_facilities = []
    unassigned_towns = towns.copy()
    assigned_towns = []

    while True:
        # selection of facility that cause least total risk
        current_facility = least_total_hazard_facility(closed_facilities, hazards)

        # open the current facility, the best obtained
        current_facility.is_open = True

        # remove the current facility from the closed facilities list
        closed_facilities.pop(closed_facilities.index(current_facility))

        # update the opened facilities list
        opened_facilities.append(current_facility)

        # assign the facility to towns
        unassigned_towns, temp_assigned_towns = assign_facility_to_town(current_facility, unassigned_towns)

        # reset of parameters
        assigned_towns += temp_assigned_towns

        # exit from loop if all towns have been assigned
        if not unassigned_towns:
            break

    return closed_facilities, opened_facilities, unassigned_towns, assigned_towns
