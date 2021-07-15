from PIL import Image,ImageEnhance
import cv2 as cv
import pyscreenshot as ss
from pytesseract import pytesseract
import numpy as np

# part of the screen
im=ss.grab(bbox=(500,100,1400,1000))
#im.show()
im.save('C:\\Users\\ACER\\Pictures\\save.png')
# Defining paths to tesseract.exe
# and the image we would be using
#path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#image_path = r"csv\d.jpg"

# Opening the image & storing it in an image object
img = cv.imread(r"C:\Users\ACER\Pictures\save.png")
img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
adj=cv.convertScaleAbs(img,alpha=0.5,beta=50)
kernel = np.array([[-1, -1, -1],[-1, 9, -1],[-1, -1, -1]])
shar = cv.filter2D(adj, -1, kernel)
#cv.imshow('ss',img)
cv.imshow('adj',adj)
cv.imshow('sharpened',shar)
cv.waitKey(0)
cv.destroyAllWindows()
#cv.imshow("ss",img)
#cv.waitKey(0)

# Providing the tesseract
# executable location to pytesseract library
pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# Passing the image object to
# image_to_string() function
# This function will
# extract the text from the image
text = pytesseract.image_to_string(shar)

# Displaying the extracted text
print(text[:-1])