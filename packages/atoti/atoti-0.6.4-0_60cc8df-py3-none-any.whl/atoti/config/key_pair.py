from dataclasses import dataclass

from atoti_core import keyword_only_dataclass

from ._parsing_utils import Config


@keyword_only_dataclass
@dataclass(frozen=True)
class KeyPairConfig(Config):
    public_key: str
    """The public key."""

    private_key: str
    """The private key."""
