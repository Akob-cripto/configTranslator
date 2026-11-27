import xml.etree.ElementTree


def create_element(name, value):
    """Создаёт XML-элемент из значения."""
    element = xml.etree.ElementTree.Element(name)

    if isinstance(value, dict):
        for key, item in value.items():
            element.append(create_element(key, item))

    elif isinstance(value, list):
        for item in value:
            element.append(create_element("item", item))

    else:
        element.text = str(value)

    return element


def generate_xml(data):
    """Преобразует конфигурацию в XML."""
    root = create_element("config", data)
    xml.etree.ElementTree.indent(root, space="    ")

    return xml.etree.ElementTree.tostring(root, encoding="unicode")