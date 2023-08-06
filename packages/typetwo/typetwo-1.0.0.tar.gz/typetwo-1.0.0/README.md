# Type 2

Provides a simple set of utility functions for dealing with change management for datasets based on lists of dictionaries.

## Example Usage: TypeTwo

 ```python

rows = [
    {"id" : 1, "name" : "Henry", "age" : 34}
    {"id" : 2, "name" : "Fred", "age"  : 42}
]

history = TypeType(rows, RowKey("id"), from_field = "start", to_field = "end")

history += {"id" : 1, "name" : "Henry", "age" : 37}
    
iter(history)
>>> {"id" : 1, "name" : "Henry", "age" : 34, "start": datetime(1900,1,1),  "end": datetime(2022,6,12)}
>>> {"id" : 1, "name" : "Henry", "age" : 37, "start": datetime(2022,6,12), "end": datetime(2999,12,31)}
>>> {"id" : 2, "name" : "Fred",  "age" : 42, "start": datetime(1900,1,1),  "end": datetime(2999,12,31)}


history += {"id" : 1, "name" : "Henry", "age" : 37}


changes = [
    {"id" : 1, "name" : "Henry", "age" : 99}
    {"id" : 2, "name" : "Fred", "age"  : 99}
]


```