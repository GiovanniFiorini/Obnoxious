from commons.setup_vars import setup
from heuristics.mhf_greedy import mhf_greedy
from heuristics.mchrf_greedy import mchrf_greedy
from heuristics.local_search import local_search
from commons.town import *
import time


# TODO: trasforma in funzioni di stampa
# TODO: refactor dei tipi di ritorno -> può essere più utile ritornare il successo o il fallimento dell'algoritmo
def obnoxious(choice: int, filename: str):
    facilities, towns, hazards = setup(f"./instances/{filename}.json")

    if choice == 1:

        start = time.time()

        f, t = mhf_greedy(facilities, towns, hazards)

        end = time.time()

        duration = end - start

        town, max_hazard = get_town_with_max_hazard(f, t, hazards)

        print(f"Greedy Result, exec_time [{duration}]")
        print(f'Total Garbage: {total_garbage(towns)}')
        print(f"Town with max hazard: {town.name} -> hazard: {max_hazard}, garbage: {town.garbage}")
        print("Opened Facility:")
        for item in f:
            if item.is_open:
                print(f"\t{item.name}, capacity: {item.capacity}")
        print("\n\n")

        start = time.time()

        fac, to, i, improv = local_search(f, t, hazards, 50, 10)

        end = time.time()

        duration = end - start

        town, max_hazard = get_town_with_max_hazard(fac, to, hazards)

        print(f"Local Search Result, exec_time [{duration}]")
        print(f'Total Garbage: {total_garbage(towns)}')
        print(f"Town with max hazard: {town.name} -> hazard: {max_hazard}, garbage: {town.garbage}")
        print(f"\t\tIteration: {i}, Improvement: {improv}")
        print("Opened Facility:")
        for item in f:
            if item.is_open:
                print(f"\t{item.name}, capacity: {item.capacity}")
        print("\n")

    if choice == 2:

        start = time.time()

        f, t = mchrf_greedy(facilities, towns, hazards)

        end = time.time()

        duration = end - start

        town, max_hazard = get_town_with_max_hazard(f, t, hazards)

        print(f"Greedy Result, exec_time [{duration}]")
        print(f'Total Garbage: {total_garbage(towns)}')
        print(f"Town with max hazard: {town.name} -> hazard: {max_hazard}, garbage: {town.garbage}")
        print("Opened Facility:")
        for item in f:
            if item.is_open:
                print(f"\t{item.name}, capacity: {item.capacity}")
        print("\n\n")

        start = time.time()

        fac, to, i, improv = local_search(f, t, hazards, 50, 10)

        end = time.time()

        duration = end - start

        town, max_hazard = get_town_with_max_hazard(fac, to, hazards)

        print(f"Local Search Result, exec_time [{duration}]")
        print(f'Total Garbage: {total_garbage(towns)}')
        print(f"Town with max hazard: {town.name} -> hazard: {max_hazard}, garbage: {town.garbage}")
        print(f"\t\tIteration: {i}, Improvement: {improv}")
        print("Opened Facility:")
        for item in f:
            if item.is_open:
                print(f"\t{item.name}, capacity: {item.capacity}")
        print("\n")

    print("\n\nFacility Usage By Town")
    for town in towns:
        print(f"{town.name} with garbage= {town.garbage} use facility: {town.facility.name}"
              f" (capacity= {town.facility.capacity})")
