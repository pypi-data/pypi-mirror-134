from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Union

from atoti_core import keyword_only_dataclass

from ._parsing_utils import Config, convert_path_to_absolute_string


@keyword_only_dataclass
@dataclass(frozen=True)
class ClientCertificateConfig(Config):
    """The JKS truststore config to enable client certificate authentication (also called mutual TLS or mTLS) on the application.

    This requires :class:`~atoti.config.https.HttpsConfig` to be configured.

    It can be used alongside the other :class:`~atoti.config.authentication.authentication.AuthenticationConfig` providers.
    If a user presents valid certificates they will be authenticated, if not they will have to authenticate using the other configured security provider.

    Opening a query session on a session protected with this config can be done using :class:`atoti_query.client_certificate.ClientCertificate`.

    Example:
        >>> config = {
        ...     "client_certificate": {
        ...         "trust_store": "../truststore.jks",
        ...         "trust_store_password": "secret",
        ...     },
        ...     "https": {
        ...         "certificate": "../cert.p12",
        ...         "password": "secret",
        ...     },
        ... }

        .. doctest::
            :hide:

            >>> validate_config(config)
    """

    trust_store: Union[Path, str]
    """Path to the truststore file generated with the certificate used to sign client certificates."""

    trust_store_password: Optional[str]
    """Password protecting the truststore."""

    username_regex: str = "CN=(.*?)(?:,|$)"
    """Regex to extract the username from the certificate."""

    def __post_init__(self) -> None:
        convert_path_to_absolute_string(self, "trust_store")
