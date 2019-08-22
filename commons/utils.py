from entity.facility import Facility


# FACILITIES
def total_capacity(facilities: list) -> int:
    tot_capacity = 0
    for facility in facilities:
        tot_capacity += facility.capacity
    return tot_capacity


# check the hazards matrix and discover the facility with the minimum total hazard (for every town)
def facility_least_total_hazard(facilities: list, hazards: list) -> Facility:
    current_facility_hazard = 101
    current_facility = None
    for facility in facilities:
        facility_hazard = total_hazard_caused_by_facility(hazards, facility.facility_id)

        if facility_hazard < current_facility_hazard:
            current_facility_hazard = facility_hazard
            current_facility = facility
    if current_facility is None:
        print('ERROR in utils.py: facility_least_total_hazard: current facility is None')
        exit(1)
    else:
        return current_facility


# TOWNS
def total_garbage(towns: list) -> int:
    tot_garbage = 0
    for town in towns:
        tot_garbage += town.garbage
    return tot_garbage


# assign a facility to many towns as possible (circa knapsack problem)
def assign_facility_to_town(facility: Facility, unassigned_towns: list) -> tuple:
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


# HAZARDS
def total_hazard_caused_by_facility(hazards: list, facility_id: int) -> int:
    facility_hazard = 0
    for hazard in hazards:
        facility_hazard += hazard[facility_id]
    return facility_hazard


def total_hazard_perceived_by_town(hazards: list, town_id: int, facilities: list) -> int:
    hazard = hazards[town_id]
    tot_hazard = 0
    for facility in facilities:
        if facility.is_open:
            tot_hazard += hazard[facility.facility_id]
    return tot_hazard


def show_data(towns: list, facilities: list, hazards: list):
    for town in towns:
        print(f'({town.town_id}, {town.name}, {town.garbage}):')
        for facility in facilities:
            print(
                f'\t rischio associato a ({facility.facility_id}, {facility.name}, {facility.capacity}): {hazards[town.town_id - 1][facility.facility_id - 1]}')
