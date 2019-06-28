from typing import Any
from src.entity.package import Package
import json


def json_serialize(string: str) -> Any:
    return json.loads(string)


def json_deserialize(data: Any) -> str:
    return json.dumps(data)


def read(file_name: str) -> str:
    handle = open(file_name)

    return handle.read()


def get_prototype() -> Package:
    return Package()