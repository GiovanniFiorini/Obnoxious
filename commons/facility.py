from entity.facility import Facility
from .hazard import total_hazard_caused_by_facility


def total_capacity(facilities: list) -> int:
    """
    Function to obtain the total capacity of all facilities of the current problem

    :param facilities: list of problem instance's facilities
    :return: an int representing the total capacity of all the facilities
    """

    tot_capacity = 0
    for facility in facilities:
        tot_capacity += facility.capacity
    return tot_capacity


def least_total_hazard_facility(facilities: list, hazards: list) -> Facility:
    """
    Check the hazards matrix and discover the facility with the minimum total hazard (for every town)

    :param facilities: list of facilities
    :param hazards: list of list, describe every hazard for the couple (town,facility)
    :return: the facility with the minimum total hazard
    """

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


def maximum_capacity_hazard_ratio_facility(facilities: list) -> Facility:
    """
    Function to obtain the facility with the maximum capacity/hazard ratio

    :param facilities: list of facilities
    :return: the facility with the highest capacity/hazard ratio
    """

    current_facility_ratio = 0
    current_facility = None

    for facility in facilities:
        facility_ratio = facility.capacity/facility.total_hazard

        if facility_ratio > current_facility_ratio:
            current_facility_ratio = facility_ratio
            current_facility = facility

    if current_facility is None:
        print('ERROR in utils.py: facility_least_total_hazard: current facility is None')
        exit(1)
    else:
        return current_facility
