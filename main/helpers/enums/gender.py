from enum import Enum


class GenderEnum(Enum):
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"

    @classmethod
    def choices(cls):
        return [
            (
                key.value,
                key.name,
            )
            for key in cls
        ]
