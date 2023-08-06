import sys

from atoti_core import BaseSession
from typing_extensions import Final

# pylint: disable=wrong-import-position
from ._runtime_type_checking_utils import _instrument_typechecking, typecheck

# This needs to be done here so that the runtime type checking decoration can be done before evaluating any classes inheriting from `BaseSession`.
# Otherwise the monkey-patching mechanism used by plugins will target the incorrect method references.
typecheck(BaseSession)

from atoti_query import (
    BasicAuthentication as BasicAuthentication,
    TokenAuthentication as TokenAuthentication,
)

from . import (  # pylint: disable=redefined-builtin
    _functions,
    agg as agg,
    array as array,
    comparator as comparator,
    config as config,
    experimental as experimental,
    math as math,
    query as query,
    scope as scope,
    string as string,
    type as type,
)
from ._compatibility import check_python_version
from ._functions import *  # pylint: disable=redefined-builtin
from ._java_utils import retrieve_info_from_jar
from ._licensing import (
    EULA as __license__,
    check_license,
    hide_new_license_agreement_message as hide_new_license_agreement_message,
)
from ._plugins import register_active_plugins
from ._sessions import Sessions
from ._telemetry import telemeter
from ._tutorial import copy_tutorial
from ._version import VERSION as __version__
from .column import Column as Column
from .cube import Cube as Cube
from .hierarchy import Hierarchy as Hierarchy
from .level import Level as Level
from .measure import Measure as Measure
from .query import Auth as Auth, ClientCertificate as ClientCertificate
from .query.cube import QueryCube as QueryCube
from .query.hierarchy import QueryHierarchy as QueryHierarchy
from .query.level import QueryLevel as QueryLevel
from .query.measure import QueryMeasure as QueryMeasure
from .query.query_result import QueryResult as QueryResult
from .query.session import QuerySession as QuerySession
from .session import Session as Session
from .table import Table as Table
from .type import DataType as DataType

# pylint: enable=wrong-import-position

check_python_version()

# pylint: disable=invalid-name
sessions: Final = Sessions()
create_session: Final = sessions.create_session
open_query_session: Final = sessions.open_query_session
# pylint: enable=invalid-name


def close() -> None:
    """Close all opened sessions."""
    sessions.close()


(_LICENSE_END_DATE, _IS_COMMUNITY_LICENSE) = retrieve_info_from_jar()

check_license(_LICENSE_END_DATE, _IS_COMMUNITY_LICENSE)

register_active_plugins()

# Need to export elements before typechecking and telemetry setup for walk_api
__all__ = [
    "copy_tutorial",
    "create_session",
    "__version__",
]
__all__ += _functions.__all__
if __license__:
    __all__.append("__license__")


_instrument_typechecking(sys.modules[__name__])

telemeter()
