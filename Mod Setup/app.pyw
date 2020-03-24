import setup
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class app_modsetup():
    def __init__(self):
        self.editFirst = False
        app = QApplication([]) #init app
        app.setStyle("fusion")
        app.setWindowIcon(QIcon("resource/gui/logo.png"))

        self.create_layout_base()
        self.create_window()

        app.exec_()
    def create_layout_base(self):
        self.main_layout = QGridLayout()

        self.browsePath = QLineEdit()
        self.browsePath.setPlaceholderText("Path to create mod")
        self.browsePath.textChanged.connect(self.function_browse_edit)
        self.main_layout.addWidget(self.browsePath,0,0)

        self.browseButton = QPushButton("Browse")
        self.browseButton.clicked.connect(self.function_getdir)
        self.main_layout.addWidget(self.browseButton,0,1)
    def create_window(self):
        #define the window
        self.main_window = QWidget()
        self.main_window.setLayout(self.main_layout)
        #sets the window size and global style ect
        self.main_window.setMinimumSize(400,60)
        self.main_window.setMaximumSize(400,60)
        self.main_window.setGeometry(500, 500, 400, 60)
        self.main_window.setWindowTitle("Quiver Mod Setup")
        self.main_window.setStyleSheet(open("resource/gui/style.css").read())
        #show the window
        self.main_window.show()
    
    def function_getdir(self):
        browseSelection = str(QFileDialog.getExistingDirectory())
        self.browsePath.setText(browseSelection)
        print(browseSelection)
    
    def function_browse_edit(self):
        if (self.editFirst == False):
            self.editFirst = True
            self.gui_browse_edit()
    def gui_browse_edit(self):
        #add create mod button
        self.createmodButton = QPushButton("Create Mod")
        self.createmodButton.clicked.connect(self.function_createmod)
        self.main_layout.addWidget(self.createmodButton,1,0,1,2)
        #set size of window for new button
        self.main_window.setMinimumSize(400,100)
        self.main_window.setMaximumSize(400,100)
        self.main_window.setGeometry(500, 500, 400, 100)

    def function_createmod(self):
        self.gui_createmod()
        setupmod = setup.mod("E:/Quiver/Quiver-Mod-Setup/resource/createmod.zip",self.browsePath.text())
        setupmod.mod_extract()
        del setupmod

        createmodFinishedMsg = QMessageBox()
        createmodFinishedMsg.setIcon(QMessageBox.Information)
        createmodFinishedMsg.setText("This is a message box")
        createmodFinishedMsg.setInformativeText("This is additional information")
        createmodFinishedMsg.setWindowTitle("MessageBox demo")
        createmodFinishedMsg.setDetailedText("The details are as follows:")

        self.browsePath.setDisabled(True)
        self.browseButton.setDisabled(True)
        self.createmodButton.setDisabled(True)
        #self.mod_extract(self.browsePath.text(),"E:/Quiver/Quiver-Mod-Setup/resource/createmod.zip")
    def gui_createmod(self):
        self.browsePath.setDisabled(True)
        self.browseButton.setDisabled(True)
        self.createmodButton.setDisabled(True)

    def mod_extract(self,baseDir,modDir):
        import zipfile
        import os
        if (not os.path.exists(modDir)):
            os.makedirs(modDir)
        unzip = zipfile.ZipFile("E:/Quiver/Quiver-Mod-Setup/resource/createmod.zip", "r")
        unzip.printdir()
        unzip.extractall("E:/Quiver/Quiver-Mod-Setup/testmod")
        del unzip

app=app_modsetup()