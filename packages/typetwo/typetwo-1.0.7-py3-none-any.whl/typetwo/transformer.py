from datetime import date, datetime, time
from typing import Any, Callable

class Transformer():
    """
    A Transformer encapsulates a succession of
    functions which attempt to convert a value
    from one form to another.

    When called, the transformer applies each
    function in series, returning the value  
    from the first function to succesfully produce
    a new (different) value.

    Errors raised by transforms are ignored.
    """    
    def __init__(
        self, 
        *transforms
    ):
        self.transforms = list(transforms) if transforms else []

    def __add__(self, value : Callable[[Any], Any]):
        """Adds a transform function to this transformer.
        
        The transformer must be a simple function,
        taking a single value and returning a single value.
        
        Any errors raised by the transform function are ignored.
        """
        if isinstance(value, function):
            self.transforms.append(value)
        else:
            raise NotImplementedError()

    def enable_dates(self, *formats):
        """Adds date format strings to recognize (see strptime)"""
        self.transforms += [lambda d: datetime.strptime(d, fmt).date() for fmt in formats]
        return self
    
    def enable_times(self, *formats):
        """Adds time format strings to recognize (see strptime)"""
        self.transforms += [lambda d: datetime.strptime(d, fmt).time() for fmt in formats]
        return self
    
    def enable_datetimes(self, *formats):
        """Adds datetime format strings to recognize (see strptime)"""
        self.transforms += [lambda d: datetime.strptime(d, fmt) for fmt in formats]
        return self
    
    def enable_iso_dates(self):
        """Adds support for parsing ISO date, time and datetime strings"""
        self.transforms += [time.fromisoformat, date.fromisoformat, datetime.fromisoformat]
        return self

    def __call__(self, value):
        """Applies this transform to the given ``value``. 
        Returns the original value if no transform succeeds"""

        if value is not None:        
            if isinstance(value, list):
                return [self.__call__(d) for d in value]

            if isinstance(value, dict):
                return {key: self.__call__(v) for (key, v) in value.items()}
            
            for fn_xform in self.transforms:
                try:
                    new_value = fn_xform(value)
                    if new_value is not None and new_value != value:
                        return new_value
                except Exception as e:
                    pass
        return value