from models.bgp_process import BGPProcess
from models.bgp_neighbor import BGPNeighbor
from models.Network_Advertisement import NetworkAdvertisement

process = bgp_Process()

neighbor1 = bgp_neighbor()
neighbor2 = bgp_neighbor()

process.add_neighbor(neighbor1)
process.add_neighbor(neighbor2)