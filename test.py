from commons.setup_vars import setup
from heuristics.mhf_greedy import mhf_greedy


facilities, towns, hazards = setup("./instances/basic.json")

c_fac, o_fac, un_town, as_town = mhf_greedy(facilities, towns, hazards)

