from dataclasses import dataclass
from typing import List

from stor.util.ints import uint8, uint32
from stor.util.streamable import Streamable, streamable


@dataclass(frozen=True)
@streamable
class WalletInfo(Streamable):
    """
    This object represents the wallet data as it is stored in DB.
    ID: Main wallet (Standard) is stored at index 1, every wallet created after done has auto incremented id.
    Name: can be a user provided or default generated name. (can be modified)
    Type: is specified during wallet creation and should never be changed.
    Data: this filed is intended to be used for storing any wallet specific information required for it.
    (RL wallet stores origin_id, admin/user pubkey, rate limit, etc.)
    This data should be json encoded string.
    """

    id: uint32
    name: str
    type: uint8  # WalletType(type)
    data: str


@dataclass(frozen=True)
@streamable
class WalletInfoBackup(Streamable):
    """
    Used for transforming list of WalletInfo objects into bytes.
    """

    wallet_list: List[WalletInfo]
