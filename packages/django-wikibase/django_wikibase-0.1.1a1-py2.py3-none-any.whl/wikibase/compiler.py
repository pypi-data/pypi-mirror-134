from typing import Any
from django.db.models.sql import compiler
from json.encoder import JSONEncoder

# The izip_longest was renamed to zip_longest in py3
try:
    from itertools import zip_longest
except ImportError:
    from itertools import izip_longest as zip_longest

from logging import debug
from .cmd import Cmd


class SQLCompiler(compiler.SQLCompiler):

    _select_data = {
        'sparql': None
    }

    def resolve_columns(self, row, fields=()):
        # We need to convert values from database to correct django field representation.
        # For instance, if we defined a BooleanField field, django-wikibase do create a
        # smallint field into DB. When retrieving this field value, it's converted to
        # BooleanField again.
        index_start = len(self.query.extra_select)
        values = []
        for value, field in zip_longest(row[index_start:], fields):
            v = self.query.convert_values(
                value, field, connection=self.connection)
            values.append(v)
        return row[:index_start] + tuple(values)

    def as_sql(self, with_limits=True, with_col_aliases=False):
        sql, params = super(SQLCompiler, self).as_sql(
            with_limits=False, with_col_aliases=with_col_aliases)
        debug('SQL compiler, as_sql, with limits {}, with col alizses {}',
              with_limits, with_col_aliases)

        if with_limits:
            limits = []
            if self.query.high_mark is not None:
                limits.append('FIRST %d' %
                              (self.query.high_mark - self.query.low_mark))
            if self.query.low_mark:
                if self.query.high_mark is None:
                    val = self.connection.ops.no_limit_value()
                    if val:
                        limits.append('FIRST %d' % val)
                limits.append('SKIP %d' % self.query.low_mark)
            sql = 'SELECT %s %s' % (' '.join(limits), sql[6:].strip())
        cmd_data = {**self._select_data, **{'sparql': sql}}
        return Cmd('select', cmd_data), params


class SQLInsertCompiler(compiler.SQLInsertCompiler, SQLCompiler):

    _add_items_data = {
        'sparql': None
    }

    def as_sql(self, with_limits=True, with_col_aliases=False):
        sql, params = super(compiler.SQLInsertCompiler, self).as_sql(
            with_limits=False, with_col_aliases=with_col_aliases)
        debug('SQL insert compiler, as_sql, with limits {}, with col alizses {}',
              with_limits, with_col_aliases)
        cmd_data = {**self._add_items_data, **{'sparql': sql}}
        return [(Cmd('add_items', cmd_data), (params))]


class SQLDeleteCompiler(compiler.SQLDeleteCompiler, SQLCompiler):

    _remove_items_data = {
        'sparql': None
    }

    def as_sql(self, with_limits=True, with_col_aliases=False):
        sql, params = super(compiler.SQLDeleteCompiler, self).as_sql(
            with_limits=False, with_col_aliases=with_col_aliases)
        debug('SQL delete compiler, as_sql, with limits {}, with col alizses {}',
              with_limits, with_col_aliases)
        cmd_data = {**self._remove_items_data, **{'sparql': sql}}
        return [(Cmd('remove_items', cmd_data), (params))]


class SQLUpdateCompiler(compiler.SQLUpdateCompiler, SQLCompiler):

    _set_items_data = {
        'sparql': None
    }

    def as_sql(self, with_limits=True, with_col_aliases=False):
        sql, params = super(compiler.SQLUpdateCompiler, self).as_sql(
            with_limits=False, with_col_aliases=with_col_aliases)
        debug('SQL update compiler, as_sql, with limits {}, with col alizses {}',
              with_limits, with_col_aliases)
        cmd_data = {**self._set_items_data, **{'sparql': sql}}
        return [(Cmd('set_items', cmd_data), (params))]


class SQLAggregateCompiler(compiler.SQLAggregateCompiler, SQLCompiler):

    _agg_items_data = {
        'sparql': None
    }

    def as_sql(self, with_limits=True, with_col_aliases=False):
        sql, params = super(compiler.SQLAggregateCompiler, self).as_sql(
            with_limits=False, with_col_aliases=with_col_aliases)
        debug('SQL aggregate compiler, as_sql, with limits {}, with col alizses {}',
              with_limits, with_col_aliases)
        cmd_data = {**self._agg_items_data, **{'sparql': sql}}
        return [(Cmd('agg_items', cmd_data), (params))]
