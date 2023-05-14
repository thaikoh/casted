Casted class is used to cast class (dataclass) in Python attributes to their types. 

Example:

```
from typing import Optional
from dataclasses import dataclass

from casted import Casted


@dataclass
class ClassWithOptionalFields(Casted):
    """Class with optional fields"""
    int_field: Optional[int]
    float_field: Optional[float]
    bool_field: Optional[bool]

c_o = ClassWithOptionalFields(int_field=None, float_field=2, bool_field=0)
print(f"ClassWithFields: {c_o}")
```

Result will be:
```
ClassWithOptionalFields: ClassWithOptionalFields(int_field=None, float_field=2.0, bool_field=False)
```