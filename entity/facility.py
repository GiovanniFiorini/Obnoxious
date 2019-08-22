class Facility:
    """
    The Facility object represent a single facility

    Args:
        facility_id (int): set the id
        name (str): set the name
        capacity (int): set the capacity
        total_hazard (int): set the total hazard caused by facility
        is_open (bool): when created is false

    Attributes:
        facility_id (int): the id of the facility
        name (str): the name of the facility
        capacity (int): the capacity of the facility
        total_hazard (int): the total hazard caused by facility
        is_open (bool): True if the facility is open, False otherwise
    """

    def __init__(self,  facility_id: int, name: str, capacity: int, total_hazard: int, is_open: bool = False):
        self.facility_id = facility_id
        self.name = name
        self.capacity = capacity
        self.total_hazard = total_hazard
        self.is_open = is_open


