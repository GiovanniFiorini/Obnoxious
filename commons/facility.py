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
