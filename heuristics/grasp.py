from commons.setup_vars import setup
from heuristics.mhf_greedy import mhf_greedy
from heuristics.mchrf_greedy import mchrf_greedy
from heuristics.large_neighborhood_search import large_neighborhood_search
from heuristics.variable_depth_search import variable_depth_search
from commons.town import get_town_with_max_hazard


def grasp(facilities: list, towns: list, hazards: list, instance_path: str, g: int = 1, ls: int = 1, iterations: int = 10, ls_iteration: int = 50, ls_improvement: int = 10) -> tuple:
    """
    This function implement a meta-heuristic inspired by Greedy Randomized Adaptive Search Procedure (GRASP); it can use
    two different type of randomized greedy and two different type of local search decided by the user

    :param facilities: list of the problem instance's facilities
    :param towns: list of the problem instance's towns
    :param hazards: matrix of hazards caused by each facilities to the corresponding town
    :param instance_path: path of the instance
    :param g: the greedy chosen
    :param ls: the local search chosen
    :param iterations: max iterations number made by GRASP
    :param ls_iteration: max local search iterations
    :param ls_improvement: max local search improvements permitted
    :return: a tuple with the number of iteration performed and the number of improvements obtained
    """

    greedy = None
    local_search = None

    max_hazard = 0
    current_max_hazard = 0

    improvements = 0

    # Selecting the chosen greedy algorithm
    if g == 1:
        greedy = mhf_greedy
    elif g == 2:
        greedy = mchrf_greedy

    # Selecting the chosen local search algorithm
    if ls == 1:
        local_search = large_neighborhood_search
    elif ls == 2:
        local_search = variable_depth_search

    for i in range(iterations):
        # Setup the instances to work on
        w_facilities, w_towns, w_hazards = setup(instance_path)

        # Execute the greedy chosen
        greedy(w_facilities, w_towns, True)
        # Execute the local search chosen
        local_search(w_facilities, w_towns, w_hazards, ls_iteration, ls_improvement)

        if i > 0:
            # get the old town with the maximum hazard perceived
            max_hazard_town, max_hazard = get_town_with_max_hazard(facilities, towns, hazards)
            # get the current town with the maximum hazard perceived
            current_max_hazard_town, current_max_hazard = get_town_with_max_hazard(w_facilities, w_towns, w_hazards)

        # check if this is the first iteration or if a better solution has been found
        if i == 0 or current_max_hazard < max_hazard:

            # update the solution with opened/closed facilities
            for j in range(len(facilities)):
                if w_facilities[j].is_open:
                    facilities[j].is_open = True
                else:
                    facilities[j].is_open = False

            # update the solution with the association between towns and opened facilities
            for k in range(len(towns)):
                towns[k].facility = facilities[w_towns[k].facility.facility_id]

            # increment the number of improvements obtained
            improvements += 1

    return iterations, improvements
