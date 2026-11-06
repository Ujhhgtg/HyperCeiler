#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Portable JDK location for the host-side test scripts."""

import os
from pathlib import Path

SOURCE_ROOT = Path(__file__).resolve().parents[1]


def configured_path(name: str, default: Path) -> Path:
    """Use a nonempty environment override, expanding a user's home directory."""
    value = os.environ.get(name)
    return Path(value).expanduser().resolve() if value else default.resolve()


JAVA_HOME = configured_path("JAVA_HOME", Path.home() / ".cache/hyperceiler-build/jdk-25.0.4.1")


def java_tool(name: str) -> Path:
    """Resolve a JDK executable for the current host platform."""
    suffix = ".exe" if os.name == "nt" else ""
    return JAVA_HOME / "bin" / (name + suffix)
