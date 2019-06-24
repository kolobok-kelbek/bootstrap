from typing import List, Any


class Package:
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
