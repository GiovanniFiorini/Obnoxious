from entity.facility import Facility


# FACILITIES
def total_capacity(facilities: list):
    tot_capacity = 0
    for facility in facilities:
        tot_capacity += facility.capacity
    return tot_capacity


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
def total_garbage(towns: list):
    tot_garbage = 0
    for town in towns:
        tot_garbage += town.garbage
    return tot_garbage


# HAZARDS
def total_hazard_caused_by_facility(hazards: list, facility_id: int):
    facility_hazard = 0
    for hazard in hazards:
        facility_hazard += hazard[facility_id]
    return facility_hazard


def total_hazard_perceived_by_town(hazards: list, town_id: int, facilities: list):
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
