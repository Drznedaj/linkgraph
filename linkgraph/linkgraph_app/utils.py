from enum import IntEnum


class ArticleStatusTypes(IntEnum):
    NOT_REVIEWED = 1
    APPROVED = 2
    REJECTED = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
