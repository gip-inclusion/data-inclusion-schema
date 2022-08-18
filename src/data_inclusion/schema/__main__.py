import json

from data_inclusion.schema import models


def main():
    print(
        json.dumps(
            models.generate_structures_json_schema(),
            indent=2,
        )
    )


if __name__ == "__main__":
    # typical usage:
    # python -m data_inclusion.schema > structures.json
    main()
