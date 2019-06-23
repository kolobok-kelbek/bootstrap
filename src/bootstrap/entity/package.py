from typing import List, Any


class Package:
    __name: str = None
    __description: str = None
    __commands: List[Any] = List

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, dependence: str) -> None:
        self.__description = dependence

    @property
    def commands(self) -> List:
        return self.__commands

    @commands.setter
    def commands(self, commands) -> None:
        self.__commands = commands
