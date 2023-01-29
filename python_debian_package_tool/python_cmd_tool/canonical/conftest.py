""" Pytest Config - Defining Fixtures and Mock """

import pytest
from requests.exceptions import ConnectionError, HTTPError, RequestException

from canonical.modules.downloader import Downloader
from canonical.modules.parser import Parser


@pytest.fixture(params=["alpha123", "BETA456"])
def arch_valid(request):
    return request.param


@pytest.fixture
def arch_numeric():
    return "12345"


@pytest.fixture(params=[False, True])
def parser_without_contents(request):
    return Parser(
        architecture="alpha123",
        verbose=False,
        regex_parse=request.param,
        get_contents=False,
    )


@pytest.fixture(params=[False, True])
def parser_with_contents(request):
    return Parser(
        architecture="alpha123",
        verbose=False,
        regex_parse=request.param,
        get_contents=True,
    )


@pytest.fixture
def parser_byte_to_str():
    return b"alphaBetaCharlie"


@pytest.fixture
def parser_process_data():
    return [
        "f1 p1",
        "f2 p2",
        "f3 p3",
        "EMPTY_PACKAGE p4",
        "f4 p2",
        "f5 p3",
        "f6 p3",
        "f7 ",
        " p8",
        "f8,f9,f10,f11 p5",
    ]


@pytest.fixture
def downloader():
    return Downloader(
        architecture="alpha123", base_url="https://testurl", verbose=False
    )


@pytest.fixture
def downloader_url_parser():
    return ["alphabetagamma-arch123.gz", "alphabetagamma-arch123-arch456-arch789.gz"]


class MockResponse:
    def __init__(self, response_status: int, response_text="alphabeta123"):
        self.status_code = response_status
        self.text = response_text

    def get_response_status(self):
        if self.status_code == 200:
            return self.status_code
        elif self.status_code // 100 == 4:
            return HTTPError
        elif self.status_code // 100 == 5:
            return ConnectionError
        else:
            return RequestException

    def raise_for_status(self):
        if self.status_code != 200:
            return HTTPError
