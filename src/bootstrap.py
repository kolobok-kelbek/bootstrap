from typing import Any, List
from src.entity.package import Package
import json
import threading
import subprocess

DIR_LOG = 'log'
ENC = 'utf-8'
DIR_PAC = 'packages'


def json_serialize(string: str) -> Any:
    return json.loads(string)


def json_deserialize(data: Any) -> str:
    return json.dumps(data)


def read_package(file_name: str) -> str:
    handle = open(DIR_PAC + '/' + file_name)

    return handle.read()


def read_packages() -> List:
    list = []

    

    return list


def get_prototype() -> Package:
    return Package()


class ProcessorThread(threading.Thread):
    def __init__(self, package: Package):
        threading.Thread.__init__(self)
        self.package = package

    def run(self) -> None:
        self.process()

    def process(self) -> None:
        stdout = open('%s/%s.out.log' % (DIR_LOG, self.package.name), 'w+')
        stderr = open('%s/%s.err.log' % (DIR_LOG, self.package.name), 'w+')

        p = subprocess.Popen(
            self.package.get_format_commands(),
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        out, err = p.communicate()

        stdout.write(out.decode(ENC))
        stderr.write(err.decode(ENC))

        stdout.close()
        stderr.close()


