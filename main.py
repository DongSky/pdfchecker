import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=QWidget()
    window.resize(400,300)
    window.setWindowTitle("PDFChecker")
    window.setWindowIcon(QIcon("icon.png"))
    
    window.show()
    sys.exit(app.exec_())
