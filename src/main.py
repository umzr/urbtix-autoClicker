

import webbrowser
from PyQt6.QtCore import  Qt
from PyQt6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
     QPushButton, QVBoxLayout )
import pyautogui, sys
import keyboard

class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)
        self.targetHttp = "https://www.urbtix.hk/"
        self.positionX = None 
        self.positionY = None 

        # top
        styleLabel = QLabel("網頁Link:")

        httpLink = QLineEdit()
        httpLink.setText(self.targetHttp)
        httpLink.setPlaceholderText("https://www.urbtix.hk/")
        httpLink.textChanged.connect(self.textchanged)
        
        clickBnt2Website = QPushButton("Enter")
        clickBnt2Website.clicked.connect(self.topButton2Website)
        # end top


        self.createTopLeftGroupBox()

        topLayout = QHBoxLayout()
        topLayout.addWidget(styleLabel)
        topLayout.addWidget(httpLink)
        topLayout.addWidget(clickBnt2Website)
        topLayout.addStretch(1)


        self.progressBar =  QPushButton('RUN press s to stop',self)
        self.progressBar.clicked.connect(self.runTarget)
        self.runAlertMessage =  QLabel("https://github.com/umzr")
        
        
        BottomLayout = QVBoxLayout()
        BottomLayout.addWidget(self.progressBar )
        BottomLayout.addWidget(self.runAlertMessage )

        BottomLayout.addStretch(1)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 1)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addLayout(BottomLayout, 3, 0, 1, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("urbtix auto clicker")

    def click(self):
        pyautogui.PAUSE = 0.01
        pyautogui.click(x=self.positionX, y=self.positionY) 
        

    def runTarget(self):
        while True:
            
            self.progressBar.setText("留名系統啟動，請勿負評干擾運作！！！")
            self.runAlertMessage.setText("Press s to stop")
            QApplication.processEvents()
            self.click()
            if keyboard.is_pressed('s'):
                self.runAlertMessage.setText("https://github.com/umzr")
                self.progressBar.setText("RUN press s to stop")
                return False
            

        
    def textchanged(self,text):
            self.targetHttp = text
    
    def topButton2Website(self):
        webbrowser.open(self.targetHttp)
        

    def mouse(self):
        while True:
            if keyboard.is_pressed('b'):
                x, y = pyautogui.position()
                positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
                print (positionStr)
                self.positionX = x
                self.positionY = y
                self.targetPosition.setText("X: {}, Y: {}".format(self.positionX, self.positionY))
                return False



    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("INPUT TARGET")
        
        XYBtn = QPushButton('Click')
        XYBtn.clicked.connect(self.mouse)
        self.targetPosition = QLabel("X: {}, Y: {}".format(self.positionX, self.positionY))
        # ............
        LabelYourScreenSize = QLabel("Your Screen Target (press b to target): ")
        ScreenRow = QHBoxLayout()
        ScreenRow.addWidget(LabelYourScreenSize)
        ScreenRow.addWidget(XYBtn)
        ScreenRow.addStretch(1)
        # .............

        checkBox = QCheckBox("Tri-state check box")
        checkBox.setTristate(True)
        checkBox.setCheckState(Qt.CheckState.PartiallyChecked)

        layout = QVBoxLayout()
        layout.addLayout( ScreenRow )
        layout.addWidget(self.targetPosition)
    
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)
    


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec())