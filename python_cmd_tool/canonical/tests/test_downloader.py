import pytest
import requests
from requests.exceptions import ConnectionError, HTTPError, RequestException

from canonical.conftest import MockResponse


@pytest.mark.parametrize(
    "status, expected",
    [(200, 200), (404, HTTPError), (502, ConnectionError), (310, RequestException)],
)
def test_downloader_request(monkeypatch, downloader, status, expected):
    def get_mock_response(*args, **kwargs):
        return MockResponse(response_status=status)

    monkeypatch.setattr(requests, "get", get_mock_response)
    response, _ = downloader.request_soup(url=downloader.base_url)

    assert response.get_response_status() == expected


def test_downloader_url_parser(downloader, downloader_url_parser: list):
    parsed_urls = downloader.extract_arch(downloader_url_parser)
    assert all([isinstance(arch, str) for arch in parsed_urls])
    assert parsed_urls[0] == "arch123"
    assert parsed_urls[1] == "arch123-arch456-arch789"
