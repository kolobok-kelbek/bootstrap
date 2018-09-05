#!/usr/bin/python3
import locale
from system import system
from install import installing as inst

locale.setlocale(locale.LC_ALL, '')

systemObj = system.System()
systemObj.verified()
systemObj.createTmpDir()

instObj = inst.Installing()
instObj.go()