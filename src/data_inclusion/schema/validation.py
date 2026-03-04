from contextlib import contextmanager

import pydantic
import pydantic_core


@contextmanager
def avertissement(info: pydantic.ValidationInfo):
    ignore_warnings = info.context is None or info.context.get("ignore_warnings", True)

    try:
        yield
    except ValueError as exc:
        if ignore_warnings:
            return
        raise pydantic_core.PydanticCustomError("avertissement", str(exc))
