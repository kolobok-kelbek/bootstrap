import json
from typing import Any


class Json:

    def serialize(self, string: str) -> Any:
        return json.loads(string)

    def deserialize(self, data: Any) -> str:
        return json.dumps(data)
