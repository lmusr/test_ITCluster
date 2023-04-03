from tkinter.filedialog import askopenfile, asksaveasfile
import cv2
import numpy as np

def process_image_opencv ():
    "Load from file - process image - show image - save image in OpenCV"
    
    # Читання RGB-зображення
    f = askopenfile (mode = 'rb', defaultextension = ". jpg",
              filetypes = (( "Image files", "* .jpg"), ( "All files", "*. *")))
    img = cv2.imread (f.name)
    # Показ RGB-зображення
    cv2.imshow ( "BGR", img)
    # Перетворення RGB-зображення в відтінки сірого
    gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
    cv2.imshow ( "Gray", gray)
    # Збереження в файл
    cv2.imwrite ( "gray_image.jpg", gray)
    # Виділення меж зображення (Алгоритм Канни)
    edges = cv2.Canny (img, 10, 50)
    cv2.imshow ( "Edges", edges)
    # Бінаризація зображення 
    tr, im_bw = cv2.threshold (gray, 55, 255, cv2.THRESH_BINARY)
    cv2.imshow ( 'Binary', im_bw)
    # Детектування кутів
    corners = cv2.goodFeaturesToTrack (gray, 10, 0.009, 20)
    corners = np.float32 (corners) # Перетворити в масив numpy
    for item in corners:  # Намалювати кружечки
        x, y = item [0]
        cv2.circle (img, (x, y), 5, 255, -1)
    cv2.imshow ( "Top 'k' features", img)
    cv2.waitKey ()

#some changes
#some other changes 1
