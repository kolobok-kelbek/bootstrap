from typing import List, Any, Dict


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

    def from_dist(self, data: Dict):
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
