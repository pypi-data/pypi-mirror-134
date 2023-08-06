import datetime
from enum import IntEnum
from typing import *

from attrs import define, field

from elgas.frames import ServiceNumber


class Archive(IntEnum):
    EXTREME = 0
    DATA = 1
    BINARY = 2
    DAILY = 3
    MONTHLY = 4
    SETTING = 5
    FAST_1 = 6
    FAST_2 = 7
    STATUS = 8
    BILLING = 9
    GAS_COMPOSITION = 10


@define
class ReadActualValuesRequest:
    """
    Will request a readout of all current parameters in the device
    """

    password: str


@define
class ReadActualValuesResponse:
    """
    A long datastructure of parameters that depends on the firmware of the device
    """

    ...


@define
class ReadActualValuesResponseV1:
    """
    For firmware versions < 1.18
    """

    ...


@define
class ReadActualValuesResponseV2:
    """
    For firmware versions  1.18 < fwv < 1.99
    """

    ...


@define
class ReadActualValuesResponseV3:
    """
    For firmware versions > 2.00 and Elcor gen 4
    """

    ...


@define
class ReadTimeRequest:
    """
    Request for the device's time. It contains no data.
    """

    SERVICE_GROUP: ClassVar[ServiceNumber] = ServiceNumber.READ_DEVICE_TIME


@define
class ReadTimeResponse:
    """
    Contains the device time
    """

    time: datetime
    data_access_result: bytes
