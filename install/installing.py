import os
import subprocess
import simplejson as json
from dialog import Dialog

class Installing:

    line = "------------------------------------------------"

    fieldName = "name"
    fieldOut = "out"
    fieldMessage = "message"
    fieldStatus = "status"
    fieldPkgs = "packages"
    fieldCommands = "commands"
    fieldDependence = "dependence"

    messageSuccess = "is installed"
    messageFeiled = "is failed"
    messageNoInstalled = "is not installed"

    file = "./packages.json"

    pkgs = []
    dialog = Dialog(dialog="dialog")

    def initPkgs(self):
        for pkg in self.pkgs:
            pkg[self.fieldOut] = ''
            pkg[self.fieldMessage] = self.messageNoInstalled
            pkg[self.fieldStatus] = False

    def getPackages(self):
        str = open(self.file, "r").read()
        data = json.loads(str)
        self.pkgs = data[self.fieldPkgs]
        self.initPkgs()

    def go(self):
        self.getPackages()
        selected = self.checkingPackages(self.pkgs)
        for pkg in self.pkgs:
            for command in pkg[self.fieldCommands]:
                if pkg[self.fieldName] in selected:
                    pkgName = pkg[self.fieldName]
                    tmp = "No information"
                    try:
                        tmp = self.exec(command)
                        self.clear()
                        self.outDataSetToPkgs(tmp, True, self.messageSuccess, pkgName)
                    except:
                        self.clear()
                        self.outDataSetToPkgs(tmp, False, self.messageFeiled, pkgName)
        self.outData()
        return

    def checkingPackages(self, pkgs):
        self.dialog.set_background_title("Installer program")

        pkgChecklist = []

        for pkg in pkgs:
            pkgChecklist.append((pkg[self.fieldName], "", True))

        code, tags = self.dialog.checklist("What installing?", choices=pkgChecklist, title="Installer program")
        if code == self.dialog.OK:
            return tags
        self.clear()

    def systemUpdate(self):
        os.system("apt-get update")

    def clear(self):
        os.system("clear")

    def exec(self, command):
        outFull = []
        out = subprocess.check_output(command, shell=True)
        out = str(out)
        out = out.split('\'')[1]
        out = out.split('\\n')
        del out[-1]
        outFull.append(self.line)
        outFull.append(command)
        outFull.append(self.line)
        for outLine in out:
            outFull.append(outLine)
        outFull.append(self.line)
        return outFull

    def outDataSetToPkgs(self, data, status, message, pkgName):
        for pkg in self.pkgs:
            if (pkg[self.fieldName] == pkgName):
                pkg[self.fieldOut] = data
                pkg[self.fieldStatus] = status
                pkg[self.fieldMessage] += message
                break

    def outData(self):
        menuData = []

        for pkg in self.pkgs:
            menuData.append((pkg[self.fieldName], pkg[self.fieldMessage]))

        code, tag = self.dialog.menu("View details", choices=menuData)
        self.clear()
        if code == self.dialog.OK:
            for pkg in self.pkgs:
                if (pkg[self.fieldName] == tag):
                    if pkg[self.fieldStatus]:
                        os.system("echo \"" + self.outDataToString(pkg[self.fieldOut]) + "\" | less")
                    else:
                        os.system("echo \"" + self.messageNoInstalled + "\" | less")
                    break
            self.outData()

    def outDataToString(self, outData):
        str = ""
        for line in outData:
            str += line + "\n"
        return str
