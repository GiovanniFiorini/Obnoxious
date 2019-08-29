from entity.facility import Facility


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


def facility_with_max_hazard_per_town(open_facilities: list, town_id: int, hazards) -> Facility:
    """
    Retrieve the facility with the highest hazard for the town specified

    :param open_facilities: list of the opened facilities
    :param town_id: the id of the town
    :param hazards: matrix of the hazards
    :return: the facility
    """

    max_hazard = 0
    max_facility = None
    for facility in open_facilities:
        current_hazard = hazards[town_id][facility.facility_id]
        if current_hazard > max_hazard:
            max_hazard = current_hazard
            max_facility = facility
    return max_facility
