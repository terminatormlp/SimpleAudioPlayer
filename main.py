import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Music Player")
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec_())
