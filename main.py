from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pdfminer.pdfparser import PDFParser,PDFDocument
import platform
import sys

class PDF_Manage():
    def __init__(self,fname):
        self.file_name=fname
        self.fp=open(self.file_name,"rb")
        self.praser=PDFParser(fp)
        self.doc=PDFDocument()
        self.parser.set_document(self.doc)
        self.doc.set_parser(self.praser)
        self.doc.initialize()
    def __del__(self):
        self.fp.close()

class File_Chooser(QWidget):
    def __init__(self,parent=None):
        super(File_Chooser,self).__init__(parent)
        layout=QVBoxLayout()
        self.file_choose_btn=QPushButton("Choose File")
        self.file_choose_btn.clicked.connect(self.getFile)
        layout.addWidget(self.file_choose_btn)
        self.setLayout(layout)
        self.resize(400,300)
        self.setWindowTitle("Choose File")
    def getFile(self):
        DEFAULT_DIR=""
        SYSTEM=platform.system()
        if SYSTEM=="windows":
            DEFAULT_DIR="C:\\"
        elif SYSTEM=="Darwin":
            DEFAULT_DIR="/Users"
        elif SYSTEM=="Linux":
            DEFAULT_DIR="/home"
        fname=QFileDialog.getOpenFileName(self,"Open file",DEFAULT_DIR,"PDF Files (*.pdf)")
        print(fname)
        if fname[0]!="":
            pdf1=PDF_Manage(fname[0])
        #f=open(fname[0],'rb')
        #print(len(f.read()))
        #f.close()
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=File_Chooser()
    window.show()
    sys.exit(app.exec_())
