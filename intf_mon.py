#! /usr/bin/env python

import pygal
from snmp_helper import snmp_extract, snmp_get_oid_v3
import time
import line_graph
from pprint import pprint
import pdb

oids = {
        'in_octets':    '1.3.6.1.2.1.2.2.1.10.5',
        'out_octets':   '1.3.6.1.2.1.2.2.1.16.5',
        'in_ucast_pkts':    '1.3.6.1.2.1.2.2.1.11.5',
        'out_ucast_pkts':    '1.3.6.1.2.1.2.2.1.17.5',
    }

snmp_port = 161
username = 'pysnmp'
auth_key = 'galileo1'
encr_key = 'galileo1'

pynet_rtr1 = ('184.105.247.70', snmp_port)
snmp_user = (username, auth_key, encr_key)


def main():
    graph_stats = {
        'in_octets': [],
        'out_octets': [],
        'in_ucast_pkts': [],
        'out_ucast_pkts': [],
    }

    base_value = {}

    for time_interval in range(0, 65, 5):
        for oid in oids.keys():
            snmp_data = snmp_get_oid_v3(pynet_rtr1, snmp_user, oid=oids[oid], auth_proto='sha',
                                        encrypt_proto='aes128', display_errors=True)
            value = snmp_extract(snmp_data)
            base = base_value.get(oid)
            if base:
                graph_stats[oid].append(int(value) - int(base))
            base_value[oid] = value
        pprint(graph_stats)
        time.sleep(10)

    print

    x_labels = []
    for x_label in range(5, 65, 5):
        x_labels.append(str(x_label))

    # Create the graphs
    if line_graph.twoline("pynet-rtr1-octets.svg", "pynet-rtr1 Fa4 Input/Output Bytes",
                          graph_stats["in_octets"], "In Octets", graph_stats["out_octets"],
                          "Out Octets", x_labels):
        print "In/Out Octets graph created"

    if line_graph.twoline("pynet-rtr1-pkts.svg", "pynet-rtr1 Fa4 Input/Output Unicast Packets",
                          graph_stats["in_ucast_pkts"], "In Packets", graph_stats["out_ucast_pkts"],
                          "Out Packets", x_labels):
        print "In/Out Packets graph created"
    print

if __name__ == '__main__':
    main()