import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QScrollArea, QHBoxLayout, QMenu, QMenuBar, QDialog, QLabel, QWidget, QVBoxLayout, QStackedWidget, QAction, QToolBar, QFileDialog, QTextBrowser
from PyQt5.QtGui import QPixmap, QIcon, QMovie
from PyQt5.QtCore import Qt


class HomePage(QWidget):
    def __init__(self, parent=None):
        super(HomePage, self).__init__(parent)
        layout = QVBoxLayout()

        # Set window properties
        self.setWindowTitle("APP NAME HERE")  # Set the window title
        self.setFixedSize(800, 600)  # Set the window size to 800x600 pixels
        self.setGeometry(300, 100, 800, 600)  # Set the window's position and size (x, y, width, height)
        self.setWindowIcon(QIcon(r"..\Images\WindowLogo1.ico"))  # Set the window icon

        # Create a QLabel to display the background image
        self.background_label = QLabel(self)
        pixmap = QPixmap(r"..\Images\Background1.jpg")  # Provide the path to your background image
        desired_width = 1920
        desired_height = 1200
        pixmap = pixmap.scaled(desired_width, desired_height)
        label_x = int((self.width() - pixmap.width()) / 2)
        label_y = int((self.height() - pixmap.height()) / 2) - 90
        self.background_label.setGeometry(label_x, label_y, pixmap.width(), pixmap.height())
        self.background_label.setPixmap(pixmap)
        self.background_label.lower()


        # Create a QLabel widget to display an animated GIF
        image_label = QLabel(self)
        image_label.setGeometry(0, 0, 300, 150)
        # Specify the path to the GIF file
        movie = QMovie(r"..\Images\AnimatedSampleLogo2.gif")
        
        image_label.setMovie(movie)
        # Calculate the center position for the label
        center_x = (self.width() - image_label.width()) // 2
        center_y = (self.height() - image_label.height()) // 3

        # Set the label position to the center
        image_label.move(center_x, center_y)

        # Start the GIF animation
        movie.start()


        # Create a button to open the main application page with custom style
        self.open_button = QPushButton("Go to Second Page", self)
        self.open_button.setGeometry(245, 420, 300, 70)
        self.open_button.clicked.connect(parent.navigateToSecondPage)  # Connect to the main window's method

        self.open_button.setStyleSheet(
            """
            QPushButton {
                background-color: #2b2b2b;
                color: #00db4d;
                border: 2px solid #006806;
                border-radius: 5px;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #00db4d;
                color: #2b2b2b;
                border: 2px solid #0d0d0d;
                border-radius: 5px;
                font-size: 20px;
            }
            """
        )

class SecondPage(QWidget):
    def __init__(self, parent=None):
        super(SecondPage, self).__init__(parent)
        layout = QVBoxLayout()

        # Set window properties
        self.setWindowTitle("APP NAME HERE")
        self.setFixedSize(800, 600)
        self.setGeometry(300, 100, 800, 600)
        self.setWindowIcon(QIcon(r"..\Images\WindowLogo1.ico"))

        # Create a QLabel to display the background image
        self.background_label = QLabel(self)
        pixmap = QPixmap(r"..\Images\Background1.jpg")  # Provide the path to your background image
        desired_width = 1920
        desired_height = 1200
        pixmap = pixmap.scaled(desired_width, desired_height)
        label_x = int((self.width() - pixmap.width()) / 2)
        label_y = int((self.height() - pixmap.height()) / 2) - 90
        self.background_label.setGeometry(label_x, label_y, pixmap.width(), pixmap.height())
        self.background_label.setPixmap(pixmap)
        self.background_label.lower()

        # Create a QLabel to display the image
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, 400, 300)
        pixmap = QPixmap(r"..\Images\SampleLogo1.png")  # Provide the path to your image file
        label_width = 400
        label_height = 350
        self.image_label.setPixmap(pixmap.scaled(label_width, label_height, aspectRatioMode=1))
        label_x = int((800 - label_width) / 2) + 20
        label_y = int((600 - label_height) / 2) - 50
        self.image_label.move(label_x, label_y)

        # Create a button to navigate back to the home page with custom style
        self.back_button = QPushButton("Go Back", self)
        self.back_button.setGeometry(245, 450, 300, 70)
        self.back_button.clicked.connect(parent.showHomePage)  # Connect to the main window's method

        self.back_button.setStyleSheet(
            """
            QPushButton {
                background-color: #2b2b2b;
                color: #00db4d;
                border: 2px solid #006806;
                border-radius: 5px;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #00db4d;
                color: #2b2b2b;
                border: 2px solid #0d0d0d;
                border-radius: 5px;
                font-size: 20px;
            }
            """
        )

