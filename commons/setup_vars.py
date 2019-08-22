import json
from entity.facility import Facility
from entity.town import Town
from commons.utils import total_hazard_caused_by_facility


def setup(path: str) -> tuple:

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

    return facilities, towns, hazards
