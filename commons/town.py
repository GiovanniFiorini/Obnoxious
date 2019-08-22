from entity.facility import Facility


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


def assign_facility_to_town(facility: Facility, unassigned_towns: list) -> tuple:
    """
    Assign a facility to many towns as possible (circa knapsack problem)

    :param facility: the facility to assign
    :param unassigned_towns: list of the remaining towns with no facility assigned
    :return: the unassigned towns, the town to whom the facility have been assigned
    """
    capacity = facility.capacity
    assigned_towns: list = []
    temp_unassigned_towns = unassigned_towns.copy()

    # exit from loop if all the towns have been assigned
    while len(temp_unassigned_towns) > 0:
        # get the town that produce the most amount of garbage
        max_garbage_town = max(temp_unassigned_towns, key=lambda town: town.garbage)

        if max_garbage_town.garbage <= capacity:
            # decreasing current facility capacity by the garbage produced by the town
            capacity -= max_garbage_town.garbage
            # remove the current town from the unassigned towns list
            unassigned_towns.pop(unassigned_towns.index(max_garbage_town))
            # remove the current town from the temporary unassigned towns list
            temp_unassigned_towns.pop(temp_unassigned_towns.index(max_garbage_town))
            # assign the facility to the current town
            max_garbage_town.facility = facility
            # add the current town to the assigned towns list
            assigned_towns.append(max_garbage_town)
        elif min(unassigned_towns, key=lambda town: town.garbage).garbage < capacity:
            temp_unassigned_towns.pop(temp_unassigned_towns.index(max_garbage_town))
        else:
            # exit from loop if the minimum amount of garbage (of any town) is bigger than the residual capacity
            break

    return unassigned_towns, assigned_towns
