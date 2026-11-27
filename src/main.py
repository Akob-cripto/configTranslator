import sys

from lark.exceptions import UnexpectedInput, VisitError
from src.parser import parse
from src.xml_generator import generate_xml


def main():
    """Выполняет трансляцию конфигурационного языка в XML."""
    try:
        text = sys.stdin.read()
        data = parse(text)
        print(generate_xml(data))

    except UnexpectedInput as error:
        print(f"Синтаксическая ошибка: {error}", file=sys.stderr)
        return 1

    except VisitError as error:
        print(f"Ошибка: {error.orig_exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())