

class Facility:

    facility_id: int
    name: str
    capacity: int

    def __init__(self,  facility_id: int, name: str, capacity: int, hazards: list):
        self.facility_id = facility_id
        self.name = name
        self.capacity = capacity

    @property
    def get_capacity(self):
        return self.capacity
