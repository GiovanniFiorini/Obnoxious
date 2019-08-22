from commons.facility import maximum_capacity_hazard_ratio_facility
from commons.town import assign_facility_to_town


def mchrf_greedy(facilities: list, towns: list, hazards: list) -> tuple:
    """
    The algorithm is a greedy heuristic that decide which facility to open first based on capacity/hazard ratio,
    starting from the facility with maximum ratio and proceeding by non ascending order

    :param facilities: list of the problem instance's facilities
    :param towns: list of the problem instance's towns
    :param hazards: matrix of hazards caused by each facilities to the corresponding town
    :return: a tuple containing the used/unused facilities and the towns with their relative facilities
    """

    closed_facilities = facilities.copy()
    opened_facilities = []
    unassigned_towns = towns.copy()
    assigned_towns = []

    while True:
        current_facility = maximum_capacity_hazard_ratio_facility(closed_facilities)

        current_facility.is_open = True

        closed_facilities.pop(closed_facilities.index(current_facility))

        opened_facilities.append(current_facility)

        unassigned_towns, temp_assigned_towns = assign_facility_to_town(current_facility, unassigned_towns)
        assigned_towns += temp_assigned_towns

        if not unassigned_towns:
            break

    return closed_facilities, opened_facilities, unassigned_towns, assigned_towns
