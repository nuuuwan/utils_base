import os
from functools import cached_property

import camelot
import PyPDF2

from utils_base.file.File import File


class PDFFile(File):
    @cached_property
    def n_pages(self):
        file = open(self.path, "rb")
        reader = PyPDF2.PdfReader(file)
        return len(reader.pages)

    def write_tables(self):
        dir_tables_path = self.path + ".tables"
        os.makedirs(dir_tables_path)
        tables = camelot.read_pdf(self.path, pages="all")
        table_files = []
        for i, table in enumerate(tables):
            table_path = os.path.join(dir_tables_path, f"{i}.tsv")
            table.to_csv(table_path, sep="\t")
            table_files.append(File(table_path))
        return table_files
