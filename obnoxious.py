import time
import pathlib
from commons.setup_vars import setup
from heuristics.mhf_greedy import mhf_greedy
from heuristics.mchrf_greedy import mchrf_greedy
from heuristics.large_neighborhood_search import large_neighborhood_search
from heuristics.variable_depth_search import variable_depth_search
from commons.utils import show_facility_usage_by_town, show_greedy_result, show_local_search_result
from instances.instance_generator import generate_instance


def obnoxious():
    """
    The project main function

    :return: None
    """

    print("  ██████╗  ██████╗  ███╗   ██╗  ██████╗  ██╗  ██╗ ██╗  ██████╗  ██╗   ██╗ ███████╗")
    print(" ██╔═══██╗ ██╔══██╗ ████╗  ██║ ██╔═══██╗ ╚██╗██╔╝ ██║ ██╔═══██╗ ██║   ██║ ██╔════╝")
    print(" ██║   ██║ ██████╔╝ ██╔██╗ ██║ ██║   ██║  ╚███╔╝  ██║ ██║   ██║ ██║   ██║ ███████╗")
    print(" ██║   ██║ ██╔══██╗ ██║╚██╗██║ ██║   ██║  ██╔██╗  ██║ ██║   ██║ ██║   ██║ ╚════██║")
    print(" ╚██████╔╝ ██████╔╝ ██║ ╚████║ ╚██████╔╝ ██╔╝ ██╗ ██║ ╚██████╔╝ ╚██████╔╝ ███████║")
    print("  ╚═════╝  ╚═════╝  ╚═╝  ╚═══╝  ╚═════╝  ╚═╝  ╚═╝ ╚═╝  ╚═════╝   ╚═════╝  ╚══════╝")

    print("\n\n- COMMAND LIST -------------------------------------------")
    print("|                                                        |")
    print("| 1 - Generate new instance file                         |")
    print("| 2 - Insert instance file relative path                 |")
    print("| 3 - Minimum Hazard Facility Greedy                     |")
    print("| 4 - Minimum Capacity/Hazard Ratio Facility Greedy      |")
    print("| 5 - Large Neighborhood Local Search                    |")
    print("| 6 - Variable Depth Local Search                        |")
    print("| 7 - Show facility usage by town                        |")
    print("|                                                        |")
    print("| (type 'exit' to exit the program)                      |")
    print("----------------------------------------------------------\n\n")

    facilities = None
    towns = None
    hazards = None

    while True:
        choice = input("Choose the action: ")

        start = 0
        end = 0

        iterations = 0
        improvements = 0

        if choice == "exit":
            print("\nGoodbye!\n")
            break

        if (choice == "3" or choice == "4" or choice == "5" or choice == "6" or choice == "7") and not facilities:
            print("\nThere are no instance set up to work on; you need to give one first.\n")
            continue

        if choice == "1":

            num_facilities = int(input("Insert the number of facilities: "))
            num_towns = int(input("Insert the number of towns: "))
            filename = input("Insert the file name: ")
            generate_instance(num_facilities, num_towns, filename)

            print(f"\nNew instance '{filename}' with {num_facilities} facilities and {num_towns} towns has been "
                  f"generated in './instances'\n")

        if choice == "2":

            filename = input("Insert instance file relative path: ")

            path = pathlib.Path(f"./instances/{filename}.json")

            if path.exists() and path.is_file():
                facilities, towns, hazards = setup(f"./instances/{filename}.json")

                print("\nInstance setup completed correctly\n")
            else:
                print("\nFile doesn't exist\n")

        if choice == "3":

            start = time.time()
            greedy_success = mhf_greedy(facilities, towns)
            end = time.time()

            if not greedy_success:
                print("The Minimum Hazard Facility Greedy failed.")
                continue

        if choice == "4":

            start = time.time()
            greedy_success = mchrf_greedy(facilities, towns)
            end = time.time()

            if not greedy_success:
                print("The Minimum Capacity/Hazard Ratio Facility Greedy failed.")
                continue

        if choice == "5":

            start = time.time()
            iterations, improvements = large_neighborhood_search(facilities, towns, hazards, 50, 10)
            end = time.time()

        if choice == "6":

            start = time.time()
            iterations, improvements = variable_depth_search(facilities, towns, hazards, 50, 10)
            end = time.time()

        if choice == "3" or choice == "4":

            duration = end - start
            show_greedy_result(facilities, towns, hazards, duration)

        if choice == "5" or choice == "6":

            duration = end - start
            show_local_search_result(facilities, towns, hazards, duration, iterations, improvements)

        if choice == "7" and facilities:
            show_facility_usage_by_town(towns)


if __name__ == "__main__":
    obnoxious()
