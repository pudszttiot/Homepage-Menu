import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox, QFileDialog, QVBoxLayout, QWidget, QProgressBar, QAction, QStatusBar
from PyQt5.QtGui import QKeySequence, QCursor, QFont
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QPixmap, QIcon

class WebContentApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ENTER NAME HERE 2")
        self.setFixedSize(800, 600)  # Increased window size
        self.setWindowIcon(QIcon(r"..\Images\WindowLogo.ico"))
        self.initUI()

    def initUI(self):
        # Apply a style sheet for a professional look
        self.setStyleSheet("""
            QMainWindow {
                background-color: #000000;
            }
        """)

# ENTER PYTHON CODE BELOW

# Create a QLabel to display the image
        self.image_label = QLabel(self)
        self.image_label.setGeometry(200, -40, 400, 600)  # Adjust the position and size as needed
        pixmap = QPixmap(r"..\Images\SampleLogo2.png")  # Provide the path to your image file
        self.image_label.setPixmap(pixmap)

# ENTER PYTHON CODE ABOVE

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebContentApp()
    window.show()
    sys.exit(app.exec_())
