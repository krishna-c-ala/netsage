from search.search_types import SearchType


class SearchRouter:

    SUPPORTED_SECTIONS = {
        "bgp",
        "ospf",
        "eigrp",
        "isis",
        "aaa",
        "ntp",
        "snmp",
        "logging",
        "hsrp",
        "vrrp",
        "stp",
    }

    def classify(self, query):

        query = query.strip().lower()

        if query in self.SUPPORTED_SECTIONS:
            return SearchType.SECTION

        return SearchType.KEYWORD