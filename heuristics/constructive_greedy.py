from commons.utils import *


# TODO: rinomina greedy in min_hazard_first_greedy -> mhf_greedy
# TODO: nuova greedy -> max_capacity_hazard_ratio_first_greedy mchrf_greedy (scegliamo facility con capacity/tot_hazard maggiore)


def constructive_greedy(facilities: list, towns: list, hazards: list) -> tuple:
    # initial solution empty
    closed_facilities = facilities.copy()
    opened_facilities = []
    unassigned_towns = towns.copy()
    assigned_towns = []
    current_facility: Facility

    # iteration
    while True:
        # selection of facility that cause least total risk
        current_facility = facility_least_total_hazard(closed_facilities, hazards)

        # open the current facility, the best obtained
        current_facility.is_open = True

        # remove the current facility from the closed facilities list
        index = closed_facilities.index(current_facility)
        closed_facilities.pop(index)

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
