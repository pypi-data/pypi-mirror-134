from dataclasses import dataclass

from stor.types.blockchain_format.coin import Coin
from stor.types.blockchain_format.sized_bytes import bytes32
from stor.util.ints import uint32
from stor.wallet.util.wallet_types import WalletType


@dataclass(frozen=True)
class WalletCoinRecord:
    """
    These are values that correspond to a CoinName that are used
    in keeping track of the unspent database.
    """

    coin: Coin
    confirmed_block_height: uint32
    spent_block_height: uint32
    spent: bool
    coinbase: bool
    wallet_type: WalletType
    wallet_id: int

    def name(self) -> bytes32:
        return self.coin.name()
