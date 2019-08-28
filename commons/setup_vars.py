import json
from entity.facility import Facility
from entity.town import Town
from commons.hazard import total_hazard_caused_by_facility
from commons.facility import total_capacity
from commons.town import total_garbage


def setup(path: str) -> tuple:
    """
    Function to setup the data structures that will hold the data for the current problem instance

    :param path: a string containing the path to the JSON file with the problem's data
    :return: a tuple containing facilities, towns and hazards of the current problem's instance
    """

    facilities = []
    towns = []
    hazards = []

    with open(path, 'r') as f:
        data = json.load(f)

    hazards += data['hazards']

    for facility in data['facilities']:
        tot_hazard = total_hazard_caused_by_facility(hazards, facility['facility_id'])
        temp_facility = Facility(facility['facility_id'], facility['name'], facility['capacity'], tot_hazard)
        facilities.append(temp_facility)

    for town in data['towns']:
        temp_town = Town(town['town_id'], town['name'], town['garbage'])
        towns.append(temp_town)

    if total_garbage(towns) > total_capacity(facilities):
        print("L'istanza non ha soluzione: la capacità totale delle facility è minore dei rifiuti totali prodotti.")
        exit(0)

    return facilities, towns, hazards
