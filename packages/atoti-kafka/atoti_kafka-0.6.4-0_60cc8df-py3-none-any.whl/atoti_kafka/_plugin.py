from pathlib import Path
from typing import Any, Optional

from atoti_core import BaseSession, Plugin

from atoti._local_session import LocalSession
from atoti.table import Table

from ._source import load_kafka

JAR_PATH = (Path(__file__).parent / "data" / "atoti-kafka.jar").absolute()


class KafkaPlugin(Plugin):
    """Kafka plugin."""

    def static_init(self) -> None:
        """Init to be called only once."""
        Table.load_kafka = load_kafka  # type: ignore

    def get_jar_path(self) -> Optional[Path]:
        """Return the path to the JAR."""
        return JAR_PATH

    def init_session(self, session: BaseSession[Any]) -> None:
        """Initialize the session."""
        if not isinstance(session, LocalSession):
            return
        session._java_api.gateway.jvm.io.atoti.loading.kafka.KafkaPlugin.init()
