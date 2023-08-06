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

from copy import deepcopy

import wikibase.wavior.expressions as exp
from wikibase.wavior import parse_one


class chainable:
    def __init__(self, func):
        self.func = func

    def __set_name__(self, owner, name):
        def wrapper(rewriter, *args, **kwargs):
            expression = self.func(rewriter, *args, **kwargs)
            return Rewriter(expression, rewriter.copy)

        setattr(owner, name, wrapper)


class Rewriter:
    def __init__(self, expression, copy=True):
        self.copy = copy
        self.expression = deepcopy(expression) if copy else expression

    @chainable
    def ctas(self, table, db=None, file_format=None):
        create = self.expression.find(exp.Create)

        if create:
            create.args["db"] = db
            create.args["this"] = table
            if file_format is not None:
                create.args["file_format"] = exp.FileFormat(this=file_format)
        else:
            create = exp.Create(
                this=exp.Table(this=table, db=db),
                kind="table",
                expression=self.expression,
                file_format=exp.FileFormat(this=file_format)
                if file_format is not None
                else None,
            )

        return create

    @chainable
    def add_selects(self, *selects, read=None):
        select = self.expression.find(exp.Select)
        for sql in selects:
            select.args["expressions"].append(parse_one(sql, read=read))
        return self.expression
