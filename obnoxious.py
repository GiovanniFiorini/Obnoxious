from commons.setup_vars import setup
from heuristics.mhf_greedy import mhf_greedy
from heuristics.mchrf_greedy import mchrf_greedy


def obnoxious(choice: int, filename: str):
    facilities, towns, hazards = setup(f"./instances/{filename}.json")

    if choice == 1:
        return mhf_greedy(facilities, towns, hazards)

    if choice == 2:
        return mchrf_greedy(facilities, towns, hazards)
