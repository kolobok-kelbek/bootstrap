import sys
import platform
import os
import subprocess
from click import echo, style, confirm

class System:

    def verified(self):
        self.verifiedVersion()
        self.verifiedRoot()
        self.userActive()
        return

    def userActive(self):
        if not confirm('Do you want to continue?'):
            quit()

    def verifiedVersion(self):
        if sys.version_info < (3, 5, 3):
            echo(style(u"This python version is " + platform.python_version(), fg="red"))
            echo(u"Minimal version for script work - 3.5.3.")
            quit()

    def verifiedRoot(self):
        if os.geteuid() != 0:
            echo(style("We're not root!", fg="red"))
            subprocess.call(['sudo', 'python3', *sys.argv])
            quit()

    def createTmpDir(self):
        directory = 'tmp'
        if not os.path.exists(directory):
            os.makedirs(directory)