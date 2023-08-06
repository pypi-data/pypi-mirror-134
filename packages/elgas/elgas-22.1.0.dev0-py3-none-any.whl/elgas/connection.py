from __future__ import annotations

from attrs import define, field, validators
from security import EncryptionKeyId


@define
class ElgasConnection:
    """
    address1 is used for addressing measuring place  0-65535
    address2 is used for addressing concrete measuring place 0-255
    TODO: exactly what does that mean?..
    Address 0 in any will make all devices respond. In the response the correct
    address will be sent.


    """

    source_address_1: int = field(validator=[validators.ge(0), validators.le(65535)])
    source_address_2: int = field(validator=[validators.ge(0), validators.le(255)])
    destination_address_1: int = field(
        validator=[validators.ge(0), validators.le(65535)]
    )
    destination_address_2: int = field(validator=[validators.ge(0), validators.le(255)])
    encryption_key: bytes | None = field(default=None)
    encryption_key_id: EncryptionKeyId | None = field(default=None)
    # TODO: Validate that there is an encryption key id if there is an encryption key.

    password: str = field(validator=[validators.max_len(6)])
    password_id: int = field(validator=[validators.ge(801), validators.le(849)])
