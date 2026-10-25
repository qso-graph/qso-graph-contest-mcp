"""Conformance with the Model Context Protocol, revision 2026-07-28.

We documented how to *publish* an MCP server in detail and never wrote down what makes
one *valid*, which is how missing ``isError`` and missing annotations reached every
server in the fleet.

**This server is a placeholder**, so what is worth asserting is the *reason* the four
hints hold rather than the values — copied from another server they are right today and
wrong after the build-out.

What is particular here, and is in neither ``dxe-mcp``'s nor ``js8call-mcp``'s otherwise
similar file:

* **The name is a doctrine, and it is published.** ``PLANNED`` says every contest will
  cite the sponsor that published its rules, and that the server is *"named for this
  project rather than any sponsor: a server covering many sponsors' contests cannot take
  one sponsor's name."* That is this project's rule — the owner of a list is its
  authority — applied to the package name itself. ``TestItTakesNoSponsorsName`` holds
  both halves, because the day somebody renames this after a sponsor, or drops the
  attribution promise, nothing else would notice.

* **``openWorldHint`` will have to change, and this file says so in advance.** Contest
  rules are published by many sponsors, on their own pages, on their own schedules, and
  nothing enumerates them. The specification's own closed-domain example is a database
  query, which this will not be. ``CT-C12`` fails on the first socket, which is when
  that call gets made deliberately rather than inherited.

Test IDs: CT-C01 onward.
"""

from __future__ import annotations

import asyncio

from fastmcp import Client

from qso_graph_contest_mcp import server

ANNOTATION_HINTS = ("readOnlyHint", "destructiveHint", "idempotentHint", "openWorldHint")

# Contest sponsors, whose names this server must not take. It serves all of them.
SPONSORS = ("arrl", "cq-", "cqww", "rsgb", "darc", "jarl", "wwrof", "iaru")


def _tools() -> dict[str, object]:
    return {t.name: t for t in asyncio.run(server.mcp.list_tools())}


def _wire(tool: object) -> dict[str, object]:
    annotations = getattr(tool, "annotations", None)
    assert annotations is not None, "tool declares no annotations"
    return annotations.model_dump(by_alias=True, exclude_none=True)


def call(name: str, args: dict | None = None):
    async def go():
        async with Client(server.mcp) as c:
            return (await c.call_tool(name, args or {})).data
    return asyncio.run(go())


def _sources():
    import pathlib

    src = pathlib.Path(server.__file__).parent
    for py in src.rglob("*.py"):
        yield py, py.read_text()


class TestToolAnnotations:
    def test_every_tool_declares_all_four_hints(self) -> None:
        """CT-C01: the defaults are pessimistic, so silence is the wrong answer."""
        for name, tool in _tools().items():
            wire = _wire(tool)
            for hint in ANNOTATION_HINTS:
                assert hint in wire, f"{name} omits {hint}; got {sorted(wire)}"

    def test_the_values(self) -> None:
        """CT-C02: read-only, non-destructive, idempotent, closed-world."""
        for name, tool in _tools().items():
            wire = _wire(tool)
            assert wire["readOnlyHint"] is True, name
            assert wire["destructiveHint"] is False, name
            assert wire["idempotentHint"] is True, name
            assert wire["openWorldHint"] is False, name


class TestItTakesNoSponsorsName:
    """The naming doctrine, held where it can be checked.

    This project's rule is that the owner of a list is its authority: ARRL adjudicates
    DXCC, CQ adjudicates WAZ. A server that serves *many* sponsors' contests therefore
    cannot be named for one of them without implying an endorsement none of them gave.
    ``PLANNED`` states that, and these two tests are what keep it true.
    """

    def test_the_published_name_is_this_projects(self) -> None:
        """CT-C10: the name a client sees names no sponsor."""
        advertised = (server.mcp.name or "").lower()
        offenders = [s for s in SPONSORS if s in advertised]
        assert not offenders, (
            f"the server name {advertised!r} takes a sponsor's name ({offenders}); it "
            "serves many sponsors' contests and can take none of their names"
        )
        info = call("get_version_info")
        assert info["service_name"] == "qso-graph-contest-mcp"

    def test_the_attribution_promise_is_still_published(self) -> None:
        """CT-C11: the reason for the name is stated where a caller can read it.

        If this sentence goes, CT-C10 is enforcing a rule nobody has written down any
        more, and the first contest answered without a citation breaks nothing visible.
        This fails first.
        """
        assert "citing the sponsor that published its rules" in server.PLANNED
        assert "cannot take one sponsor's name" in server.PLANNED


class TestTheHintsReasonHolds:
    def test_nothing_in_the_package_opens_a_socket(self) -> None:
        """CT-C12: `openWorldHint: false` depends on this, and only for now.

        Contest rules are published by many sponsors, on their own pages, on their own
        schedules, and nothing enumerates them. The specification's closed-domain
        example is a database query; this will not be one. When the first fetch lands,
        this fails — which is when `openWorldHint: true` and `certifi` get chosen
        deliberately rather than inherited.
        """
        offenders = [
            f"{py.name}:{i}: {line.strip()}"
            for py, text in _sources()
            for i, line in enumerate(text.splitlines(), 1)
            if any(t in line for t in ("urlopen", "urllib", "http.client", "socket.",
                                       "requests.", "httpx."))
        ]
        assert not offenders, (
            "something here reaches the network: openWorldHint almost certainly becomes "
            "true, and an outbound HTTPS call needs certifi (qso-graph-devel#73):\n"
            + "\n".join(offenders)
        )

    def test_nothing_in_the_package_writes(self) -> None:
        """CT-C13: `readOnlyHint: true` depends on this."""
        offenders = [
            f"{py.name}:{i}: {line.strip()}"
            for py, text in _sources()
            for i, line in enumerate(text.splitlines(), 1)
            if any(t in line for t in ("write_text(", ".write(", "mkdir("))
        ]
        assert not offenders, "something here writes:\n" + "\n".join(offenders)

    def test_there_is_still_only_the_one_tool(self) -> None:
        """CT-C14: a second tool must choose its own hints, not inherit these."""
        assert set(_tools()) == {"get_version_info"}


class TestNothingCanFail:
    def test_no_error_payload_anywhere_in_the_source(self) -> None:
        """CT-C20: issue #4 says "0 occurrences", and it is right.

        Reads the parse tree for a dict literal with an ``"error"`` key rather than
        searching text, which cannot tell a sentence about a payload from a payload.
        """
        import ast

        offenders = [
            f"{py.name}:{node.lineno}"
            for py, text in _sources()
            for node in ast.walk(ast.parse(text))
            if isinstance(node, ast.Dict)
            and any(isinstance(k, ast.Constant) and k.value == "error" for k in node.keys)
        ]
        assert not offenders, (
            "an error payload exists now, so this server needs the isError conversion "
            f"the rest of the fleet had: {offenders}"
        )


class TestItSaysItIsNotReady:
    def test_the_server_instructions_say_in_development(self) -> None:
        """CT-C30: the instructions are what a client reads before anything else."""
        instructions = server.mcp.instructions or ""
        assert "IN DEVELOPMENT" in instructions
        assert server.TRACKING in instructions

    def test_get_version_info_says_so_too(self) -> None:
        """CT-C31: and so does the one answer it can give."""
        info = call("get_version_info")
        assert info["service_version"]
        assert "in development" in info["status"]
        assert info["tracking"] == server.TRACKING
