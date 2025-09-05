import PyPDF2
#PDF Merger

files = ["file1.pdf", "file2.pdf"]

pdf_writer = PyPDF2.PdfMerger()

for file in files:
    pdf_writer.append(file)

pdf_writer.write("merged.pdf")
