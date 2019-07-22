# bootstrap v0.2.0
##### System for installation software in ubuntu/mint Linux.

Package configuration file "IPP" (Install Packages Protocol):<br>
```JSON
[
  {
    "name": "package name",
    "description": "description",
    "dependencies": [
        "dependency package name"
    ],
    "commands": [
      "wget https://download.teamviewer.com/download/linux/teamviewer_amd64.deb",
      "sudo dpkg -i teamviewer_amd64.deb",
      "sudo rm teamviewer_amd64.deb"
    ],
    "deb": {
      "link": "http://link"
    },
    "apt": {
      "pkg_name": "package name"
    },
    "snap": {
      "pkg_name": "package name"
    }
  }
]
```