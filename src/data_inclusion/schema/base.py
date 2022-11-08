import enum
import textwrap


class EnhancedEnum(str, enum.Enum):
    def __new__(cls, value, label, description):
        obj = str.__new__(cls, [value])
        obj._value_ = value
        obj.label = label
        obj.description = (
            textwrap.dedent(description).strip("\n").replace("\n", " ")
            if description
            else None
        )

        try:
            if obj.description is not None:
                if not obj.description[0].isupper():
                    raise ValueError("description must start with uppercase letter")
        except ValueError as err:
            raise ValueError(f"{cls.__name__}({value})'s {err}")

        return obj
