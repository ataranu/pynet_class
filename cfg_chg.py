#! /usr/bin/env python

import json
from snmp_helper import snmp_get_oid_v3, snmp_extract
import time
from pprint import pprint
from email_helper import send_mail
import pdb

ccmHistoryRunningLastChanged = '1.3.6.1.4.1.9.9.43.1.1.1.0'
ccmHistoryRunningLastSaved = '1.3.6.1.4.1.9.9.43.1.1.2.0'
ccmHistoryStartupLastChanged = '1.3.6.1.4.1.9.9.43.1.1.3.0'
sysUptime = '1.3.6.1.2.1.1.3.0'
sysName = '1.3.6.1.2.1.1.5.0'
snmp_port = 161
username = 'pysnmp'
auth_key = 'galileo1'
encr_key = 'galileo1'


def compare(old_devices, devices):
    for device in devices.keys():
        if devices[device][1] < old_devices[device][1]:
            msg = "{device} rebooted".format(device=devices[device][0])
            send_mail('taranu.vector@gmail.com', 'Router Alert!', msg, 'pynet_lab@example.com')
        elif devices[device][2] != old_devices[device][2]:
            msg = "{device} config changed".format(device=devices[device][0])
            send_mail('taranu.vector@gmail.com', 'Router Alert!', msg, 'pynet_lab@example.com')


def main():
    pynet_rtr1 = ('184.105.247.70', snmp_port)
    pynet_rtr2 = ('184.105.247.71', snmp_port)

    snmp_user = (username, auth_key, encr_key)

    old_devices = {pynet_rtr1[0]: [], pynet_rtr2[0]: []}
    first = True

    while True:
        devices = {pynet_rtr1[0]: [], pynet_rtr2[0]: []}
        for device in (pynet_rtr1, pynet_rtr2):
            for oid in (sysName, sysUptime, ccmHistoryRunningLastChanged):
                snmp_data = snmp_get_oid_v3(device, snmp_user, oid=oid, auth_proto='sha',
                                encrypt_proto='aes128', display_errors=True)
                devices[device[0]].append(snmp_extract(snmp_data))
        if first == False:
            compare(old_devices, devices)

        pprint(devices)

        old_devices = devices
        first = False

        time.sleep(300)

if __name__ == '__main__':
    main()
