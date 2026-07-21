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

config = """
router bgp 65001
neighbor 10.1.1.1 remote-as 65002
neighbor 10.1.1.1 description AWS Primary
"""


parser = ciscoBGPParser()

process = parser.parse(config)


print("========== Configuration ==========")

for line in process.config_lines:
    print(line)


print("\n========== Context Configuration ==========")

for neighbor in process.neighbors:

    for line in neighbor.config_lines:
       print(line)