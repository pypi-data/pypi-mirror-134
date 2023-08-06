from pathlib import Path
from typing import Any, Optional

from atoti_core import BaseSession, Plugin
from atoti_query import QueryResult

from ._link import link
from ._visualize import visualize
from ._widget_conversion import create_query_result_repr_mimebundle_method_
from ._widget_manager import WidgetManager


class JupyterLabPlugin(Plugin):
    """JupyterLab plugin."""

    _widget_manager: WidgetManager = WidgetManager()

    def static_init(self):
        """Init to be called only once."""

        BaseSession.link = link  # type: ignore
        BaseSession.visualize = visualize  # type: ignore

        QueryResult._repr_mimebundle_ = create_query_result_repr_mimebundle_method_(
            original_method=QueryResult._repr_mimebundle_
        )

    def get_jar_path(self) -> Optional[Path]:
        """Return the path to the JAR."""
        return None

    def init_session(self, session: BaseSession[Any]):
        """Initialize the session."""
        session._widget_manager = self._widget_manager  # type: ignore
