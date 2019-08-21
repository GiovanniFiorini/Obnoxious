from entity.facility import Facility
from commons.utils import *


# assign a facility to many towns as possible
def facility_assignment(facility: Facility, unassigned_towns: list):
    capacity = facility.capacity
    assigned_towns: list = []

    while True:
        # get the town that produce the most amount of garbage
        max_garbage_town = max(unassigned_towns, key=lambda town: town.garbage)

        if max_garbage_town.garbage < capacity:
            # decreasing current facility capacity by the garbage produced by the town
            capacity -= max_garbage_town.garbage
            # remove the current town from the unassigned towns list
            max_garbage_town_index = unassigned_towns.index(max_garbage_town)
            unassigned_towns.pop(max_garbage_town_index)
            # assign the facility to the current town
            max_garbage_town.facility = facility
            # add the current town to the assigned towns list
            assigned_towns.append(max_garbage_town)
        
        # exit from loop if all the towns have been assigned
        # or the minimum amount of garbage (of any town) is bigger than the residual capacity
        if not unassigned_towns or min(unassigned_towns, key=lambda town: town.garbage).garbage > capacity:
            break

    return unassigned_towns, assigned_towns


def constructive_greedy(facilities: list, towns: list, hazards: list):
    # initial solution empty
    closed_facilities = facilities.copy()
    opened_facilities = []
    unassigned_towns = towns.copy()
    assigned_towns = []
    current_facility_hazard = 101

    # iteration
    while True:
        # selection of facility that cause least total risk
        for facility in closed_facilities:
            facility_hazard = total_hazard_caused_by_facility(hazards, facility.facility_id)

            if facility_hazard < current_facility_hazard:
                current_facility_hazard = facility_hazard
                current_facility = facility

        # open the current facility, the best obtained
        current_facility.is_open = True
        # remove the current facility from the closed facilities list
        index = closed_facilities.index(current_facility)
        closed_facilities.pop(index)
        # update the opened facilities list
        opened_facilities.append(current_facility)
        # assign the facility to towns
        unassigned_towns, temp_assigned_towns = facility_assignment(current_facility, unassigned_towns)
        # reset of parameters
        assigned_towns += temp_assigned_towns
        current_facility_hazard = 101

        # exit from loop if all towns have been assigned
        if not unassigned_towns:
            break

    return closed_facilities, opened_facilities, unassigned_towns, assigned_towns
