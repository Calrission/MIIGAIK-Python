import docx2pdf
from pdf2docx import Converter

from .directory import is_linux
from aspose.words import Document


def convert_docx_to_pdf(docx: str, pdf: str):
    if not is_linux:
        docx2pdf.convert(input_path=docx, output_path=pdf)
    else:
        Document(docx).save(pdf)


def convert_pdf_to_docx(pdf: str, docx: str):
    converter = Converter(pdf_file=pdf)
    converter.convert(docx_filename=docx)
