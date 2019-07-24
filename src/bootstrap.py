from typing import Any, List, Dict
from multiprocessing.pool import ThreadPool
import json
import subprocess
import glob
import os


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


class PackageList:
    __name: str = None
    __list: List[Package] = List


class Serializer:

    @staticmethod
    def serialize(string: str) -> Any:
        return json.loads(string)

    @staticmethod
    def deserialize(data: Any) -> str:
        return json.dumps(data)


class Reader:
    @staticmethod
    def read_package(file_name: str) -> Dict:
        handle = open(file_name)

        return Serializer.serialize(handle.read())

    @staticmethod
    def read_packages(template: str) -> List:
        data_list = []

        for pkg_file in glob.glob(template):
            for pkg in Reader.read_package(pkg_file):
                prototype = Package()
                prototype.hydrate_from_dist(pkg)
                data_list.append(prototype)

        return data_list


class Processor:
    ENC = 'utf-8'
    TEMPLATE = "packages/*.pkg.json"

    def process(self, package: Package) -> None:
        pkg_name = package.name.lower().replace(" ", "")
        dir_log = Logger.DIR_LOG + '/' + pkg_name
        if not os.path.exists(dir_log):
            os.mkdir(dir_log)

        stdout = open('%s/%s/out.log' % (Logger.DIR_LOG, pkg_name), 'w+')
        stderr = open('%s/%s/err.log' % (Logger.DIR_LOG, pkg_name), 'w+')

        p = subprocess.Popen(package.get_format_commands(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        out, err = p.communicate()

        stdout.write(out.decode(self.ENC))
        stderr.write(err.decode(self.ENC))

        stdout.close()
        stderr.close()

    def run(self) -> None:
        package_list = Reader.read_packages(self.TEMPLATE)

        pool = ThreadPool()
        pool.map(self.process, package_list)

        pool.close()
        pool.join()


class Logger:
    DIR_LOG = 'log'
