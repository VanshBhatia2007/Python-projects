import pikepdf

pdf_my = pikepdf.Pdf.open(r"C:\Users\HP\Downloads\ViewGeneratedDocs (4).pdf")

for i in pdf_my.pages:
    i.obj["/Rotate"] = (i.obj.get("/Rotate", 0) + 180) % 360

pdf_my.save("newpdf.pdf")
