class BGPProcess:
    def __init__(self):
        self.local_as = None
        self.router_id = None
        self.vrf = None
        
        # collections
        self.neighbors = []
        self.advertised_networks = []   # List of NetworkAdvertisement objects
    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def add_network(self, network):
        self.advertised_networks.append(network)
































