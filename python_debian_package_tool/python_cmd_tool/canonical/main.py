""" Main Script for Getting Debian Packages based on Architecture from Command Line """

import os

from modules.cmdline_parser import args_parser
from modules.downloader import Downloader
from modules.logger import def_logger
from modules.parser import Parser


def main() -> None:
    """
    Request, Download, Save, Parse and Output the top-n Debian Packages with their Files
    Returns:
        None
    """
    base_url = "http://ftp.uk.debian.org/debian/dists/stable/main/"

    # Get the architecture from command line
    args = args_parser()

    for arch in args.arch:
        # Download and save the data
        downloader = Downloader(
            architecture=arch, base_url=base_url, verbose=args.verbose
        )
        downloader.initiate()
        downloader.save_gzip()
        downloader.save_txt()

        # Parse data and Output Package Stats
        parser = Parser(
            architecture=arch,
            verbose=args.verbose,
            regex_parse=False,
            get_contents=False,
        )
        parser.package_stats(write_to_file=True)


if __name__ == "__main__":
    logger = def_logger(log_dir=os.getcwd())
    main()
