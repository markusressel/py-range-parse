# py-range-parse [![Contributors](https://img.shields.io/github/contributors/markusressel/py-range-parse.svg)](https://github.com/markusressel/py-range-parse/graphs/contributors) [![MIT License](https://img.shields.io/github/license/markusressel/py-range-parse.svg)](/LICENSE) [![Code Climate](https://codeclimate.com/github/markusressel/py-range-parse.svg)](https://codeclimate.com/github/markusressel/py-range-parse) ![Code Size](https://img.shields.io/github/languages/code-size/markusressel/py-range-parse.svg) ![https://badge.fury.io/py/py-range-parse](https://badge.fury.io/py/py-range-parse.svg) [![Build Status](https://travis-ci.org/markusressel/py-range-parse.svg?branch=master)](https://travis-ci.org/markusressel/py-range-parse)

**py-range-parse** is a library to parse commonly used range 
notations to python objects that act like sets.

**py-range-parse is used by**
* [container-app-conf](https://github.com/markusressel/container-app-conf)

and hopefully many others :)

# How to use

```shell
pip install py-range-parse
```

```python
from py_range_parse import parse_range

range = parse_range("[0..5]")
```

or create on manually:

```python
from py_range_parse import Range
range = Range(0,5)
```

## Input formats

When parsing a `Range` from a `str` any whitespace is ignored.

### `int` ranges

If both the _start_ and _end_ value are of type `int`, the resulting `Range` will only consider integers as part of it. If you want to include `float` values as well, at least one of the values has to be a `float`.

* `[-2 .. 5]`
* `[10 .. 1]`

If the _end_ value is bigger than the _start_ value the resulting range will automatically be inverted. Therefore `range.start <= range.end` is **always** `True` in a `Range`.


### `float` ranges

A `float` `Range` includes every possible `float` value between the _start_ and _end_ value.

* `[-2.2 .. 5.123]`
* `[-2.0 .. 5]`

### Infinity

Infinity can also be specified using both `inf` as well as the unicode symbol `∞`. Since it is internally represented using `math.inf` it will behave like a `float`.

* `]-inf .. inf[`
* `]-∞ .. ∞[`

### Exclude borders

The _start_ and _end_ values can be excluded from the `Range` independent of one another using the open bracket notation.

* `]0 .. 5.5]`
* `]0 .. inf[`

## Operations

### Contains

You can easily check if a value is within a given `Range` like this:

```python
> from py_range_parse import parse_range
> range = parse_range("[0 .. 5]")
> print(4 in range)
True
```

### Comparison

You can check if a value is above or below a given `Range` using 
`>` and `<` respectively:

```python
> from py_range_parse import parse_range
> range = parse_range("[0 .. 5]")
> print(6 > range)
True
> print(3 > range)
False
> print(3 < range)
False
> print(-1 < range)
True
```

### Equality

You can compare equality of two `Range` instances using the `==` operator.
For two ranges to be equal they have to have the same 
* `start` value
* `end` value
* start inclusion
* end inclusion
* type (`int` or `float`)

```python
> from py_range_parse import parse_range
> range1 = parse_range("[0 .. 5]")
> range2 = parse_range("[0 .. 5]")
> range3 = parse_range("[0 .. 5.0]")
> print(range1 == range2)
True
> print(range1 == range3)
False
```

# Contributing

GitHub is for social coding: if you want to write code, I encourage contributions through pull requests from forks
of this repository. Create GitHub tickets for bugs and new features and comment on the ones that you are interested in.


# License
```text
py-range-parse
Copyright (c) 2019 Markus Ressel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
