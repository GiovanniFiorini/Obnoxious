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
                f'\t rischio associato a ({facility.facility_id}, {facility.name}, {facility.capacity}): {hazards[town.town_id - 1][facility.facility_id - 1]}')
