# homepage.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QPixmap, QIcon
from main import WebContentApp

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ENTER NAME HERE")
        self.setFixedSize(800, 600) 
        self.setWindowIcon(QIcon(r"..\Images\WindowLogo.ico"))

        # Tkinter Window Icon Code Below
        # root.iconbitmap("path_to_your_icon.ico")

        # PyQt5 Window Icon Code Below
        # window.setWindowIcon(QIcon("path_to_your_icon.ico"))
        

        # Create a QLabel to display the image
        self.image_label = QLabel(self)
        self.image_label.setGeometry(200, -40, 400, 600)  # Adjust the position and size as needed
        pixmap = QPixmap(r"..\Images\SampleLogo1.png")  # Provide the path to your image file
        self.image_label.setPixmap(pixmap)

        # Create a button to open the content page
        self.open_button = QPushButton("Open ENTER NAME HERE", self)
        self.open_button.setGeometry(300, 480, 200, 50)
        self.open_button.clicked.connect(self.open_content_page)

        # Apply custom style to the button (same as before)
        self.open_button.setStyleSheet(
            """
            QPushButton {
                background-color: #3498db;
                color: white;
                border: 1px solid #3498db;
                border-radius: 5px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #2E8B57;
                border: 1px solid #2980b9;
            }
            """
        )

    def open_content_page(self):
        # Open the content page frame (imported from your existing code)
        self.content_page = WebContentApp()
        self.content_page.show()

        # Close the home page
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Set a custom application-wide style (optional)
    app.setStyleSheet(
        """
        QMainWindow {
            background-color: #000000;
        }
        """
    )

    homepage = HomePage()
    homepage.show()
    sys.exit(app.exec_())