class HelpDialog(QDialog):
    def __init__(self):
        super(HelpDialog, self).__init__()
        self.setWindowTitle("How to Use")
        self.setGeometry(100, 100, 400, 300)
        self.setWindowIcon(QIcon(r"..\Images\WindowLogo1.ico"))

        help_text = """

        <p style="text-align: center;"><h2><span style="color: #007BFF;">===================================</span></h2>
        <h1>🛠 APP NAME HERE 🛠</h1>
        <h2>📝 Version: 1.0.0</h2>
        <h2>📅 Release Date: MM DD, YYYY (May 28, 2023)</h2>
        <h2><span style="color: #007BFF;">===================================</span></h2></p>
        <p><strong><span style="color: #007BFF;">APP NAME HERE</span></strong> is a simple template for a PyQt application.</p>
        <p><h3>Here's how to use it:</h3></p>
        <ul>
            <li>Click on the <strong><span style="color: #007BFF;">"File"</span></strong> menu to perform file-related actions.</li>
            <li>Click on the <strong><span style="color: #007BFF;">"Help"</span></strong> menu and select <strong><span style="color: #007BFF;">"How to Use"</span></strong> to see this dialog.</li>
        </ul>
        <p><h3>Here's how to use it:</h3></p>
        <ol>
            <li>Click on the <strong><span style="color: #007BFF;">"File"</span></strong> menu to perform file-related actions.</li>
            <li>Click on the <strong><span style="color: #007BFF;">"Help"</span></strong> menu and select <strong><span style="color: #007BFF;">"How to Use"</span></strong> to see this dialog.</li>
        </ol>
        <p><strong>That's it!</strong>...You can now customize this application as needed.</p>
        <p>Thank you for using <span style="color: #007BFF;">APP NAME HERE</span>!</p>
 
        <!-- Add an image here -->
        <p style="text-align: center;"><img src="..\Images\SampleLogo1.png" alt="Sample-Logo1" width="100" height="100" border="1"></p>

        <p style="text-align: center;"><h3>▲▲▲👽👽 MY CHANNELS 👽👽▲▲▲</h3></p>
        <p style="text-align: center;"><a href="https://github.com/pudszttiot">Github Page</a></p>
        <p style="text-align: center;"><a href="https://youtube.com/channel/UCwtvRlFsh1-CI1h0g32AlwQ">YouTube Page</a></p>

        """

        help_label = QLabel()
        help_label.setAlignment(Qt.AlignLeft)
        help_label.setText(help_text)

        # Create a scroll area for the help text
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        scroll_area.setWidget(help_label)

        layout = QVBoxLayout()
        layout.addWidget(help_label)
        self.setLayout(layout)

class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()

        self.toolbar = QToolBar()
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)

        self.home_action = QAction(QIcon(r"..\Images\home_icon.png"), "Home", self)
        self.home_action.triggered.connect(self.showHomePage)
        self.toolbar.addAction(self.home_action)
        

        # Create a menu bar
        menubar = self.menuBar()

        # Create a "File" menu
        file_menu = menubar.addMenu("File")

        # Create an "Exit" action under the "File" menu
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Create a "Help" menu
        help_menu = menubar.addMenu("Help")

        # Create a "How to Use" action under the "Help" menu
        how_to_use_action = QAction("How to Use", self)
        how_to_use_action.triggered.connect(self.show_help_dialog)
        help_menu.addAction(how_to_use_action)

        # Initialize the stacked widget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Create and add the pages
        self.home_page = HomePage(parent=self)
        self.second_page = SecondPage(parent=self)
        self.help_dialog = HelpDialog()

        self.stacked_widget.addWidget(self.home_page)
        self.stacked_widget.addWidget(self.second_page)

    def showHomePage(self):
        self.stacked_widget.setCurrentIndex(0)

    def navigateToSecondPage(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_help_dialog(self):
        self.help_dialog.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = AppWindow()
    main_window.setWindowTitle("APP NAME HERE")
    main_window.setFixedSize(800, 600)
    main_window.setGeometry(300, 100, 800, 600)
    main_window.setWindowIcon(QIcon(r"..\Images\WindowLogo1.ico"))
    main_window.show()

    sys.exit(app.exec_())
