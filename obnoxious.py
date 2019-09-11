import time
import pathlib
from commons.setup_vars import setup
from heuristics.mhf_greedy import mhf_greedy
from heuristics.mchrf_greedy import mchrf_greedy
from heuristics.large_neighborhood_search import large_neighborhood_search
from heuristics.variable_depth_search import variable_depth_search
from heuristics.grasp import grasp
from commons.utils import show_facility_usage_by_town, show_greedy_result, show_local_search_result, show_grasp_result
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
    print("| 7 - GRASP                                              |")
    print("| 8 - Show facility usage by town                        |")
    print("|                                                        |")
    print("| (type 'exit' to exit the program)                      |")
    print("----------------------------------------------------------\n\n")

    facilities = None
    towns = None
    hazards = None

    instance_setup = False
    path = None

    greedy_success = False

    while True:
        command = input("Give a command: ")

        if command == "exit":
            print("\nGoodbye!\n")
            break

        elif command == "1":

            num_facilities = int(input("Insert the number of facilities: "))
            num_towns = int(input("Insert the number of towns: "))
            filename = input("Insert the file name: ")
            instance_generated = generate_instance(num_facilities, num_towns, filename)

            if instance_generated:
                print(f"\nNew instance '{filename}' with {num_facilities} facilities and {num_towns} towns has been "
                      f"generated in './instances'\n")
            else:
                print("\nError while generating the new instance\n")

        elif command == "2":

            filename = input("Insert instance file name contained in 'instances' directory: ")

            path = pathlib.Path(f"./instances/{filename}.json")

            if path.exists() and path.is_file():
                facilities, towns, hazards = setup(f"./instances/{filename}.json")

                if facilities and towns and hazards:
                    print("\nInstance setup completed correctly\n")
                    instance_setup = True
                    greedy_success = False
                else:
                    print("\nError during the instance setup\n")
                    instance_setup = False
            else:
                print("\nFile doesn't exist\n")
                instance_setup = False

        elif command == "3":

            if greedy_success:
                facilities, towns, hazards = setup(str(path))
                greedy_success = False

            if instance_setup:
                start = time.time()
                greedy_success = mhf_greedy(facilities, towns)
                end = time.time()

                if greedy_success:
                    print("\nThe Minimum Hazard Facility Greedy has been completed\n")
                    duration = end - start
                    show_greedy_result(facilities, towns, hazards, duration)
                else:
                    print("\nThe Minimum Hazard Facility Greedy failed.\n")
            else:
                print("\nNo instance has been set up: you need to set up an instance before executing a greedy "
                      "heuristic\n")

        elif command == "4":

            if greedy_success:
                facilities, towns, hazards = setup(str(path))
                greedy_success = False

            if instance_setup:
                start = time.time()
                greedy_success = mchrf_greedy(facilities, towns)
                end = time.time()

                if greedy_success:
                    print("\nThe Minimum Capacity/Hazard Ratio Facility Greedy has been completed\n")
                    duration = end - start
                    show_greedy_result(facilities, towns, hazards, duration)
                else:
                    print("\nThe Minimum Capacity/Hazard Ratio Facility Greedy failed.\n")
            else:
                print("\nNo instance has been set up: you need to set up an instance before executing a greedy "
                      "heuristic\n")

        elif command == "5":
            if not greedy_success:
                print("\nThe Large Neighborhood Local Search cannot be performed: you need to execute a greedy first\n")
            else:
                start = time.time()
                iterations, improvements = large_neighborhood_search(facilities, towns, hazards, 50, 10)
                end = time.time()

                print("\nThe Large Neighborhood Local Search has been completed\n")
                duration = end - start
                show_local_search_result(facilities, towns, hazards, duration, iterations, improvements)

        elif command == "6":
            if not greedy_success:
                print("\nThe Variable Depth Local Search cannot be performed: you need to execute a greedy first\n")
            else:
                start = time.time()
                iterations, improvements = variable_depth_search(facilities, towns, hazards, 50, 10)
                end = time.time()

                print("\nThe Variable Depth Local Search has been completed\n")
                duration = end - start
                show_local_search_result(facilities, towns, hazards, duration, iterations, improvements)

        elif command == "7":
            if not instance_setup:
                print("\nYou need to set up an instance in order to use GRASP\n")
            else:
                if greedy_success:
                    facilities, towns, hazards = setup(str(path))

                g = None
                ls = None

                while g != "1" and g != "2":
                    g = input("\nChoose (1) for MHF or (2) for MCHRF: ")

                while ls != "1" and ls != "2":
                    ls = input("\nChoose (1) for LNS or (2) for VDS: ")

                start = time.time()
                iterations, improvements = grasp(facilities, towns, hazards, str(path), g=int(g), ls=int(ls))
                end = time.time()

                print("\nThe GRASP has been completed\n")
                duration = end - start
                show_grasp_result(facilities, towns, hazards, duration, iterations, improvements)

        elif command == "8":
            if instance_setup:
                show_facility_usage_by_town(towns)
            else:
                print("\nYou need to set up an instance in order to see the facility usage by town\n")

        else:
            print(f"\nThe command '{command}' is not supported yet\n")


if __name__ == "__main__":
    obnoxious()
