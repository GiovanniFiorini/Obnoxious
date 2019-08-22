from commons.setup_vars import setup
from heuristics.mhf_greedy import mhf_greedy
from heuristics.mchrf_greedy import mchrf_greedy


def main(choice: int):
    facilities, towns, hazards = setup("./instances/basic.json")

    if choice == 1:
        return mhf_greedy(facilities, towns, hazards)

    if choice == 2:
        return mchrf_greedy(facilities, towns, hazards)
