from commons.town import get_town_with_max_hazard, total_garbage
from commons.facility import total_capacity, total_hazard, facility_with_max_hazard_per_town


def show_data(towns: list, facilities: list, hazards: list):
    """
    Function to print all the towns with the associated facility and the risk brought by it

    :param towns: list of problem instance's towns
    :param facilities: list of problem instance's facilities
    :param hazards: matrix of hazards caused by each facilities to the corresponding town
    :return: None
    """

    for town in towns:
        print(f'\n({town.town_id}, {town.name}, {town.garbage}):')
        for facility in facilities:
            print(
                f'\t hazard associated to ({facility.facility_id}, {facility.name}, {facility.capacity}): '
                f'{hazards[town.town_id - 1][facility.facility_id - 1]}')
    print("")


def show_greedy_result(facilities: list, towns: list, hazards: list, duration: float):
    """
    Print the formatted result of the Greedy Algorithm

    :param facilities: list of facilities
    :param towns: list of towns
    :param hazards: matrix of hazards
    :param duration: the execution time of the algorithm
    :return: None
    """

    opened_facilities = list(filter(lambda el: el.is_open, facilities))

    town, max_hazard = get_town_with_max_hazard(facilities, towns, hazards)

    max_hazard_facility = facility_with_max_hazard_per_town(opened_facilities, town.town_id, hazards)

    print(f":::: GREEDY RESULTS ::::")
    print(f"\texec_time: {duration} sec")
    print(f'\nTotal garbage produced by all cities: {total_garbage(towns)}')
    print(f"Total capacity of all opened facilities: "
          f"{total_capacity(opened_facilities)}")
    print(f"Total hazard caused by all opened facilities: "
          f"{total_hazard(opened_facilities)}")
    print("\nTown with max hazard:")
    print(f"\t{town.name} -> highest suffered hazard: "
          f"{max_hazard} caused by {max_hazard_facility.name}, garbage: {town.garbage}")
    print("Opened Facility:")
    for facility in facilities:
        if facility.is_open:
            print(f"\t{facility.name} -> capacity: {facility.capacity}, global caused hazard: {facility.total_hazard}")
    print("")


def show_local_search_result(facilities: list, towns: list, hazards: list, duration: float,
                             iterations: int, improvements: int):
    """
    Print the formatted result of the Local Search Algorithm

    :param facilities: list of facilities
    :param towns: list of towns
    :param hazards: list of hazards
    :param duration: the execution time of the algorithm
    :param iterations: number of the iterations
    :param improvements: number of improvements
    :return: None
    """

    opened_facilities = list(filter(lambda el: el.is_open, facilities))

    town, max_hazard = get_town_with_max_hazard(facilities, towns, hazards)

    max_hazard_facility = facility_with_max_hazard_per_town(opened_facilities, town.town_id, hazards)

    print(f":::: LOCAL SEARCH RESULTS ::::")
    print(f"\texec_time: {duration} sec")
    print(f"\tIteration: {iterations}, Improvement: {improvements}")
    print(f'\nTotal garbage produced by all cities: {total_garbage(towns)}')
    print(f"Total capacity of all opened facilities: "
          f"{total_capacity(opened_facilities)}")
    print(f"Total hazard caused by all opened facilities: "
          f"{total_hazard(opened_facilities)}")
    print("\nTown with max hazard:")
    print(f"\t{town.name} -> highest suffered hazard: "
          f"{max_hazard} caused by {max_hazard_facility.name}, garbage: {town.garbage}")
    print("Opened Facility:")
    for facility in facilities:
        if facility.is_open:
            print(f"\t{facility.name} -> capacity: {facility.capacity}, global caused hazard: {facility.total_hazard}")
    print("")


def show_facility_usage_by_town(towns: list):
    """
    Show the usage of the facilities listed by town

    :param towns: list of towns
    :return: None
    """

    print("\nFacility Usage By Town")
    for town in towns:
        print(f"{town.name} with garbage = {town.garbage} use facility: {town.facility.name}"
              f" (capacity = {town.facility.capacity})")
    print("")
