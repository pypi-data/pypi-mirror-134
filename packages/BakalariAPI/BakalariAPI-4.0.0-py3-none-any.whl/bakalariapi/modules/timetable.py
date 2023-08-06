"""Modul obsahující funkce týkající se rozvrhu."""
# Zatím zde nic není... :)
from typing import cast

from bs4 import BeautifulSoup
from bs4.element import Tag  # Kvůli mypy - https://github.com/python/mypy/issues/10826

from ..bakalari import BakalariAPI, Endpoint, _register_parser
from ..looting import GetterOutput, ResultSet
from ..objects import Grade
from ..sessions import RequestsSession


@_register_parser(Endpoint.ROZVRH, BeautifulSoup)
def parser(getter_output: GetterOutput[BeautifulSoup]) -> ResultSet:
    output = ResultSet()
    getter_output.data("div", attrs={"data-detail": True})

    return output
