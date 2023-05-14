from dataclasses import dataclass, fields
import typing


@dataclass
class Casted:
    """Casts class attributes to it types including Optional fields"""
    def __post_init__(self):
        for field in fields(self):
            value = getattr(self, field.name)
            types = typing.get_args(field.type)
            if value is None and type(None) in types:
                continue
            if types:
                setattr(self, field.name, next(t for t in types if t != type(None))(value))
            elif not isinstance(value, field.type):
                setattr(self, field.name, field.type(value))
