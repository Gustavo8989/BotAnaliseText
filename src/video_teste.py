import cv2 as cv 

cap = cv.VideoCapture(0)

if not cap.isOpened:
    print("Problema com sua webcam, por favor verificar se esta tudo certo")

else:
    print("Câmera acessada com sucesso presione `q` para sair")
while True:
    ret,frame = cap.read()
    if not ret:
        break 

    frame_invertido = cv.flip(frame,1)
    cv.imshow("Teste",frame_invertido)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break 

cap.release()
cv.destroyAllWindows()