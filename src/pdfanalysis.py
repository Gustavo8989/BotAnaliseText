from pypdf import PdfReader,PdfWriter 
from reportlab.pdfgen import canvas 
import cv2 as cv 
import pytesseract 


print("ler pdf\ncriar pdf")
RESPOSTA = str(input(":> ")) 

if RESPOSTA.lower() == "ler pdf":

    ler_pdf = PdfReader("teste_pdf.pdf") #Não ter arquivo pdf 
    pages_pdf = ler_pdf.pages 
    todas_paginas = ""
    for c in range(len(pages_pdf)):
        todas_paginas = pages_pdf[c].extract_text(extraction_mode="layout",layout_mode_space_vertically=False)
    print(todas_paginas)

elif RESPOSTA.lower() == "criar pdf":
    try:
        pdf_novo = canvas.Canvas("teste_pdf.pdf")
        pdf_novo.drawString(100,750, "Teste de Criação de PDF com pyhton utilizando a biblioteca reportlab")
        pdf_novo.save()
        print("Arquivo Criando com Sucesso")
    except Exception as e:
        print(f"Ocorreu um Erro de {type(e).__name__}")
        print(f"Mais detalhes do Erro {e}")


