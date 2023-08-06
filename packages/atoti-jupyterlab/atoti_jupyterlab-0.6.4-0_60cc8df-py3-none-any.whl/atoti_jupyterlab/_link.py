from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from atoti_core import BaseSession, keyword_only_dataclass

from ._mime_types import LINK_MIME_TYPE


@keyword_only_dataclass
@dataclass(frozen=True)
class Link:
    _path: str
    _session: BaseSession

    def _repr_mimebundle_(
        self, include: Any, exclude: Any  # pylint: disable=unused-argument
    ) -> Mapping[str, Any]:
        return {
            "text/plain": """Open the notebook in JupyterLab with the atoti extension enabled to see this link.""",
            LINK_MIME_TYPE: {
                "path": self._path,
                "sessionLocation": self._session._location,
            },
        }


def link(session: BaseSession[Any], *, path: str = "") -> Any:
    """Display a link to this session.

    Clicking on the link will open it in a new browser tab.

    Note:
        This method requires the :mod:`atoti-jupyterlab <atoti_jupyterlab>` plugin.

    The extension will try to access the session through (in that order):

    #. `Jupyter Server Proxy <https://jupyter-server-proxy.readthedocs.io/>`__ if it is enabled.
    #. ``f"{session_protocol}//{jupyter_server_hostname}:{session.port}"`` for :class:`~atoti.session.Session` and ``session.url`` for :class:`~atoti_query.query_session.QuerySession`.

    Args:
        path: The path to append to the session base URL.
            Defaults to the session home page.

    Example:

        Pointing directly to an existing dashboard:

        .. testcode::

            dashboard_id = "92i"
            session.link(path=f"#/dashboard/{dashboard_id}")

    """
    return Link(_path=path.lstrip("/"), _session=session)
