from commons.hazard import total_hazard_perceived_by_town
from entity.facility import Facility
import random


# TODO: bug nei controlliu per la selezione della facility che dovrebbe sostituire quella destroyed
def local_search(facilities: list, towns: list, hazards: list, max_iteration, max_improvement_counter) -> tuple:
    """
    Implements a local search on the solution obtained by the greedy.
    This algorithm is inspired by the Large Neighborhood  Search.

    :param facilities: list of the problem instance's facilities
    :param towns: list of the problem instance's towns
    :param hazards: matrix of hazards caused by each facilities to the corresponding town
    :param max_iteration: limits the number of iteration
    :param max_improvement_counter: limits the number of the improvement
    :return: a tuple...
    """

    # counters
    max_attempts_per_town = 30
    attempts_per_town = 0

    iteration = 0

    improvement_counter = 0

    temp_facility: Facility = None

    while attempts_per_town < max_attempts_per_town:
        print(f'attempts per town: {attempts_per_town}\n')

        # var
        opened_facilities = list(filter(lambda o_facility: o_facility.is_open, facilities))
        closed_facilities = list(filter(lambda c_facility: not c_facility.is_open, facilities))

        # get the town with the maximum hazard perceived
        current_town = max(towns,
                           key=lambda town: total_hazard_perceived_by_town(hazards, town.town_id, opened_facilities))
        current_town_hazard = total_hazard_perceived_by_town(hazards,current_town.town_id, opened_facilities)

        # get random 2 opened facility to close
        del_facility_1, del_facility_2 = random.sample(opened_facilities, 2)

        for facility in closed_facilities:
            current_hazard = hazards[current_town.town_id][facility.facility_id]
            del_hazard_1 = hazards[current_town.town_id][del_facility_1.facility_id]
            del_hazard_2 = hazards[current_town.town_id][del_facility_2.facility_id]

            # searching a facility with capacity higher than the sum of the capacity of the selected facilities
            # and a associated risk for the current town smaller than the sum of the risk
            if current_hazard < del_hazard_1 + del_hazard_2:
                if facility.capacity >= del_facility_1.capacity + del_facility_2.capacity:
                    temp_facility = facility
                    break
        print(f'{temp_facility.name}')
        # if no facility respect the constraints,
        # count the attempts and get back to top for select a new couple of facility
        if not temp_facility:
            attempts_per_town += 1
            continue

        # update all the local variables
        closed_facility_1 = opened_facilities.pop(opened_facilities.index(del_facility_1))
        closed_facility_1.is_open = False
        closed_facilities.append(closed_facility_1)
        closed_facility_2 = opened_facilities.pop(opened_facilities.index(del_facility_2))
        closed_facility_2.is_open = False
        closed_facilities.append(closed_facility_2)
        closed_facilities.pop(closed_facilities.index(temp_facility))
        temp_facility.is_open = True
        opened_facilities.append(temp_facility)

        # calculate the max hazard and the respective town
        new_max_hazard_town = max(towns,
                                  key=lambda town: total_hazard_perceived_by_town(hazards, town.town_id,
                                                                                  opened_facilities))
        new_max_hazard = total_hazard_perceived_by_town(hazards, new_max_hazard_town.town_id,opened_facilities)

        # compares the old and the new constraint
        if new_max_hazard < current_town_hazard:
            # update all the assignments of the solution
            new_facilities = closed_facilities + opened_facilities
            facilities = new_facilities.sort(key=lambda item: item.facility_id)

            for town in towns:
                if town.facility == del_facility_1 or town.facility == del_facility_2:
                    town.facility = temp_facility

            improvement_counter += 1
            # check the number of improvement
            if improvement_counter == max_improvement_counter:
                break

        iteration += 1
        print(f'iterazione: {iteration}\n')
        # check the number of iteration
        if iteration == max_iteration:
            break

    return facilities, towns
