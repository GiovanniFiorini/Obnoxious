class Facility:

    facility_id: int
    name: str
    capacity: int

    def __init__(self,  facility_id: int, name: str, capacity: int):
        self.facility_id = facility_id
        self.name = name
        self.capacity = capacity
