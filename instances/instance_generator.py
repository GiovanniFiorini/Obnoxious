import random
import math
import json


def generate_instance(num_facilities: int, num_towns: int, file_name: str) -> None:
    """
    Function to generate problem's instances

    :param num_towns: number of towns to be generated
    :param num_facilities: number of facilities to be generated
    :param file_name: name of the json file containing the problem's instance
    :return: None
    """

    facility_dictionary = [
        "Perseus",
        "Andromeda",
        "Cassiopeia",
        "Cetus",
        "Cepheus",
        "Pegasus",
        "Auriga",
        "Hercules",
        "Sagitta",
        "Aquila",
        "Lyra",
        "Cygnus",
        "Hydra",
        "Crater",
        "Corvus",
        "Ophiuchus",
        "Serpens",
        "Centaurus",
        "Lupus",
        "Corona Australis",
        "Ara",
        "Orion",
        "Canis Major",
        "Canis Minor",
        "Lepus",
        "Monoceros",
        "Aries",
        "Taurus",
        "Gemini",
        "Cancer",
        "Leo",
        "Virgo",
        "Libra",
        "Scorpius",
        "Sagittarius",
        "Capricornus",
        "Aquarius",
        "Pisces",
        "Ursa Major",
        "Ursa Minor",
        "Draco",
        "Canes Venatici",
        "Boötes",
        "Corona Borealis"
    ]
    towns_dictionary = [
        "Rome",
        "Milan",
        "Naples",
        "Turin",
        "Florence",
        "Salerno",
        "Palermo",
        "Catania",
        "Genoa",
        "Bari",
        "Bologna",
        "Verona",
        "Pescara",
        "Cagliari",
        "Venice",
        "Messina",
        "Como",
        "Caserta",
        "Trieste",
        "Pisa",
        "Taranto",
        "Bergamo",
        "Reggio di Calabria",
        "Treviso",
        "Modena",
        "Parma",
        "Lecce",
        "Livorno",
        "Foggia",
        "Perugia",
        "Ravenna",
        "Ferrara",
        "Siracusa",
        "Sassari",
        "Udine",
        "Barletta",
        "Trento",
        "Brindisi",
        "Novara",
        "Ancona",
        "Soprabolzano",
        "Catanzaro",
        "Arezzo",
        "Marsala",
        "Asti",
        "Potenza",
        "Ragusa",
        "L’Aquila",
        "Benevento",
        "Civitavecchia",
        "Crotone",
        "Siena",
        "Campobasso",
        "Olbia",
        "Aosta",
        "Vibo Valentia",
        "Padova",
        "Savona",
        "Caltanissetta",
        "Vicenza",
        "Gorizia",
        "Rieti",
        "Grosseto",
        "Bolzano",
        "Massa",
        "Sanluri",
        "Latina",
        "Vercelli",
        "Belluno",
        "Cremona",
        "Oristano",
        "Mantova",
        "Prato",
        "Enna",
        "Lucca",
        "Viterbo",
        "Villacidro",
        "Trani",
        "Pavia",
        "Piacenza",
        "Monza",
        "Verbania",
        "Rimini",
        "Andria",
        "Fermo",
        "Nuoro",
        "Alessandria",
        "Matera",
        "Pistoia",
        "Reggio Emilia",
        "Frosinone",
        "Imperia",
        "Tortolì",
        "Iglesias",
        "Tempio Pausania",
        "Trapani",
        "Rovigo",
        "Teramo",
        "Sondrio",
        "Lanusei",
        "Biella",
        "Cosenza",
        "Cuneo",
        "Ascoli Piceno",
        "Avellino",
        "Chieti",
        "Terni",
        "Varese",
        "Forlì",
        "Lecco",
        "Carbonia",
        "Macerata",
        "La Spezia",
        "Pesaro",
        "Pordenone",
        "Lodi",
        "Brescia",
        "Agrigento"
    ]

    if num_facilities > len(facility_dictionary):
        print(f"Sono state richieste troppe facility, il numero massimo consentito è di: {len(facility_dictionary)}")
        return

    if num_towns > len(towns_dictionary):
        print(f"Sono state richieste troppe facility, il numero massimo consentito è di: {len(towns_dictionary)}")
        return

    facilities = []
    towns = []
    hazards = []

    for i in range(num_facilities):
        facility = {
            "facility_id": i,
            "name": facility_dictionary[i],
            "capacity": math.floor(random.uniform(51, 200))
        }
        facilities.append(facility)

    for i in range(num_towns):
        town = {
            "town_id": i,
            "name": towns_dictionary[i],
            "garbage": math.floor(random.uniform(1, 50))
        }
        towns.append(town)

    for i in range(num_towns):
        town_hazards = []
        for j in range(num_facilities):
            town_hazards.append(math.floor(random.uniform(1, 100)))
        hazards.append(town_hazards)

    data = {
        "towns": towns,
        "facilities": facilities,
        "hazards": hazards
    }

    with open(f"./instances/{file_name}.json", 'w') as outfile:
        json.dump(data, outfile)
