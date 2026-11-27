import pytest

from lark.exceptions import UnexpectedInput, VisitError

from src.parser import parse
from src.xml_generator import generate_xml


def test_number():
    """Проверяет обработку числа."""
    text = "123"
    expected = 123

    assert parse(text) == expected


def test_string():
    """Проверяет обработку строки."""
    text = '@"Hello"'
    expected = "Hello"

    assert parse(text) == expected


def test_array():
    """Проверяет обработку массива."""
    text = "list(1, 2, 3)"
    expected = [1, 2, 3]

    assert parse(text) == expected


def test_dictionary():
    """Проверяет обработку словаря."""
    text = "{port: 8080}"
    expected = {"port": 8080}

    assert parse(text) == expected


def test_name():
    """Проверяет допустимые символы имени."""
    text = "{server_port1: 8080}"
    expected = {"server_port1": 8080}

    assert parse(text) == expected


def test_single_line_comment():
    """Проверяет однострочный комментарий."""
    text = """
    # Comment
    123
    """
    expected = 123

    assert parse(text) == expected


def test_multiline_comment():
    """Проверяет многострочный комментарий."""
    text = """
    =begin
    Multiline
    comment
    =end
    123
    """
    expected = 123

    assert parse(text) == expected