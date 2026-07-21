class BGPProcess:

    def __init__(self):
        self.local_as = None
        self.router_id = None
        self.vrf = None

        self.neighbors = []
        self.advertised_networks = []

        # Original BGP configuration section
        self.config_lines = []


    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)


    def find_neighbor(self, ip_address):

        for neighbor in self.neighbors:
            if neighbor.ip_address == ip_address:
                return neighbor

        return None


    def add_network(self, network):
        self.advertised_networks.append(network)

"""
Instead of the parser knowing how neighbors are stored, it simply asks the BGPProcess:

"Find me the neighbor with this IP."

This is called encapsulation.
"""
































