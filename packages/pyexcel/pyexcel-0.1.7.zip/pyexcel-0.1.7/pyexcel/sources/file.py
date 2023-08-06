"""
    pyexcel.sources.file
    ~~~~~~~~~~~~~~~~~~~

    Representation of file sources

    :copyright: (c) 2015 by Onni Software Ltd.
    :license: New BSD License
"""
import os
from .base import Source, one_sheet_tuple
from ..constants import KEYWORD_FILE_NAME
from pyexcel_io import load_data


class SheetSource(Source):
    """Pick up 'file_name' field and do single sheet based read and write
    """
    fields = [KEYWORD_FILE_NAME]

    def __init__(self, file_name=None, **keywords):
        self.file_name = file_name
        self.keywords = keywords

    def get_data(self):
        """
        Return a dictionary with only one key and one value
        """
        sheets = load_data(self.file_name, **self.keywords)
        return one_sheet_tuple(sheets.items())

    def write_data(self, sheet):
        from ..writers import Writer
        w = Writer(self.file_name, sheet_name=sheet.name, **self.keywords)
        w.write_reader(sheet)
        w.close()


class BookSource(SheetSource):
    """Pick up 'file_name' field and do multiple sheet based read and write
    """
    def get_data(self):
        sheets = load_data(self.file_name, **self.keywords)
        path, filename_alone = os.path.split(self.file_name)
        return sheets, filename_alone, path

    def write_data(self, book):
        from ..writers import BookWriter
        writer = BookWriter(self.file_name, **self.keywords)
        writer.write_book_reader(book)
        writer.close()
