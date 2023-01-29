import argparse


def args_parser() -> argparse.Namespace:
    cmd_parser = argparse.ArgumentParser(
        description="Calculate Foreign Remittance Transaction Details"
    )
    cmd_parser.add_argument(
        "amount_euros",
        type=float,
        nargs="+",
        help="Euros to Transfer",
    )
    args = cmd_parser.parse_args()
    return args
