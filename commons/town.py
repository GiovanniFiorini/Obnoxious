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