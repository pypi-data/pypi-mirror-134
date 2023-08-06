from pathlib import Path
from typing import Any, Optional

from atoti_core import BaseSession, Plugin

from atoti._local_session import LocalSession

JAR_PATH = (Path(__file__).parent / "data" / "atoti-gcp.jar").absolute()


class GCPPlugin(Plugin):
    """GCP plugin."""

    def static_init(self):
        """Init to be called only once."""

    def get_jar_path(self) -> Optional[Path]:
        """Return the path to the JAR."""
        return JAR_PATH

    def init_session(self, session: BaseSession[Any]):
        """Initialize the session."""
        if not isinstance(session, LocalSession):
            return
        session._java_api.gateway.jvm.io.atoti.loading.gcp.GcpPlugin.init()  # type: ignore
