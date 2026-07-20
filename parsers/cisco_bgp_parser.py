from models.bgp_process import BGPProcess
from models.bgp_neighbor import BGPNeighbor


class ciscoBGPParser:

    def __init__(self):
        pass

    def parse(self, config):

        process = BGPProcess()

        for line in config.splitlines():

            line = line.strip()

            # Parse Local AS
            if line.startswith("router bgp"):

                parts = line.split()

                process.local_as = parts[2]

            # Parse Neighbor Remote-AS
            if line.startswith("neighbor"):

                parts = line.split()

                if len(parts) >= 4 and parts[2] == "remote-as":

                    neighbor = BGPNeighbor(
                        ip_address=parts[1],
                        remote_as=parts[3]
                    )

                    process.add_neighbor(neighbor)

        return process
    

#return = give data/object back to the caller

#print = display something to a human