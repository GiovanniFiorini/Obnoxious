def total_hazard_caused_by_facility(hazards: list, facility_id: int) -> int:
    """
    Retrieve from the hazards matrix the total risk caused by facility

    :param hazards: list of list, describe every hazard for the couple (town,facility)
    :param facility_id: the facility of interest
    :return: the amount of risk caused by the specified facility for every town
    """
    facility_hazard = 0
    for hazard in hazards:
        facility_hazard += hazard[facility_id]
    return facility_hazard


def total_hazard_perceived_by_town(hazards: list, town_id: int, facilities: list) -> int:
    """
    For the specified town retrieve the total risk caused by opened facility

    :param hazards: list of list, describe every hazard for the couple (town,facility)
    :param town_id: the town of interest
    :param facilities: list of the facility
    :return: the amount of risk perceived by the specified town
    """
    hazard = hazards[town_id]
    tot_hazard = 0
    for facility in facilities:
        if facility.is_open:
            tot_hazard += hazard[facility.facility_id]
    return tot_hazard
