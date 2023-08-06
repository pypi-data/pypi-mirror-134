from enum import IntEnum


class EncryptionKeyId(IntEnum):
    FACTORY = 1
    TEMPORARY = 2
    ADMINISTRATOR = 3
    MAINTENANCE = 4
    USER_1 = 5
    USER_2 = 6
    USER_3 = 7


def encrypt(data: bytes, key: bytes, key_id: int):
    ...


def decrypt(data: bytes, key: bytes, key_id: int):
    ...
