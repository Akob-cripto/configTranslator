from pathlib import Path

from lark import Lark, Transformer


class ConfigTransformer(Transformer):
    """Преобразует дерево разбора в объекты Python."""

    def __init__(self):
        super().__init__()
        self.constants = {}

    def number(self, items):
        """Преобразует число."""
        return int(items[0])

    def string(self, items):
        """Преобразует строку."""
        return str(items[0])[2:-1]

    def array(self, items):
        """Создаёт список."""
        return items

    def pair(self, items):
        """Создаёт пару ключ — значение."""
        return str(items[0]), items[1]

    def dictionary(self, items):
        """Создаёт словарь."""
        return dict(items)

    def constant(self, items):
        """Сохраняет значение константы."""
        name, value = items
        self.constants[str(name)] = value

    def reference(self, items):
        """Возвращает значение константы."""
        name = str(items[0])

        if name not in self.constants:
            raise ValueError(f"Неизвестная константа: {name}")

        return self.constants[name]

    def start(self, items):
        """Возвращает итоговое значение конфигурации."""
        return items[-1]


def parse(text: str):
    """Разбирает и преобразует входной текст."""
    grammar_path = Path(__file__).with_name("grammar.lark")
    grammar = grammar_path.read_text(encoding="utf-8")

    parser = Lark(grammar, parser="lalr")
    tree = parser.parse(text)

    return ConfigTransformer().transform(tree)