#!/usr/bin/python3
import locale
from src.bootstrap import *


locale.setlocale(locale.LC_ALL, '')

data_str = read_package("packages.json")
data = json_serialize(data_str)

packageList = []

for packageData in data['packages']:
    package = get_prototype()
    package.hydrate_from_dist(packageData)
    packageList.append(package)

for package in packageList:
    print(package.get_format_commands())
