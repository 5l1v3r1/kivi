# Kivi
It calculates the creation time and size of python objects.

## Installation
```
python3 setup.py install
```

## Example
``` 
from kivi import Kivi 

with Kivi("List Example"):
    a = [i for i in range(10000)]
```
Output:
```
List Example
Time:0.0011322498321533203
Size of a is 87600
```
