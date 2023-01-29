"""Downloader for Downloading & Saving the data as gzip & text"""

import gzip
import logging
import os
import sys
from typing import Tuple
from urllib import parse

import bs4
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

logger = logging.getLogger(__name__)


class Downloader:
    def __init__(
        self,
        architecture: str,
        base_url: str,
        verbose: bool,
        file_name: str = "data",
        arch_file_name: str = "arch_names",
    ):
        self.data_dir = os.path.join(os.getcwd(), "files")
        self.architecture = architecture
        self.verbosity = verbose
        self.gzip_filepath = os.path.join(
            self.data_dir, (file_name + f"_{self.architecture}" + ".gz")
        )
        self.txt_filepath = os.path.join(
            self.data_dir, (file_name + f"_{self.architecture}" + ".txt")
        )
        self.base_url = base_url
        self.base_pattern = "Contents-"
        self.architecture_url = None
        self.arch_names = None
        self.arch_filepath = os.path.join(os.getcwd(), arch_file_name + ".txt")
        self.fetch_attempts = 0
        self.max_fetch_attempts = 1

    def initiate(self) -> None:
        """
        Initiate process for getting the URL for the given architecture
        Returns:
            None
        """
        if self.verbosity:
            logging.info(f"Checking locally for '{self.architecture}'...")
        self._check_arch_names_file()

    def get_content_urls(self) -> None:
        """
        Fetch & parse all download links of gzip files from base URL
        Returns:
            list: all download URLs
        """
        if self.verbosity:
            logging.info("Fetching & saving architecture names for local storage...")
        _, url_soup = Downloader.request_soup(self.base_url)
        content_urls = [
            link.get("href")
            for link in url_soup.find_all("a")
            if self.base_pattern in link.get("href")
        ]
        self.arch_names = Downloader.extract_arch(content_urls)
        self._write_arch_names()

    def extract_arch_url(self) -> str:
        """
        Extract URL for the given architecture from all URLs
        Returns:
            str: download url specific to the architecture
        """
        if self.architecture in self.arch_names:
            if self.verbosity:
                logging.info(
                    f"'{self.architecture}' found in file, fetching its content..."
                )
            self.architecture_url = parse.urljoin(
                self.base_url, (self.base_pattern + self.architecture + ".gz")
            )
            return self.architecture_url
        else:
            while self.fetch_attempts < self.max_fetch_attempts:
                if self.verbosity:
                    logging.info(f"'{self.architecture}' not found in local file!")
                    logging.info(f"Updating data from {self.base_url}...")
                self.fetch_attempts += 1
                self.get_content_urls()
            print(
                f"Nothing found for '{self.architecture}' architecture after update, exiting..."
            )
            sys.exit()

    def save_gzip(self, chunk_size: int = 1024) -> None:
        """
        Save data as a gzip file
        Args:
            chunk_size: the packet size for streaming from extracted URL
        Returns:
            None
        """
        if self.verbosity:
            logger.info("Downloading contents from URL & saving as gzip...")
        r, _ = Downloader.request_soup(self.architecture_url)
        try:
            with open(self.gzip_filepath, "wb") as f:
                with tqdm(
                    unit="B",
                    unit_scale=True,
                    unit_divisor=1024,
                    miniters=1,
                    desc="Progress",
                    total=int(r.headers.get("content-length", 0)),
                    bar_format="{l_bar}{bar:20}{r_bar}{bar:-10b}",
                    colour="green",
                ) as progress_bar:
                    for chunk in r.iter_content(chunk_size=chunk_size):
                        f.write(chunk)
                        progress_bar.update(len(chunk))
        except IOError as e:
            logger.error(f"Error while writing gzip file: {e}")
            sys.exit()

    def save_txt(self) -> None:
        """
        Save data from gzip in a text file
        Returns:
            None
        """
        if self.verbosity:
            logger.info("Saving as txt file for further processing...")
        try:
            with open(self.gzip_filepath, "rb") as fr_gzip, open(
                self.txt_filepath, "wb"
            ) as fr_txt:
                data = gzip.decompress(fr_gzip.read())
                fr_txt.write(data)
        except FileNotFoundError:
            logger.error("gzip file not found for writing a txt file")
            sys.exit()

    def _read_arch_names(self) -> None:
        """
        Helper function: Read architecture names from locally stored txt file
        & then attempt to get the given arch from it, if it exists
        Returns:
            None
        """
        with open(self.arch_filepath, "r") as f:
            self.arch_names = f.read().split()
        self.extract_arch_url()

    def _write_arch_names(self) -> None:
        """
        Helper function: Write extracted architecture names to a txt file
        & then attempt to get the given arch from it, if it exists
        Returns:
            None
        """
        try:
            with open(self.arch_filepath, "w") as f:
                for name in self.arch_names:
                    f.write(name + "\n")
        except IOError as e:
            logger.error(f"Error while writing arch_names txt file: {e}")
            sys.exit()
        else:
            self.extract_arch_url()

    def _check_arch_names_file(self) -> None:
        """
        Helper function: Check if a file with all architecture names exists locally,
        if yes read it else get it
        Returns:
            None
        """
        if os.path.exists(self.arch_filepath):
            if self.verbosity:
                logging.info("Architecture names file found")
            self._read_arch_names()
        else:
            if self.verbosity:
                logging.info("Architecture names file not found, creating it...")
            self.get_content_urls()

    @staticmethod
    def extract_arch(urls: list) -> list:
        """
        Extract arch name from the link for all URLs
        Args:
            urls: list of download links

        Returns:
            list: architecture names

        """
        return [url[url.index("-") + 1 : url.index(".")] for url in urls]

    @staticmethod
    def request_soup(url: str) -> Tuple[requests.Response, bs4.BeautifulSoup]:
        """
        Prepare Soup object for the URL after HTML Parsing
        Args:
            url: the link for making the request
        Returns:
            r: response object from the request
            soup_object: the parsed content from the response
        """
        try:
            r = requests.get(url)
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP Error: {url} {e}")
            sys.exit()
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Cannot Connect: {url} {e}")
            sys.exit()
        except requests.exceptions.RequestException as e:
            logger.error(f"Problem encountered: {url} {e}")
            sys.exit()
        else:
            return r, BeautifulSoup(r.text, "html.parser")

    def __str__(self):
        """
        Give info about architecture url
        Returns:
            str: architecture url
        """
        return f" For {self.architecture}, download URL - {self.architecture_url}"
