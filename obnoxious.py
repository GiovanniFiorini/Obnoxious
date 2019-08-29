import time
from commons.setup_vars import setup
from heuristics.mhf_greedy import mhf_greedy
from heuristics.mchrf_greedy import mchrf_greedy
from heuristics.large_neighborhood_search import large_neighborhood_search
from heuristics.variable_depth_search import variable_depth_search
from commons.utils import show_facility_usage_by_town, show_greedy_result, show_local_search_result


def obnoxious(greedy: int, local_search: int, filename: str):
    """
    The main function, it runs the algorithm chosen

    :param greedy: the greedy chosen
    :param local_search: the local search chosen
    :param filename: the name of the file containing the instance
    :return: None
    """

    facilities, towns, hazards = setup(f"./instances/{filename}.json")

    start = 0
    end = 0

    iterations = 0
    improvements = 0

    if greedy == 1:
        start = time.time()
        greedy_success = mhf_greedy(facilities, towns)
        end = time.time()

        if not greedy_success:
            print("The Minimum Hazard Facility Greedy failed.")
            return

    if greedy == 2:

        start = time.time()
        greedy_success = mchrf_greedy(facilities, towns)
        end = time.time()

        if not greedy_success:
            print("The Minimum Capacity/Hazard Ratio Facility Greedy failed.")
            return

    duration = end - start

    show_greedy_result(facilities, towns, hazards, duration)

    if local_search == 1:

        start = time.time()
        iterations, improvements = large_neighborhood_search(facilities, towns, hazards, 50, 10)
        end = time.time()

    if local_search == 2:

        start = time.time()
        iterations, improvements = variable_depth_search(facilities, towns, hazards, 50, 10)
        end = time.time()

    duration = end - start

    show_local_search_result(facilities, towns, hazards, duration, iterations, improvements)

    # show_facility_usage_by_town(towns)
