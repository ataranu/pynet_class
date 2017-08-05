#! /usr/bin/env/ python

from snmp_helper import snmp_get_oid,snmp_extract



def main():
    community = 'galileo'
    port = 161

    device1 = ('cisco1.twb-tech.com', community, port)
    device2 = ('cisco2.twb-tech.com', community, port)


    sysDescr = '1.3.6.1.2.1.1.1.0'
    sysName = '1.3.6.1.2.1.1.5.0'

    print(30*'=')
    snmp_data = snmp_get_oid(device1, oid=sysName, display_errors=True)
    print(snmp_extract(snmp_data) + '\n')
    snmp_data = snmp_get_oid(device1, oid=sysDescr, display_errors=True)
    print(snmp_extract(snmp_data))
    print(30 * '=')
    snmp_data = snmp_get_oid(device2, oid=sysName, display_errors=True)
    print(snmp_extract(snmp_data) + '\n')
    snmp_data = snmp_get_oid(device2, oid=sysDescr, display_errors=True)
    print(snmp_extract(snmp_data))
    

if __name__ == '__main__':
    main()