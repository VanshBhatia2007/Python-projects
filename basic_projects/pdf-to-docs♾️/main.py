from pdf2docx import Converter

new_doc = "new.docx"

obj = Converter(r"c:\Users\HP\Downloads\AdmitCard-253510000051.pdf")
obj.convert(new_doc)
obj.close()