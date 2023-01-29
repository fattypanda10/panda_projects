"""Command Line Argument Parsing using Argparse"""

import argparse
import logging
import sys

logger = logging.getLogger(__name__)


def validate_arch(arch: str) -> str:
    """
    Validate the 'arch' argument from cmdline assuming that no architecture
    is purely numeric & return the lowercase value if validated and also "source" is not allowed
    as it is a pseudo-architecture and does not follow the given format, hence ignored
    Args:
        arch: positional argument from cmd line
    Returns:
        str: the validated & converted to lowercase 'arch' argument
    """
    if arch.isnumeric():
        logger.error("TypeError: Invalid value for architecture")
        sys.exit()
    if arch.lower() == "source":
        logger.error(
            f"'{arch.lower()}' is a pseudo architecture, only binary architecture(s) is valid, exiting..."
        )
        sys.exit()
    return arch.lower()


def args_parser() -> argparse.Namespace:
    """
    Handle Command Line Arguments
    Returns:
        args_object: parsed arguments namespace
    """
    cmd_parser = argparse.ArgumentParser(
        description="Get Debian Packages for a Given Architecture"
    )
    cmd_parser.add_argument(
        "arch",
        type=str,
        nargs="+",
        help="Architecture(s) for which Debian Packages are required, give multiple values separated by space",
    )
    cmd_parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Show Progress Status",
    )
    args = cmd_parser.parse_args()
    args.arch = [validate_arch(arch) for arch in args.arch]
    return args
