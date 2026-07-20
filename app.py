"""from models.bgp_process import BGPProcess
from models.bgp_neighbor import BGPNeighbor
from parsers.cisco_bgp_parser import ciscoBGPparser




process = BGPProcess()

neighbor = BGPNeighbor()

process.add_neighbor(neighbor)
"""

from models.bgp_neighbor import BGPNeighbor
from parsers.cisco_bgp_parser import ciscoBGPParser
from models.bgp_process import BGPProcess

parser = ciscoBGPParser()

config = """
router bgp 65001
neighbor 10.1.1.1 remote-as 65002
"""

process = parser.parse(config)

print("Local AS:", process.local_as)

for neighbor in process.neighbors:
    print("Neighbor:", neighbor.ip_address)
    print("Remote AS:", neighbor.remote_as)