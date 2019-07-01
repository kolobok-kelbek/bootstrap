#!/usr/bin/python3
import locale
from src.bootstrap import *
from multiprocessing.pool import ThreadPool

TEMPLATE = "packages/*.pkg.json"

locale.setlocale(locale.LC_ALL, '')

packageList = Reader.read_packages(TEMPLATE)

pool = ThreadPool()
pool.map(process, packageList)

pool.close()
pool.join()

