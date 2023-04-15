from PyPDF2 import PdfFileWriter, PdfFileReader

template = PdfFileReader(open('super.pdf', 'rb'))
watermark = PdfFileReader(open('wtr.pdf', 'rb'))
output = PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)
