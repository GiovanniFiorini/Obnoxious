from .facility import Facility


class Town:

    town_id: int
    name: str
    garbage: int
    facility: Facility

    def __init__(self, town_id: int, name: str, garbage: int):
        self.town_id = town_id
        self.name = name
        self.garbage = garbage

    @property
    def get_garbage(self):
        return self.garbage

    @property
    def get_facility(self):
        return self.facility

    @property
    def set_facility(self, facility: Facility):
        self.facility = facility
