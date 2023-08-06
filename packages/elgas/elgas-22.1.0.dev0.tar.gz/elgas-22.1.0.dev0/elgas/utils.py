import random
from datetime import datetime


def calculate_lrc(data: bytearray) -> int:
    lrc = 0
    for _byte in data:
        temp = lrc ^ _byte
        lrc = temp & 0xFF
    return lrc & 0xFF


def calculate_checksum(data: bytearray) -> int:
    checksum = 0
    for _byte in data:
        temp = checksum + _byte
        checksum = temp & 0xFF
    return checksum & 0xFF


def calculate_drc(data: bytearray) -> int:
    drc = 0
    for _byte in data:
        temp = drc << 1
        if temp & 0x100:
            temp = temp + 1
        temp = temp & 0xFF
        temp = temp ^ _byte
        drc = temp & 0xFF
    return drc & 0xFF


def escape_characters(data: bytes) -> bytes:
    """
    Characters that are used for telegram control are replaced with others
    so that it easier to parse the message over the wire.
    Final character is never replaced.

    '\x0d' -> '\x1b\x0e'
    '\x1b' -> '\x1b\x1b'
    '\x8d' -> '\x1b\x0f'
    """
    if not data.endswith(b"\x0d"):
        raise ValueError("Data does not end with end-char 0x0D")
    workable_data = data[:-1]
    escaped_data = (
        workable_data.replace(b"\x0d", b"\x1b\x0e")
        .replace(b"\x1b", b"\x1b\x1b")
        .replace(b"\x8d", b"\x1b\x0f")
    )
    return escaped_data + b"\x0d"


def return_characters(data: bytes) -> bytes:
    """
    Characters that are used for telegram control are replaced with others
    so that it easier to parse the message over the wire.
    Final character is never replaced.
    This function returns them to their original form.

    '\x1b\x0e' -> '\x0d'
    '\x1b\x1b' -> '\x1b'
    '\x1b\x0f' -'\x8d'
    """
    if not data.endswith(b"\x0d"):
        raise ValueError("Data does not end with end-char 0x0D")
    workable_data = data[:-1]
    returned_data = (
        workable_data.replace(b"\x1b\x0e", b"\x0d")
        .replace(b"\x1b\x1b", b"\x1b")
        .replace(b"\x1b\x0f", b"\x8d")
    )
    return returned_data + b"\x0d"


def pad_password(password: str):
    """
    Passwords are 6 characters long. But are sent as 10 characters where the last
    4 characters are insignificant.
    """
    possible_chars = "abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ0123456789"
    four_random = random.choices(possible_chars, k=4)
    return password + "".join(four_random)


def bytes_to_datetime(data: bytes) -> datetime:
    """
    BCD of 6 bytes  seconds, minutes, hour, day, month, year
    10 33 12 30 05 06 == 2006-05-30T12:33:10
    """
    if len(data) != 6:
        raise ValueError(f"{data!r} is not a BCD encoded datetime")
    second = from_bcd(data[0:1])
    minute = from_bcd(data[1:2])
    hour = from_bcd(data[2:3])
    day = from_bcd(data[3:4])
    month = from_bcd(data[4:5])
    # The year is only the last 2 digits. We set it so all dates are in the 20xx
    # I will probably be retired when it becomes a problem :)
    year = from_bcd(data[5:]) + 2000

    return datetime(
        year=year, month=month, day=day, hour=hour, minute=minute, second=second
    )


def datetime_to_bytes(timestamp: datetime) -> bytes:
    """
    Packs a datetime into a BCD encoded format
    """
    out = bytearray()
    out.extend(to_bdc(timestamp.second))
    out.extend(to_bdc(timestamp.minute))
    out.extend(to_bdc(timestamp.hour))
    out.extend(to_bdc(timestamp.day))
    out.extend(to_bdc(timestamp.month))
    out.extend(to_bdc(timestamp.year - 2000))

    return bytes(out)


def to_bdc(number: int) -> bytes:
    """
    4 bit bcd (Binary Coded Decimal)
    Example: Decimal 30 would be encoded with b"\x30" or 0b0011 0000
    """
    chars = str(number)
    if (len(chars) % 2) != 0:
        # pad string to make it a hexadecimal one.
        chars = "0" + chars
    bcd = bytes.fromhex(str(chars))
    return bcd


def from_bcd(data: bytes) -> int:
    """
    make a bcd encoded bytestring into an integer
    Example: b"\x30" should be 30
    """
    chars = data.hex()
    return int(chars)
