from typing import Optional
from dataclasses import dataclass

from casted import Casted


@dataclass
class ClassWithFields(Casted):
    """Class with required fields"""
    int_field: int
    float_field: float
    bool_field: bool


@dataclass
class ClassWithOptionalFields(Casted):
    """Class with optional fields"""
    int_field: Optional[int]
    float_field: Optional[float]
    bool_field: Optional[bool]


def main():
    # noinspection PyTypeChecker
    c = ClassWithFields(int_field=1.25, float_field=2, bool_field=1)
    print(f"ClassWithFields: {c}")

    # noinspection PyTypeChecker
    c_o = ClassWithOptionalFields(int_field=None, float_field=2, bool_field=0)
    print(f"ClassWithOptionalFields: {c_o}")


if __name__ == "__main__":
    main()
