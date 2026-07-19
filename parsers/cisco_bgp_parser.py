from models.bgp_process import BGPProcess


class ciscoBGPparser:
    def __init__(self):
        pass

    def parse(self, config):
        process = BGPProcess

        for line in config.splitlines():
            line = line.strip()
            if line.startswith("router bgp"):
                parts = line.split()
                process.local_as = parts[2]
        return process
    

#return = give data/object back to the caller

#print = display something to a human