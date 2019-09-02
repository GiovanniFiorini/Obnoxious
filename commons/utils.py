from commons.town import get_town_with_max_hazard, total_garbage


def show_data(towns: list, facilities: list, hazards: list):
    """
    Function to print all the towns with the associated facility and the risk brought by it

    :param towns: list of problem instance's towns
    :param facilities: list of problem instance's facilities
    :param hazards: matrix of hazards caused by each facilities to the corresponding town
    :return: None
    """

    for town in towns:
        print(f'({town.town_id}, {town.name}, {town.garbage}):')
        for facility in facilities:
            print(
                f'\t rischio associato a ({facility.facility_id}, {facility.name}, {facility.capacity}): '
                f'{hazards[town.town_id - 1][facility.facility_id - 1]}')


def show_greedy_result(facilities: list, towns: list, hazards: list, duration: float):
    """
    Print the formatted result of the Greedy Algorithm

    :param facilities: list of facilities
    :param towns: list of towns
    :param hazards: matrix of hazards
    :param duration: the execution time of the algorithm
    :return: None
    """

    town, max_hazard = get_town_with_max_hazard(facilities, towns, hazards)

    print(f"Greedy Result, exec_time [{duration}]")
    print(f'Total Garbage: {total_garbage(towns)}')
    print(f"Town with max hazard: {town.name} -> hazard: {max_hazard}, garbage: {town.garbage}")
    print("Opened Facility:")
    for facility in facilities:
        if facility.is_open:
            print(f"\t{facility.name}, capacity: {facility.capacity}")
    print("\n\n")


def show_local_search_result(facilities: list, towns: list, hazards: list, duration: float, iteration: int, improvements: int):
    """
    Print the formatted result of the Local Search Algorithm

    :param facilities: list of facilities
    :param towns: list of towns
    :param hazards: list of hazards
    :param duration: the execution time of the algorithm
    :param iteration: number of the iterations
    :param improvements: number of improvements
    :return: None
    """

    town, max_hazard = get_town_with_max_hazard(facilities, towns, hazards)

    print(f"Local Search Result, exec_time [{duration}]")
    print(f'Total Garbage: {total_garbage(towns)}')
    print(f"Town with max hazard: {town.name} -> hazard: {max_hazard}, garbage: {town.garbage}")
    print(f"\t\tIteration: {iteration}, Improvement: {improvements}")
    print("Opened Facility:")
    for facility in facilities:
        if facility.is_open:
            print(f"\t{facility.name}, capacity: {facility.capacity}")
    print("\n\n")


def show_facility_usage_by_town(towns: list):
    """
    Show the usage of the facilities listed by town

    :param towns: list of towns
    :return: None
    """

    print("\n\nFacility Usage By Town")
    for town in towns:
        print(f"{town.name} with garbage = {town.garbage} use facility: {town.facility.name}"
              f" (capacity= {town.facility.capacity})")
