#!/usr/bin/env python3
"""adcs-audit - Review AD Certificate Services templates for known misconfiguration classes

Authorised security testing only. See README.
"""
from __future__ import annotations

import argparse
import sys

TOOL = "adcs-audit"
DESCRIPTION = "Review AD Certificate Services templates for known misconfiguration classes"


def banner() -> None:
    print(f"[ {TOOL} ] {DESCRIPTION}")


def safe_display(value: str) -> str:
    """Render non-printable input characters as visible escape sequences."""
    return "".join(
        char if char.isprintable() else char.encode("unicode_escape").decode("ascii")
        for char in value
    )


def authorised(assume_yes: bool) -> bool:
    """Refuse to run against a target without an explicit authorisation ack.

    This is not legal cover; it is a deliberate speed bump. Offensive tooling
    should never run by accident against the wrong target.
    """
    if assume_yes:
        return True
    ans = input("Do you have written authorisation to test this target? [y/N] ")
    return ans.strip().lower() in ("y", "yes")


def run(args: argparse.Namespace) -> int:
    """Core routine.

    This is a scaffold: it validates input, states scope, and defines the
    workflow. Extend `run()` with the checks your engagement needs.
    """
    banner()
    print(f"[*] target : {safe_display(args.target)}")
    print(f"[*] output : {safe_display(args.output) if args.output else '(stdout)'}")
    print("[*] scaffold ready - implement engagement-specific logic in run().")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog=TOOL, description=DESCRIPTION)
    p.add_argument("target", help="target host, domain, file, or scope identifier")
    p.add_argument("-o", "--output", help="write results to this file")
    p.add_argument("-v", "--verbose", action="store_true", help="verbose output")
    p.add_argument("-y", "--yes", action="store_true", help="skip the authorisation prompt")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if not authorised(args.yes):
        print("[!] authorisation not confirmed; nothing was done.")
        return 1
    try:
        return run(args)
    except KeyboardInterrupt:
        print("\n[!] interrupted.")
        return 130


if __name__ == "__main__":
    sys.exit(main())
