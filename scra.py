import PyPDF2
ar = "1901560503_hist_escolar_simplificado.pdf"
lerpdf = PyPDF2.PdfFileReader(ar)
pagina = lerpdf.getPage(1)
cont = pagina.extract_text()
print(cont)