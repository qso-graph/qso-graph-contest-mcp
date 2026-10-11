<!-- mcp-name: io.github.qso-graph/qso-graph-contest-mcp -->
# qso-graph-contest-mcp

[![PyPI](https://img.shields.io/pypi/v/qso-graph-contest-mcp?label=PyPI&color=blue)](https://pypi.org/project/qso-graph-contest-mcp/)

> ### In development
>
> This package is published so the name is held while the work is planned in the open.
> It registers one tool, `get_version_info`, and **does nothing else yet**. If you install
> it expecting a working server, that is what you will find — which is why it says so
> here, in the server's own instructions, and in the one tool it has.
>
> PyPI does not reserve a name for a pending trusted publisher, so a name is only held
> once something is actually published. Given that, a package that says what it is beats
> an empty one that does not.

Which contests are running now, what is coming, and the rules, exchange and multipliers for each — with every contest citing the sponsor that published its rules. Named for this project rather than any sponsor: a server covering many sponsors' contests cannot take one sponsor's name.

Planned work, including the data sources it would use and whether each is actually
available, is tracked in
[qso-graph-devel#49](https://github.com/qso-graph/qso-graph-devel/issues/49).

Part of the [qso-graph](https://qso-graph.io/) project.

## Install

```bash
uvx qso-graph-contest-mcp            # run it; nothing to install
```

## Tools

| Tool | Description |
|------|-------------|
| `get_version_info` | Service version, development status, and where the work is tracked |

## Quick Start

No credentials needed — install and configure your MCP client.

### Configure your MCP client

qso-graph-contest-mcp works with any MCP-compatible client. Add the server config and restart.

#### Claude Desktop

Add to `claude_desktop_config.json` (`~/Library/Application Support/Claude/` on macOS,
`%APPDATA%\Claude\` on Windows):

```json
{
  "mcpServers": {
    "qso-graph-contest": {
      "command": "uvx",
      "args": ["qso-graph-contest-mcp"]
    }
  }
}
```

#### Claude Code

Add to `.claude/settings.json`:

```json
{
  "mcpServers": {
    "qso-graph-contest": {
      "command": "uvx",
      "args": ["qso-graph-contest-mcp"]
    }
  }
}
```

#### ChatGPT Desktop

Configure via Settings > Apps & Connectors, or in your agent definition:

```json
{
  "mcpServers": {
    "qso-graph-contest": {
      "command": "uvx",
      "args": ["qso-graph-contest-mcp"]
    }
  }
}
```

### Questions it will answer

Not yet — these are what the finished server is for:

> "What contests are running this weekend?"

> "What is the exchange for this contest, and who sponsors it?"

> "Which upcoming contests are CW only on 40m?"

## Licence

GPL-3.0-or-later. See [LICENSE](LICENSE).
