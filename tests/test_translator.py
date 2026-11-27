import pytest

from lark.exceptions import UnexpectedInput, VisitError

from src.parser import parse
from src.xml_generator import generate_xml


def test_number():
    """Проверяет обработку числа."""
    assert parse("123") == 123


def test_string():
    """Проверяет обработку строки."""
    assert parse('@"Hello"') == "Hello"


def test_array():
    """Проверяет обработку массива."""
    assert parse("list(1, 2, 3)") == [1, 2, 3]


def test_dictionary():
    """Проверяет обработку словаря."""
    assert parse("{port: 8080}") == {"port": 8080}


def test_name():
    """Проверяет допустимые символы имени."""
    assert parse("{server_port1: 8080}") == {
        "server_port1": 8080
    }


def test_single_line_comment():
    """Проверяет однострочный комментарий."""
    text = """
    # Comment
    123
    """
    assert parse(text) == 123


def test_multiline_comment():
    """Проверяет многострочный комментарий."""
    text = """
    =begin
    Multiline
    comment
    =end
    123
    """
    assert parse(text) == 123

