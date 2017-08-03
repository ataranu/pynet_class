#! /usr/bin/env python

from ciscoconfparse import CiscoConfParse
from pprint import pprint


def pprint_cfg(configs):
    for config in configs:
        print config.text
        for child in config.children:
            print child.text


def main():
    cisco_cfg = CiscoConfParse('cisco_ipsec.txt')

    crypto_maps = cisco_cfg.find_objects(r'^crypto map')
    pprint_cfg(crypto_maps)
    pprint(20*'+')

    filtered_crypto_map = cisco_cfg.find_objects_w_child(r'crypto map', r'pfs group2')
    pprint_cfg(filtered_crypto_map)
    pprint(20 * '+')

    not_aes_crypto_maps = cisco_cfg.find_objects_wo_child(r'^crypto map', r'AES')
    pprint_cfg(not_aes_crypto_maps)

    #pprint(crypto_maps)


if __name__ == '__main__':
    main()