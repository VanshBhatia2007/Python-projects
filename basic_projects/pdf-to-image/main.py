from pdf2image import convert_from_path

old_pdf = convert_from_path(r"C:\Users\HP\Downloads\8719332_90983521754038119750.pdf", poppler_path=r"C:\Users\HP\OneDrive\Desktop\Python-projects\basic_projects\pdf-to-image\poppler-24.08.0\Library\bin")

for i in range(len(old_pdf)):
    old_pdf[i].save("new"+str(i)+".jpg","JPEG")