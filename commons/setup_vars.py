import json
from entity.facility import Facility
from entity.town import Town

facilities = []
towns = []
hazards = []

with open('../instances/basic.json', 'r') as f:
    data = json.load(f)

for facility in data['facilities']:
    temp_facility = Facility(facility['facility_id'], facility['name'], facility['capacity'])
    facilities.append(temp_facility)

for town in data['towns']:
    temp_town = Town(town['town_id'], town['name'], town['garbage'])
    towns.append(temp_town)

hazards = data['hazards']

for town in towns:
    print(f'({town.town_id}, {town.name}, {town.garbage}):')
    for facility in facilities:
        print(f'\t rischio associato a ({facility.facility_id}, {facility.name}, {facility.capacity}): {hazards[town.town_id-1][facility.facility_id-1]}')
