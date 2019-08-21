from entity.facility import Facility
from entity.town import Town


def total_garbage(towns: list):
    tot_garbage = 0
    for town in towns:
        tot_garbage += town.garbage
    return tot_garbage


def total_capacity(facilities: list):
    tot_capacity = 0
    for facility in facilities:
        tot_capacity += facility.capacity
    return tot_capacity


def total_hazard_caused_by_facility(hazards: list, facility_id: int):
    facility_hazard = 0
    for hazard in hazards:
        facility_hazard += hazard[facility_id]
    return facility_hazard


def total_hazard_perceived_by_town(hazards : list, town_id: int, facilities: list):
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
            print(f'\t rischio associato a ({facility.facility_id}, {facility.name}, {facility.capacity}): {hazards[town.town_id-1][facility.facility_id-1]}')
