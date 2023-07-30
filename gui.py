import sys
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton \
            ,QWidget,QLabel,QFileDialog
from PyQt5.QtGui import QPixmap,QImage
from model import Detector
import cv2
det = Detector("yolov7x.pt")
class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()

        #load the ui file
        uic.loadUi("image.ui",self)

        #define our widgets
        self.openimagebutton = self.findChild(QPushButton,"pushButton")
        self.usecamerabutton = self.findChild(QPushButton,"pushButton_2")
        self.label = self.findChild(QLabel,"label")
        #click the button
        self.openimagebutton.clicked.connect(self.clicker_image)
        self.usecamerabutton.clicked.connect(self.clicker_camera)


        #show the app
        self.show()
    def clicker_image(self):
        fname = QFileDialog.getOpenFileName(self,"Open File",r"C:\Users\omera\Desktop\gui\gui.py",r"All Files (*);; PNG files(*.png);;JPG files(*.jpg)")
        #open the image
        img = cv2.imread(fname[0])
        img = det.detect_image_and_return(img=img)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        height,width,channel = img.shape
        bytes_per_line = 3*width
        qImg = QImage(img.data,width,height,bytes_per_line,QImage.Format.Format_RGB888)
        pixmap01 = QPixmap.fromImage(qImg)
        pixmap = QPixmap(pixmap01)
        self.label.setPixmap(pixmap)

    def clicker_camera(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret,img = cap.read()
            result = det.detect_image_and_return(img)
            result = cv2.cvtColor(result,cv2.COLOR_BGR2RGB)
            height,width,channel = result.shape
            bytes_per_line = 3 * width
            qImg = QImage(result.data,width,height,bytes_per_line,QImage.Format.Format_RGB888)
            pixmap01 = QPixmap.fromImage(qImg)
            pixmap_image = QPixmap(pixmap01)
            self.label.setPixmap(pixmap_image)
            cv2.waitKey(30)

        
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()