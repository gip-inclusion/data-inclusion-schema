import enum
import json
import sys

from data_inclusion.schema import models


class Schema(str, enum.Enum):
    STRUCTURE = "structure"
    SERVICE = "service"


def main():
    kind = Schema(sys.argv[1])

    if kind == Schema.STRUCTURE:
        print(
            json.dumps(
                models.generate_structures_json_schema(),
                indent=2,
            )
        )
    elif kind == Schema.SERVICE:
        print(
            json.dumps(
                models.generate_services_json_schema(),
                indent=2,
            )
        )


if __name__ == "__main__":
    # typical usage:
    # python -m data_inclusion.schema structure > structures.json
    # or
    # python -m data_inclusion.schema service > services.json
    main()
