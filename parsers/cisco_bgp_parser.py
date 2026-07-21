from models.bgp_process import BGPProcess
from models.bgp_neighbor import BGPNeighbor


class ciscoBGPParser:

    def __init__(self):
        pass
    def get_or_create_neighbor(self, process, ip_address):

        neighbor = process.find_neighbor(ip_address)

        if neighbor is None:

            neighbor = BGPNeighbor(
                ip_address=ip_address
            )

            process.add_neighbor(neighbor)

        return neighbor
    def parse(self, config):

        process = BGPProcess()

        for line in config.splitlines():

            line = line.strip()

            if not line:
                continue


            parts = line.split()


            # Parse BGP process
            if line.startswith("router bgp"):

                process.local_as = parts[2]

                process.config_lines.append(line)


            # Parse neighbor remote-as
            elif line.startswith("neighbor"):

                if len(parts) >= 4 and parts[2] == "remote-as":

                    neighbor = self.get_or_create_neighbor(
                        process,
                        parts[1]
                    )

                    neighbor.remote_as = parts[3]

                    neighbor.config_lines.append(line)
                    process.config_lines.append(line)


                # Parse neighbor description
                elif len(parts) >= 4 and parts[2] == "description":

                    neighbor = self.get_or_create_neighbor(
                        process,
                        parts[1]
                    )

                    neighbor.description = " ".join(parts[3:])

                    neighbor.config_lines.append(line)
                    process.config_lines.append(line)


        return process
#return = give data/object back to the caller

#print = display something to a human