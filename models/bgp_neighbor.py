"""
The Class is the blank form. It just defines what pieces of information you need to collect 
(e.g., Company Name, Role, Date Applied). The blank form itself doesn't contain anyone's data yet; it’s just the structure.

The Object is a filled-out form. When you take that blank form and write "Google, Program Manager, July 18th" on it, you have created an actual, 
specific instance of that form.

class BGPNeighbor:
#    pass        #pass doesn nothing and just a placeholder.
    def __init__(self):
        self.ip_address = None
        self.remote_as = None
        self.description = None
        self.update_source = None   
        self.route_map_in = None
        self.route_map_out = None
"""

class BGPNeighbor:

    def __init__(
        self,
        ip_address=None,
        remote_as=None,
        description=None,
        update_source=None,
        route_map_in=None,
        route_map_out=None
    ):
        self.ip_address = ip_address
        self.remote_as = remote_as
        self.description = description
        self.update_source = update_source
        self.route_map_in = route_map_in
        self.route_map_out = route_map_out

        # Original CLI commands related to this neighbor
        self.config_lines = []





