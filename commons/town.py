from commons.hazard import total_hazard_perceived_by_town


def total_garbage(towns: list) -> int:
    """
    Function that calculate the total amount of garbage produced by all the cities

    :param towns: list of problem instance's towns
    :return: an int representing the total amount of garbage produced by all towns
    """

    tot_garbage = 0
    for town in towns:
        tot_garbage += town.garbage
    return tot_garbage


def get_town_with_max_hazard(facilities: list, towns: list, hazards: list) -> tuple:
    """
    Retrieve the town with the highest hazard and the value of that hazard

    :param facilities: list of the problem instance's facilities
    :param towns: list of the problem instance's towns
    :param hazards: matrix of hazards caused by each facilities to the corresponding town
    :return: tuple, the town with the maximum hazard associated to and the value of that hazard
    """
    town = max(towns, key=lambda c_town: total_hazard_perceived_by_town(hazards, c_town.town_id, facilities))
    town_hazard = total_hazard_perceived_by_town(hazards, town.town_id, facilities)

    return town, town_hazard
