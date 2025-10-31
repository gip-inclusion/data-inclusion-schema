import enum
from typing import Any

from pydantic import ValidationInfo


class Mode(str, enum.Enum):
    NORMAL = "normal"
    STRICT = "strict"


def avertissement(func):
    def wrapper(cls, value: Any, info: ValidationInfo) -> Any:
        is_strict = (
            isinstance(info.context, dict) and info.context.get("mode") == Mode.STRICT
        )

        try:
            return func(cls, value)
        except ValueError as exc:
            if is_strict:
                raise exc from exc
            else:
                return value

    return wrapper
