import sys

from PySide6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QWidget

from smilerating import SmileRating


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        smilerating = SmileRating("Thanks for your rating.")
        layout.addWidget(smilerating)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
