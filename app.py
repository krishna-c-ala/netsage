"""from models.bgp_process import BGPProcess
from models.bgp_neighbor import BGPNeighbor
from parsers.cisco_bgp_parser import ciscoBGPparser




process = BGPProcess()

neighbor = BGPNeighbor()

process.add_neighbor(neighbor)
"""


from parsers.cisco_bgp_parser import ciscoBGPparser
from models.bgp_process import BGPProcess

parser = ciscoBGPparser()

config = """
router bgp 65001
neighbor 10.1.1.1 remote-as 65002
"""

process = parser.parse(config)

print(process.local_as)