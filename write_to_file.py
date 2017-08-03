#! /usr/bin/env python

import json
import yaml


def main():
    my_dict = dict()

    my_list = list()

    my_dict = {
        'item1': 'value1',
        'item2': 'value2'
    }

    my_list = [
        'item1',
        'item2',
        my_dict
    ]

    with open('yaml.txt', 'w') as f:
        f.write(yaml.dump(my_list, default_flow_style=False))

    with open('json.txt', 'w') as f:
        f.write(json.dumps(my_list,))

if __name__ == '__main__':
    main()

