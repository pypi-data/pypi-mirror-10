allyourbase
===========

All Your Base is a python library for converting number strings from any base to number strings of any other base.

This library was created to make the following improvements on existing base conversion libraries out there:

- Can convert both integers and floats
- Uses Decimal package to allow for arbitrary precision / number of digits
- Uses Decimal package to avoid binary rounding errors
- Is not limited to base 36, 62, 64 due to available characters. Can convert to/from any integer base from 2 to whatever you like. (higher bases use delimited decimal format)


Installation
------------

Pip is preferred::

    pip install allyourbase

You can also install manually::

    python setup.py install

Usage
-----

First import BaseConvert and Decimal (used to maintain arbitrary precision)::

    from allyourbase import BaseConvert
    from decimal import Decimal

Decode from base *N* (string) to base 10 (Decimal)::

    numrep = BaseConvert(source_base=34)
    dec = numrep.decode("GKFT9")
    assert dec == Decimal('22185791')

Encode from base 10 (Decimal) to base *N* (string)::

    numrep = BaseConvert(10, 16, max_precision=8)
    hex = numrep.encode(Decimal('4991.58791200'))
    assert hex == "137F.9681669D"

Convert from base *N* (string) to base *M* (string)::

    numrep = BaseConvert(source_base=16, destination_base=42)
    base42 = numrep.convert("137F.9681669D", destination_delimiter=":", destination_max_precision=4)
    assert base42 == "2:34:35.24:29:3:9"

Arguments
---------

**BaseConvert()**

Initialization can provide default bases, delimiters, precision, and rounding information, but is not required to.

:source_base: (int) base the input string should be interpreted as for ``decode`` and ``convert`` (default 10)
:destination_base: (int) base the output string should be written in for ``encode`` and ``convert`` (default 16)
:source_delimiter: (str) delimiter for input string for ``decode`` and ``convert``, necessary for bases larger than 36 (default empty string)
:destination_delimiter: (str) delimiter for output string for ``encode`` and ``convert``, necessary for bases larger than 36 (default empty string)
:max_precision: (int) number of decimal places to use during calculation, when defined here the same value is used for both decoding and encoding purposes (default 10)
:rounding: (bool) applies standard rounding to output. when False, decimal places are simply truncated to desired precision (default True)

|

**decode(** ``value`` **)**

Decodes string value of a number to a Decimal (base 10). Arguments not provided will use defaults from initialization

:value: (required) (str) string representation of number in any integer base
:base: (int) base of input string
:delimiter: (str) delimiter to use for input string, necessary for bases greater than 36
:max_precision: (int) decimal places to use for conversion
:rounding: (bool) apply rounding to output
:returns: (Decimal) value converted to base 10

|

**encode(** ``value`` **)**

Encodes Decimal number to intended base. Arguments not provided will use defaults from initialization

:value: (required) (Decimal, or int or string that will be cast to Decimal) input value in base 10
:base: (int) base of output string
:delimiter: (str) delimiter to use for output string, necessary for bases greater than 36
:max_precision: (int) decimal places to use for conversion
:rounding: (bool) apply rounding to output
:returns: (str) value convert to target base

|

**convert(** ``value`` **)**

Converts value in ``source_base`` to ``destination_base``

:value: (required) (str) input value in source base
:source_base: (int) base of source value
:destination_base: (int) base of target value
:source_delimiter: (str) delimiter to use for input string, necessary for bases greater than 36
:destination_delimiter: (str) delimiter to use for output string, necessary for bases greater than 36
:source_max_precision: (int) precision to use for source->Decimal conversion
:destination_max_precision: (int) precision to use for Decimal->target conversion
:rounding: (bool) apply rounding to output