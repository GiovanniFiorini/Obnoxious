from commons.setup_vars import setup
from heuristics.mhf_greedy import mhf_greedy
from heuristics.mchrf_greedy import mchrf_greedy
from heuristics.local_search import local_search
from commons.town import get_town_with_max_hazard


def obnoxious(choice: int, filename: str):
    facilities, towns, hazards = setup(f"./instances/{filename}.json")

    if choice == 1:
        f, t = mhf_greedy(facilities, towns, hazards)

        town, max_hazard = get_town_with_max_hazard(f, t, hazards)

        print(f"Greedy Result")
        print(f"Town with max hazard: {town.name} -> hazard: {max_hazard}")
        print("Opened Facility:")
        for item in f:
            if item.is_open:
                print(f"\t{item.name}")
        print("\n\n")

        fac, to, i, improv = local_search(f, t, hazards, 50, 10)

        town, max_hazard = get_town_with_max_hazard(fac, to, hazards)

        print(f"Local Search Result")
        print(f"Town with max hazard: {town.name} -> hazard: {max_hazard}")
        print(f"\t\tIteration: {i}, Improvement: {improv}")
        print("Opened Facility:")
        for item in f:
            if item.is_open:
                print(f"\t{item.name}")
        print("\n")

    if choice == 2:
        f, t = mchrf_greedy(facilities, towns, hazards)
        town, max_hazard = get_town_with_max_hazard(f, t, hazards)

        print(f"Greedy Result")
        print(f"Town with max hazard: {town.name} -> hazard: {max_hazard}")
        print("Opened Facility:")
        for item in f:
            if item.is_open:
                print(f"\t{item.name}")
        print("\n\n")

        fac, to, i, improv = local_search(f, t, hazards, 50, 10)

        town, max_hazard = get_town_with_max_hazard(fac, to, hazards)

        print(f"Local Search Result")
        print(f"Town with max hazard: {town.name} -> hazard: {max_hazard}")
        print(f"\t\tIteration: {i}, Improvement: {improv}")
        print("Opened Facility:")
        for item in f:
            if item.is_open:
                print(f"\t{item.name}")
        print("\n")
