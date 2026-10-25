# Changelog

All notable changes to `qso-graph-contest-mcp` are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### MCP specification 2026-07-28 (#4)

- **The one tool declares the four annotation hints.** Omitting them advertises it as
  `destructiveHint: true`, `idempotentHint: false`, `openWorldHint: true`.
- **There is no `isError` work, and the issue says so correctly** — "0 occurrences" of error
  payloads in `src/`, because nothing here can refuse yet.
- **The naming doctrine is now held by a test.** `PLANNED` promises every contest will cite the
  sponsor that published its rules, and that this server is *"named for this project rather than
  any sponsor: a server covering many sponsors' contests cannot take one sponsor's name."* That is
  this project's rule — the owner of a list is its authority — applied to the package name itself.
  `CT-C10` checks the advertised name takes no sponsor's name; `CT-C11` checks the promise is still
  published, so dropping the sentence fails before the rule becomes unwritten and the first
  uncited contest answer breaks nothing visible.
- **`openWorldHint` is right today and will have to change.** Contest rules are published by many
  sponsors, on their own pages, on their own schedules, and nothing enumerates them; the
  specification's own closed-domain example is a database query, which this will not be. `CT-C12`
  fails on the first socket — which is when `true` and `certifi` get chosen deliberately rather
  than inherited.
- `tests/test_mcp_conformance.py` (CT-C01 onward). Every check falsified — **10 of 10** — with
  `CT-C11` falsified twice, once for each phrase it asserts.

### Lint (#3)

- **`E501` is adopted.** Two lines, neither a defect: the `PLANNED` string, which reflows as
  adjacent literals so the published value is **byte-identical**, and a concatenation in the
  server instructions, split at the `+`.
- The publisher-name exemption the issue was filed for does not apply — and here the reason is the
  point rather than an accident: this server names **no** sponsor's field, because naming one
  sponsor is exactly what it must not do. Zero exemptions, no `# noqa: E501`.

### Not applicable here

- **No `certifi` work and no issue for it** (qso-graph-devel#73): no outbound call of any kind in
  `src/`. `CT-C12` names `certifi` in its failure message, for the build-out.

## [0.0.1] — 2026-10-11

- Placeholder release so the name is held on PyPI while the work is planned
  (qso-graph-devel#49). A pending trusted publisher does **not** reserve a name —
  PyPI's documentation is explicit that a name is held only once something is actually
  published — so this is a real, installable package rather than an empty repository.
- One tool, `get_version_info`, reporting the development status, what is planned, and
  where the work is tracked. The server's instructions say the same, so a client listing
  it sees the truth before calling anything.
