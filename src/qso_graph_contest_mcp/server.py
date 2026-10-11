"""qso-graph-contest-mcp: Amateur radio contest calendar and rules MCP server.

**This server is in development.** It registers one tool, `get_version_info`,
and does nothing else yet.

It is published so the name is held while the work is planned in the open
(qso-graph-devel#49) — PyPI does not reserve a name for a pending trusted
publisher, so a name is only held once something is actually published. Given
that, the honest thing to publish is a package that says what it is.
"""

from __future__ import annotations

import sys
from typing import Any

from fastmcp import FastMCP

from . import __version__

PLANNED = (
    "Which contests are running now, what is coming, and the rules, exchange and multipliers for each — with every contest citing the sponsor that published its rules. Named for this project rather than any sponsor: a server covering many sponsors' contests cannot take one sponsor's name."
)
TRACKING = "https://github.com/qso-graph/qso-graph-devel/issues/49"

mcp = FastMCP(
    "qso-graph-contest-mcp",
    version=__version__,
    instructions=(
        "IN DEVELOPMENT — this server has no working tools yet, and calling it will "
        "not answer questions about " + 'Amateur radio contest calendar and rules MCP server'.lower() + ". "
        "Planned: " + PLANNED + " Progress: " + TRACKING
    ),
)


@mcp.tool()
def get_version_info() -> dict[str, Any]:
    """Get this server's version and development status.

    Returns:
        service_name, service_version, status, what is planned, and where the
        work is tracked.
    """
    return {
        "service_name": "qso-graph-contest-mcp",
        "service_version": __version__,
        "status": "in development — no working tools yet",
        "planned": PLANNED,
        "tracking": TRACKING,
    }


def main() -> None:
    """Run the server."""
    args = sys.argv[1:]
    transport, port = "stdio", 8034
    for i, arg in enumerate(args):
        if arg == "--transport" and i + 1 < len(args):
            transport = args[i + 1]
        if arg == "--port" and i + 1 < len(args):
            port = int(args[i + 1])
    # Written out rather than passed through: fastmcp takes a literal, and a
    # str that happens to hold the right word is not the same thing.
    if transport == "streamable-http":
        mcp.run(transport="streamable-http", port=port)
    else:
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
