from typing import Any
from src.bootstrap.entity.package import Package as Entity


class Package:
    NAME_FIELD = 'name'
    DESCRIPTION_FIELD = 'description'
    COMMANDS_FIELD = 'commands'

    def hydrate(self, data: Any, entity: Entity) -> Entity:
        entity.name = data[self.NAME_FIELD]
        if self.DESCRIPTION_FIELD in data:
            entity.dependence = data[self.DESCRIPTION_FIELD]
        entity.commands = data[self.COMMANDS_FIELD]

        return entity
