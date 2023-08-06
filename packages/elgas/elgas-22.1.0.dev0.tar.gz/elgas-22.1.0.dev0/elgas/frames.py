from __future__ import annotations

from enum import IntEnum
from functools import lru_cache
from typing import *

from attrs import define, field

from elgas import utils


class ServiceNumber(IntEnum):
    READ_VALUES = 0x64
    WRITE_VALUES = 0x65
    SEARCH_ARCHIVE_POINTERS_OLD = 0x67
    SEARCH_ARCHIVE_POINTERS = 0x7B
    READ_ARCHIVES_OLD = 0x68
    READ_ARCHIVES = 0x7C
    READ_DEVICE_TIME = 0x6C
    READ_SCADA_PARAMETERS = 0x70
    WRITE_DEVICE_TIME = 0x71
    GROUP_WRITE_VALUES = 0x77
    GROUP_READ_VALUES = 0x79
    CALL = 0x87
    READ_ARCHIVES_BY_DATE_OLD = 0x91
    READ_ARCHIVES_BY_DATE = 0x7D


@define(auto_attribs=True)
class Request:
    TYPE: ClassVar[int] = 0x84
    service: ServiceNumber
    destination_address_1: int
    destination_address_2: int
    source_address_1: int
    source_address_2: int
    data: bytes

    ...

    @property
    def length(self) -> int:
        """
        All bytes are counted except STX, before replacing reserved characters
        """
        return len(self.data) + 15

    def to_bytes(self) -> bytes:
        out = bytearray()
        out.append(0x02)
        out.append(0xFE)
        out.append(self.TYPE)
        out.append(self.service)
        out.extend(self.length.to_bytes(2, "big"))
        out.extend(self.destination_address_1.to_bytes(2, "big"))
        out.append(self.destination_address_2)
        out.extend(self.source_address_1.to_bytes(2, "big"))
        out.append(self.source_address_2)
        out.extend(self.data)
        redundancy_source = out[1:]
        out.append(utils.calculate_lrc(redundancy_source))
        out.append(utils.calculate_checksum(redundancy_source))
        out.append(utils.calculate_drc(redundancy_source))
        out.append(0x0D)

        return bytes(out)


@define
class Response:
    TYPE: ClassVar[int] = 0x86
    service: ServiceNumber
    destination_address_1: int
    destination_address_2: int
    source_address_1: int
    source_address_2: int
    data: bytes

    @property
    def length(self) -> int:
        """
        All bytes are counted except STX, before replacing reserved characters
        """
        return len(self.data) + 15

    def to_bytes(self) -> bytes:
        out = bytearray()
        out.append(0x02)
        out.append(0xFE)
        out.append(self.TYPE)
        out.append(self.service)
        out.extend(self.length.to_bytes(2, "big"))
        out.extend(self.destination_address_1.to_bytes(2, "big"))
        out.append(self.destination_address_2)
        out.extend(self.source_address_1.to_bytes(2, "big"))
        out.append(self.source_address_2)
        out.extend(self.data)
        redundancy_source = out[1:]
        out.append(utils.calculate_lrc(redundancy_source))
        out.append(utils.calculate_checksum(redundancy_source))
        out.append(utils.calculate_drc(redundancy_source))
        out.append(0x0D)

        return bytes(out)


@define
class EncryptedRequest:
    TYPE: ClassVar[int] = 0x85
    service: ServiceNumber
    destination_address_1: int
    destination_address_2: int
    source_address_1: int
    source_address_2: int
    data: bytes

    ...

    @property
    def length(self) -> int:
        """
        All bytes are counted except STX, before replacing reserved characters
        """
        pass


@define
class EncryptedResponse:
    TYPE: ClassVar[int] = 0x87
    service: ServiceNumber
    destination_address_1: int
    destination_address_2: int
    source_address_1: int
    source_address_2: int
    data: bytes

    ...

    @property
    def length(self) -> int:
        """
        All bytes are counted except STX, before replacing reserved characters
        """
        pass
