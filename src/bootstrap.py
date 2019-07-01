from typing import Any, List, Dict
import json
import threading
import subprocess

DIR_LOG = 'log'
ENC = 'utf-8'
DIR_PAC = 'packages'


class Package:
    NAME_FIELD = 'name'
    DESCRIPTION_FIELD = 'description'
    COMMANDS_FIELD = 'commands'

    __name: str = None
    __description: str = None
    __dependence: str = None
    __commands: List[Any] = List

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str) -> None:
        self.__description = description

    @property
    def dependence(self) -> str:
        return self.__dependence

    @dependence.setter
    def dependence(self, dependence) -> None:
        self.__dependence = dependence

    @property
    def commands(self) -> List:
        return self.__commands

    @commands.setter
    def commands(self, commands) -> None:
        self.__commands = commands

    def hydrate_from_dist(self, data: Dict):
        self.__name = data[self.NAME_FIELD]
        self.__commands = data[self.COMMANDS_FIELD]

        if self.DESCRIPTION_FIELD in data:
            self.__dependence = data[self.DESCRIPTION_FIELD]

        return self

    def to_dist(self) -> Dict:
        return {
            self.NAME_FIELD: self.__name,
            self.DESCRIPTION_FIELD: self.__dependence,
            self.COMMANDS_FIELD: self.__commands
        }

    def get_format_commands(self) -> str:
        return ' && '.join(self.__commands)


class Serializer:

    def serialize(self, string: str) -> Any:
        return json.loads(string)

    def deserialize(self, data: Any) -> str:
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

