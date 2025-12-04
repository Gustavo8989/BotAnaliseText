from pypdf import PdfReader,PdfWriter
import cv2 as cv    



#Converter para preto e branco 

imagem = cv.imread("imagens.png")
# colocando a imagem em escala de cinza 
imagem_cinza  = cv.cvtColor(imagem,cv.COLOR_BGR2GRAY)




# Aumetar o contraste 


# Detectar as bordas 
