class Facility:

    facility_id: int
    name: str
    capacity: int
    is_open: bool

    def __init__(self,  facility_id: int, name: str, capacity: int, is_open: bool = False):
        self.facility_id = facility_id
        self.name = name
        self.capacity = capacity
        self.is_open = is_open


