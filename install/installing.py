import os
import simplejson as json
import click
from dialog import Dialog

class Installing:

    def getPackages(self):
        str = open("./packages.json", "r").read()
        data = json.loads(str)
        return data["packages"]

    def go(self):
        pkgs = self.getPackages()
        selected = self.checkingPackages(pkgs)
        for indexPkg in pkgs:
            for indexCommand in indexPkg["commands"]:
                if indexPkg["name"] in selected:
                    try:
                        os.system(indexCommand)
                        click.echo(click.style("Package " + indexPkg["name"] + " is installed", fg="green"))
                    except:
                        click.echo(click.style("Package " + indexPkg["name"] + " is not installed", fg="red"))
        return

    def checkingPackages(self, pkgs):
        d = Dialog(dialog="dialog")
        d.set_background_title("Installer program")

        pkgChecklist = []

        for pkg in pkgs:
            pkgChecklist.append((pkg["name"], "", True))

        code, tags = d.checklist("What installing?",
                                 choices=pkgChecklist,
                                 title="Installer program")
        if code == d.OK:
            return tags
        self.clear()
        quit()

    def systemUpdate(self):
        os.system("apt-get update")

    def clear(self):
        os.system("clear")