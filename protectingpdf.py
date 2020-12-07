from PyPDF2 import PdfFileWriter, PdfFileReader

def secure_pdf(file, password):
    parser = PdfFileReader()
    pdf = PdfFileReader(file)

    for page in range(pdf.numPages):
        parser.addPage(pdf.getPage(page))

    parser.encrypt(password)

    with open(f"encrypted_{file}", "wb") as f:
        parser.write(f)
        f.close()

    print(f"encrypted_{file} Created...")

if __name__ == "__main__":
    file = "Antoine de Saint-Exupéry Mały Książę.pdf"
    password = "miguel"

    secure_pdf(file, password)