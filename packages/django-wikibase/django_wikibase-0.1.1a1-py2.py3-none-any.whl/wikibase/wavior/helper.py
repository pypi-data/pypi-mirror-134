# MIT License

# Copyright (c) 2021 Toby Mao

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Contributors:
# https://github.com/tobymao
# https://github.com/izeigerman
# https://github.com/acreux
# https://github.com/wseaton
# https://github.com/zeninpalm
# https://github.com/robert8138

import re
from enum import Enum


class AutoName(Enum):
    # pylint: disable=no-self-argument
    def _generate_next_value_(name, _start, _count, _last_values):
        return name


class RegisteringMeta(type):
    classes = {}

    @classmethod
    def __getitem__(cls, key):
        return cls.classes[key]

    @classmethod
    def get(cls, key, default):
        return cls.classes.get(key, default)

    def __new__(cls, clsname, bases, attrs):
        clazz = super().__new__(cls, clsname, bases, attrs)
        cls.classes[clsname.lower()] = clazz
        return clazz


def list_get(arr, index):
    try:
        return arr[index]
    except IndexError:
        return None


def ensure_list(value):
    if value is None:
        return []
    return value if isinstance(value, (list, set)) else [value]


def csv(*args, sep=", "):
    return sep.join(arg for arg in args if arg)


CAMEL_CASE_PATTERN = re.compile("(?<!^)(?=[A-Z])")


def camel_to_snake_case(name):
    return CAMEL_CASE_PATTERN.sub("_", name).upper()
