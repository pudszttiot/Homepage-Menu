import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, QMessageBox, QTextBrowser
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create a "File" menu
        file_menu = self.menuBar().addMenu("File")

        # Create a "Help" menu
        help_menu = self.menuBar().addMenu("Help")

        # Create a "How to Use" action in the "Help" menu
        how_to_use_action = QAction("How to Use", self)
        how_to_use_action.triggered.connect(self.show_how_to_use_dialog)
        help_menu.addAction(how_to_use_action)

        # Create an "Exit" action in the "File" menu
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Create the central widget (text browser)
        self.central_widget = QTextBrowser(self)
        self.central_widget.setFont(QFont("Arial", 12))
        self.central_widget.setStyleSheet("background-color: white; color: black;")
        self.central_widget.setOpenExternalLinks(True)
        self.setCentralWidget(self.central_widget)

        self.setWindowTitle("My PyQt Application")
        self.setGeometry(100, 100, 800, 600)

    def show_how_to_use_dialog(self):
        # HTML content for the "How to Use" instructions
        html_content = """
        <h1>Welcome to My PyQt Application</h1>
        <p>This is a simple template for a PyQt application.</p>
        <p>Here's how to use it:</p>
        <ul>
            <li>Click on the "File" menu to perform file-related actions.</li>
            <li>Click on the "Help" menu and select "How to Use" to see this dialog.</li>
        </ul>
        <p>That's it! You can now customize this application as needed.</p>
        <p style="text-align: center;"><a href="https://www.example.com">Example Website</a></p>
        <style>
                   .highlight {
                     background-color: yellow;
                   }
                 </style>
                 <p class="highlight">This text is highlighted.</p>
        """

        # Create a QMessageBox to display HTML content
        how_to_use_dialog = QMessageBox()
        how_to_use_dialog.setWindowTitle("Help")
        how_to_use_dialog.setText(html_content)
        how_to_use_dialog.setTextFormat(Qt.RichText)
        # how_to_use_dialog.setFont(QFont("Arial", 12))
        how_to_use_dialog.setWindowIcon(QIcon(r"..\Images\WindowLogo1.ico"))
        how_to_use_dialog.exec_()


def main():
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
