"""
from models.bgp_process import BGPProcess
from models.bgp_neighbor import BGPNeighbor
from parsers.cisco_bgp_parser import ciscoBGPparser




process = BGPProcess()

neighbor = BGPNeighbor()

process.add_neighbor(neighbor)


from models.bgp_neighbor import BGPNeighbor
from parsers.cisco_bgp_parser import ciscoBGPParser
from models.bgp_process import BGPProcess

config = 
router bgp 65001
neighbor 10.1.1.1 remote-as 65002
neighbor 10.1.1.1 description AWS Primary



parser = ciscoBGPParser()

process = parser.parse(config)


print("========== Configuration ==========")

for line in process.config_lines:
    print(line)


print("\n========== Context Configuration ==========")

for neighbor in process.neighbors:

    for line in neighbor.config_lines:
       print(line)
"""

from parsers.cisco_bgp_parser import ciscoBGPParser
from search.search_router import SearchRouter


config = """
router bgp 65001
 neighbor 10.1.1.1 remote-as 65002
 neighbor 10.1.1.1 description AWS Primary
"""


query = input("Search: ")


router = SearchRouter()

search_type = router.classify(query)

print("\nSearch Type:", search_type.value)


parser = ciscoBGPParser()

process = parser.parse(config)


print("\n========== Configuration ==========")

for line in process.config_lines:
    print(line)


print("\n========== Context Configuration ==========")

for neighbor in process.neighbors:
    for line in neighbor.config_lines:
        print(line)