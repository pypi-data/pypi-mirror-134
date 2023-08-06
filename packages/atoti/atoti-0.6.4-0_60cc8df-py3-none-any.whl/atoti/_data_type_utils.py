from typing import Any, Iterable, Mapping

from atoti_core import JavaType, is_numeric_type, parse_java_type, to_array_type

from .type import NULLABLE_DOUBLE_ARRAY, DataType

# Currently, supported types for Python constants.
PYTHON_TYPE_TO_JAVA_TYPE: Mapping[str, JavaType] = {
    "str": "string",
    # Use the widest type to avoid compilation problems
    "int": "long",
    "float": "double",
}


def get_java_type(type_string: str) -> DataType:
    if type_string == "IVector":
        return NULLABLE_DOUBLE_ARRAY

    return DataType(java_type=parse_java_type(type_string), nullable=True)


def convert_python_type_to_java(value: Any) -> DataType:
    python_type = type(value).__name__
    java_type = PYTHON_TYPE_TO_JAVA_TYPE[python_type]
    if java_type is None:
        raise TypeError("Unsupported type: " + python_type)
    if python_type == "list":
        first_element_java_type = PYTHON_TYPE_TO_JAVA_TYPE[type(value[0]).__name__]
        if not is_numeric_type(first_element_java_type):
            raise TypeError("Only lists of numeric values are supported.")
        return DataType(
            java_type=to_array_type(first_element_java_type),
            nullable=True,
        )
    return DataType(java_type=java_type, nullable=True)


TYPE_CONSTRAINTS: Mapping[str, Iterable[str]] = {
    "double": ["double", "float", "long", "int"],
    "float": ["float", "long", "int"],
    "long": ["long", "int"],
    "int": ["int"],
    "double[]": ["double[]"],
    "float[]": ["float[]"],
    "long[]": ["long[]"],
    "int[]": ["int[]"],
    "object": ["object"],
}
