from pathlib import Path
from typing import Any, Optional

from atoti_core import BaseSession, Plugin

import atoti as tt
from atoti._local_session import LocalSession

from ._source import load_sql, read_sql

JAR_PATH = (Path(__file__).parent / "data" / "atoti-sql.jar").absolute()


class SQLPlugin(Plugin):
    """SQL plugin."""

    def static_init(self) -> None:
        """Init to be called only once."""
        tt.Table.load_sql = load_sql  # type: ignore
        tt.Session.read_sql = read_sql  # type: ignore

    def get_jar_path(self) -> Optional[Path]:
        """Return the path to the JAR."""
        return JAR_PATH

    def init_session(self, session: BaseSession[Any]) -> None:
        """Initialize the session."""
        if not isinstance(session, LocalSession):
            return
        session._java_api.gateway.jvm.io.atoti.loading.sql.SqlPlugin.init()  # type: ignore
