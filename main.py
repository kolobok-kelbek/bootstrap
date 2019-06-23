#!/usr/bin/python3
import locale
from src.bootstrap.reader import Reader
from src.bootstrap.serializator.json import Json
from src.bootstrap.hydrator.package import Package as PackageHydrator
from src.bootstrap.entity.package import Package


locale.setlocale(locale.LC_ALL, '')

reader = Reader()
data_str = reader.read("packages.json")
json = Json()
data = json.serialize(data_str)

hydrator = PackageHydrator()
prototype = Package()
packageList = []

for package in data['packages']:
    packageList.append(hydrator.hydrate(package, prototype))

print(packageList)
