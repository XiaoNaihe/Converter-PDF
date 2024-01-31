from pdf2docx import Converter

# Caminho do arquivo PDF de entrada
input_pdf = "input.pdf"

# Caminho para salvar o arquivo DOCX de saída
output_docx = "out.docx"

# Converter PDF para DOCX
cv = Converter(input_pdf)
cv.convert(output_docx, start=0, end=None)
cv.close()

print(f"Arquivo {output_docx} criado com sucesso!")
