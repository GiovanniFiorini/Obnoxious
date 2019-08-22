import json
from entity.facility import Facility
from entity.town import Town


def setup(path: str) -> tuple:

    facilities = []
    towns = []
    hazards = []

    with open(path, 'r') as f:
        data = json.load(f)

    for facility in data['facilities']:
        temp_facility = Facility(facility['facility_id'], facility['name'], facility['capacity'])
        facilities.append(temp_facility)

    for town in data['towns']:
        temp_town = Town(town['town_id'], town['name'], town['garbage'])
        towns.append(temp_town)

    hazards = data['hazards']

    return facilities, towns, hazards
