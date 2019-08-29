from commons.setup_vars import setup
from heuristics.mhf_greedy import mhf_greedy
from heuristics.mchrf_greedy import mchrf_greedy
from heuristics.local_search import local_search
from commons.utils import show_facility_usage_by_town, show_greedy_result, show_local_search_result
import time


def obnoxious(choice: int, filename: str):
    facilities, towns, hazards = setup(f"./instances/{filename}.json")

    if choice == 1:

        start = time.time()
        greedy_success = mhf_greedy(facilities, towns)
        end = time.time()

        if not greedy_success:
            print("The Minimum Hazard Facility Greedy failed.")
            return

        duration = end - start

        show_greedy_result(facilities, towns, hazards, duration)

        start = time.time()
        iterations, improvements = local_search(facilities, towns, hazards, 50, 10)
        end = time.time()

        duration = end - start

        show_local_search_result(facilities, towns, hazards, duration, iterations, improvements)

    if choice == 2:

        start = time.time()
        greedy_success = mchrf_greedy(facilities, towns)
        end = time.time()

        if not greedy_success:
            print("The Minimum Capacity/Hazard Ratio Facility Greedy failed.")
            return

        duration = end - start

        show_greedy_result(facilities, towns, hazards, duration)

        start = time.time()
        iterations, improvements = local_search(facilities, towns, hazards, 50, 10)
        end = time.time()

        duration = end - start

        show_local_search_result(facilities, towns, hazards, duration, iterations, improvements)

    show_facility_usage_by_town(towns)
