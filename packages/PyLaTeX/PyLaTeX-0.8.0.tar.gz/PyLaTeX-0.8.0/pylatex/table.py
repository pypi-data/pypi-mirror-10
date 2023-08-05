# -*- coding: utf-8 -*-
"""
    pylatex.table
    ~~~~~~~

    This module implements the class that deals with tables.

    :copyright: (c) 2014 by Jelte Fennema.
    :license: MIT, see License for more details.
"""

from .utils import dumps_list
from .base_classes import BaseLaTeXClass, BaseLaTeXContainer, \
    BaseLaTeXNamedContainer
from .package import Package
from .command import Command

from collections import Counter
import re
from warnings import warn


def get_table_width(table_spec):
    """
        :param table_spec:

        :type table_spec: str

        :return:
        :rtype: int
    """

    column_letters = ['l', 'c', 'r', 'p', 'm', 'b']

    # Remove things like {\bfseries}
    cleaner_spec = re.sub(r'{[^}]*}', '', table_spec)
    spec_counter = Counter(cleaner_spec)

    return sum(spec_counter[l] for l in column_letters)


class MultiColumn(BaseLaTeXContainer):

    """A class that represents a multicolumn inside of a table."""

    def __init__(self, size, align='|c|', data=None):
        """
            :param size:
            :param align:
            :param data:

            :type size: int
            :type align: str
            :type data: str or list
        """

        self.size = size
        self.align = align

        super().__init__(data)

    def dumps(self):
        """Represents the multicolumn as a string in LaTeX syntax.

            :return:
            :rtype: str
        """

        multicolumn_type = self.__class__.__name__.lower()
        args = [self.size, self.align, dumps_list(self.data)]
        string = Command(multicolumn_type, args).dumps()
        string += dumps_list(self)

        super().dumps()

        return string


class MultiRow(BaseLaTeXContainer):

    """A class that represents a multirow in a table."""

    def __init__(self, size, width='*', data=None):
        """
            :param size:
            :param width:
            :param data:

            :type size: int
            :type width: str
            :type data: str or list
        """

        self.size = size
        self.width = width

        packages = [Package('multirow')]
        super().__init__(data, packages=packages)

    def dumps(self):
        """Represents the multirow as a string in LaTeX syntax.

            :return:
            :rtype: str
        """

        multirow_type = self.__class__.__name__.lower()
        args = [self.size, self.width, dumps_list(self.data)]
        string = Command(multirow_type, args).dumps()
        string += dumps_list(self)

        super().dumps()

        return string


class TableBase(BaseLaTeXNamedContainer):

    def __init__(self, table_spec, data=None, pos=None, **kwargs):
        """
            :param table_spec:
            :param data:
            :param pos:

            :type table_spec: str
            :type data: list
            :type pos: list
        """

        self.width = get_table_width(table_spec)

        super().__init__(data=data, options=pos,
                         argument=table_spec, **kwargs)

    def add_hline(self, start=None, end=None):
        """Adds a horizontal line to the table.

            :param start:
            :param end:

            :type start: int
            :type end: int
        """

        if start is None and end is None:
            self.append(r'\hline')
        else:
            if start is None:
                start = 1
            elif end is None:
                end = self.width

            self.append(Command('cline', str(start) + '-' + str(end)))

    def add_empty_row(self):
        """Adds an empty row to the table."""

        self.append((self.width - 1) * '&' + r'\\')

    def add_row(self, cells, escape=False):
        """Adds a row of cells to the table.

            :param cells:
            :param escape:

            :type cells: tuple
            :type escape: bool
        """

        # Propegate packages used in cells
        for c in cells:
            if isinstance(c, BaseLaTeXClass):
                for p in c.packages:
                    self.packages.add(p)

        self.append(dumps_list(cells, escape=escape, token='&') + r'\\')

    def add_multicolumn(self, size, align, content, cells=None, escape=False):
        """Adds a multicolumn of width size to the table, with cell content.

            :param size:
            :param align:
            :param content:
            :param cells:
            :param escape:

            :type size: int
            :type align: str
            :type content: str
            :type cells: tuple
            :type escape: bool
        """

        self.append(Command('multicolumn', arguments=(size, align, content)))

        if cells is not None:
            self.add_row(cells)
        else:
            self.append(r'\\')

    def add_multirow(self, size, align, content, hlines=True, cells=None,
                     escape=False):
        """Adds a multirow of height size to the table, with cell content.

            :param size:
            :param align:
            :param content:
            :param hlines:
            :param cells:
            :param escape:

            :type size: int
            :type align: str
            :type content: str
            :type hlines: bool
            :type cells: tuple
            :type escape: bool
        """

        self.append(Command('multirow', arguments=(size, align, content)))
        self.packages.add(Package('multirow'))

        if cells is not None:
            for i, row in enumerate(cells):
                if hlines and i:
                    self.add_hline(2)

                self.append('&')
                self.add_row(row)
        else:
            for i in range(size):
                self.add_empty_row()


class Tabular(TableBase):

    """A class that represents a tabular."""


class Table(Tabular):

    """A legacy name for the class that represents a tabular."""

    container_name = 'tabular'

    def __init__(self, *args, **kwargs):
        warn('Table is going te be deprecated in favor of Tabular',
             PendingDeprecationWarning)
        super().__init__(*args, **kwargs)


class Tabu(TableBase):

    """A class that represents a tabu (more flexible table)"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, packages=[Package('tabu')], **kwargs)


class LongTable(TableBase):

    """A class that represents a longtable (multipage table)"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, packages=[Package('longtable')], **kwargs)


class LongTabu(Table):

    """A class that represents a longtabu (more flexible multipage table)"""

    def __init__(self, *args, **kwargs):
        packages = [Package('tabu'), Package('longtable')]

        super().__init__(*args, packages=packages, **kwargs)
