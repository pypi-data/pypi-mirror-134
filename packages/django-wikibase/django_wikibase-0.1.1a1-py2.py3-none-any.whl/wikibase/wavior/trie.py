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

def new_trie(keywords):
    trie = {}

    for key in keywords:
        current = trie

        for char in key:
            current = current.setdefault(char, {})
        current[0] = True

    return trie


def in_trie(trie, key):
    if not key:
        return 0

    current = trie

    for char in key:
        if char not in current:
            return 0
        current = current[char]

    if 0 in current:
        return 2
    return 1
