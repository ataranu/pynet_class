#! /usr/bin/env python

import json
import yaml
from pprint import pprint

with open('json.txt') as f:
    pprint(json.load(f))

with open('yaml.txt') as f:
    pprint(yaml.load(f))