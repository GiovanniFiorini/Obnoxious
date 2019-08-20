from .facility import Facility
from .town import Town


class Hazard:

    facility: Facility
    town: Town
    value: int

    def __init__(self, facility: Facility, town: Town, value: int):
        self.facility = facility
        self.town = town
        self.value = value

    @property
    def get_value(self):
        return self.value
