# Python Standard Library - Built-in Types

[Built-in Types — Python 3.8.3rc1 documentation](https://docs.python.org/3/library/stdtypes.html#built-in-types)

## Sequence type - list, tuples, range

### Tuples

[Built-in Types — Python 3.8.3rc1 documentation](https://docs.python.org/3/library/stdtypes.html#tuples)

> Note that it is actually the comma which makes a tuple, not the parentheses. The parentheses are optional, except in the empty tuple case, or when they are needed to avoid syntactic ambiguity. For example, f(a, b, c) is a function call with three arguments, while f((a, b, c)) is a function call with a 3-tuple as the sole argument.

### List

[Built-in Types — Python 3.8.3rc1 documentation](https://docs.python.org/3/library/stdtypes.html#lists)

### Range

[Built-in Types — Python 3.8.3rc1 documentation](https://docs.python.org/3/library/stdtypes.html#ranges)

> The advantage of the  [range](https://docs.python.org/3/library/stdtypes.html#range)  type over a regular  [list](https://docs.python.org/3/library/stdtypes.html#list)  or  [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)  is that a  [range](https://docs.python.org/3/library/stdtypes.html#range)  object will always take the same (small) amount of memory, no matter the size of the range it represents (as it only stores the start, stop and step values, calculating individual items and subranges as needed).

## Text sequence type - str

## Set types - set, frozen set

## Mappings types - dict