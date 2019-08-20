from .facility import Facility


class Town:

    town_id: int
    name: str
    garbage: int
    facility: Facility

    def __init__(self, town_id: int, name: str, garbage: int, facility: Facility = None):
        self.town_id = town_id
        self.name = name
        self.garbage = garbage
        self.facility = facility
