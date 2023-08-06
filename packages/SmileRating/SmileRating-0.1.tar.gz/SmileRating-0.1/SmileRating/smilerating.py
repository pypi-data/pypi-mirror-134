from PySide6 import QtGui, QtWidgets
from PySide6 import QtCore
from PySide6.QtCore import (QPoint, QPropertyAnimation, QRect,
                            QSequentialAnimationGroup, QSize, Qt, Signal)

import resources_rc


# SmileRating class that inherits from QtWidgets.QWidget
class SmileRating(QtWidgets.QWidget):
    myMsnChanged = Signal(str)
    # The constructor must receive "myMsn", that is, the message after rating

    def __init__(self, myMsn):
        super().__init__()

        self.setSizePolicy(
            QtWidgets.QSizePolicy.Maximum,
            QtWidgets.QSizePolicy.Maximum,
        )

        self.myMsn_ = myMsn
        self.value = 0
        self.end = False

        layout = QtWidgets.QHBoxLayout()

        self.smileVeryBad = QtWidgets.QLabel()
        self.smileVeryBad.setObjectName(u"smileVeryBad")
        self.smileVeryBad.setGeometry(QRect(40, 20, 64, 64))
        self.smileVeryBad.setPixmap(QtGui.QPixmap(u":/ico/e.png"))

        self.smileVeryGood = QtWidgets.QLabel()
        self.smileVeryGood.setObjectName(u"smileVeryGood")
        self.smileVeryGood.setGeometry(QRect(320, 20, 64, 64))
        self.smileVeryGood.setPixmap(QtGui.QPixmap(u":/ico/a.png"))

        self.smileGood = QtWidgets.QLabel()
        self.smileGood.setObjectName(u"smileGood")
        self.smileGood.setGeometry(QRect(250, 20, 64, 64))
        self.smileGood.setPixmap(QtGui.QPixmap(u":/ico/b.png"))

        self.smileRegular = QtWidgets.QLabel()
        self.smileRegular.setObjectName(u"smileRegular")
        self.smileRegular.setGeometry(QRect(180, 20, 64, 64))
        self.smileRegular.setPixmap(QtGui.QPixmap(u":/ico/c.png"))

        self.smileBad = QtWidgets.QLabel()
        self.smileBad.setObjectName(u"smileBad")
        self.smileBad.setGeometry(QRect(110, 20, 64, 64))
        self.smileBad.setPixmap(QtGui.QPixmap(u":/ico/d.png"))

        self.smileVeryBad.setFixedHeight(64)
        self.smileVeryBad.setFixedWidth(64)
        self.smileVeryGood.setFixedWidth(64)
        self.smileVeryGood.setFixedHeight(64)
        self.smileGood.setFixedWidth(64)
        self.smileGood.setFixedHeight(64)
        self.smileRegular.setFixedWidth(64)
        self.smileRegular.setFixedHeight(64)
        self.smileBad.setFixedWidth(64)
        self.smileBad.setFixedHeight(64)

        self.msn = QtWidgets.QLabel("")
        self.msn.setObjectName(u"msn")
        font = QtGui.QFont()
        font.setFamilies([u"ArtBrush"])
        font.setBold(True)
        self.msn.setFont(font)
        self.msn.setAlignment(Qt.AlignCenter)
        self.msn.setWordWrap(True)

        layout.addWidget(self.smileVeryBad)
        layout.addWidget(self.smileBad)
        layout.addWidget(self.smileRegular)
        layout.addWidget(self.smileGood)
        layout.addWidget(self.smileVeryGood)
        layout.addWidget(self.msn)

        self.listLabel = [self.smileVeryGood,  self.smileGood,
                          self.smileRegular, self.smileBad, self.smileVeryBad]
        self.colorList = ["green", "lime", "yellow", "orange", "red"]
        self.setLayout(layout)

        self.smileVeryBad.enterEvent = lambda event: self.setValue(1)
        self.smileBad.enterEvent = lambda event: self.setValue(2)
        self.smileRegular.enterEvent = lambda event: self.setValue(3)
        self.smileGood.enterEvent = lambda event: self.setValue(4)
        self.smileVeryGood.enterEvent = lambda event: self.setValue(5)
        self.smileVeryBad.leaveEvent = lambda event: self.setValue(0)

        self.smileVeryBad.mousePressEvent = lambda event: self.valueConfirm(1)
        self.smileBad.mousePressEvent = lambda event: self.valueConfirm(2)
        self.smileRegular.mousePressEvent = lambda event: self.valueConfirm(3)
        self.smileGood.mousePressEvent = lambda event: self.valueConfirm(4)
        self.smileVeryGood.mousePressEvent = lambda event: self.valueConfirm(5)
   
        

    # The setValue function establishes with the value parameter the smiles to be displayed.

    def setValue(self, value: int):
        if(self.end == False):
            if(value == 0):
                self.smileVeryBad.setStyleSheet(
                    u"\n""QLabel\n""{ \n""border-radius:30%;\n""background: transparent;\n""}")
            if(value == 1):
                self.transparentAllAbove(self.smileVeryBad)
            if(value == 2):
                self.transparentAllAbove(self.smileBad)
            if(value == 3):
                self.transparentAllAbove(self.smileRegular)
            if(value == 4):
                self.transparentAllAbove(self.smileGood)
            if(value == 5):
                self.transparentAllAbove(self.smileVeryGood)
    def sizeHint(self):
        return QtCore.QSize(350, 74)
    # The hideAllExcept function hides the smile except the one passed by parameter
    # sets the color and makes your content scalable.
    def hideAllExcept(self, aLabel: QtWidgets.QLabel):
        for element in self.listLabel:
            if(element != aLabel):
                element.setHidden(True)
            else:
                element.setStyleSheet(
                    u"\n""QLabel\n""{ \n""border-radius:30%;\n""background:" + self.colorList[self.listLabel.index(element)]+";\n""}")
                self.child = element
                self.child.setScaledContents(True)

    # The transparentAllAbove function makes the background of the smile translucent
    # except for the minor ones to the past by parameter to these it establishes the background color.

    def transparentAllAbove(self, aLabel: QtWidgets.QLabel):
        for element in self.listLabel:
            if(self.listLabel.index(element) < self.listLabel.index(aLabel)):
                element.setStyleSheet(
                    u"\n""QLabel\n""{ \n""border-radius:30%;\n""background: transparent ;\n""}")
            else:
                element.setStyleSheet(
                    u"\n""QLabel\n""{ \n""border-radius:30%;\n""background:" + self.colorList[self.listLabel.index(element)]+";\n""}")
    # The setEnd function establishes that it is the end of the animation and with a label as a parameter
    # that sets fixed the value of its height and width and inserts the message to the text

    def setEnd(self, aLabel: QtWidgets.QLabel):
        if(self.end == False):
            aLabel.setFixedHeight(80)
            aLabel.setFixedWidth(80)
            self.msn.setText(self.myMsn_)
            self.end = True
    # The valueConfirm function sets the smile to show to animate and hides the rest of the smile

    def valueConfirm(self, value: int):
        if(self.end == False):
            if(value == 1):
                self.hideAllExcept(self.smileVeryBad)
            if(value == 2):
                self.hideAllExcept(self.smileBad)
            if(value == 3):
                self.hideAllExcept(self.smileRegular)
            if(value == 4):
                self.hideAllExcept(self.smileGood)
            if(value == 5):
                self.hideAllExcept(self.smileVeryGood)
            self.animationStart()
    # The animationStart function starts the SmileRating animations

    def animationStart(self):
        self.child.resize(0, 0)

        self.animSmilePosition = QPropertyAnimation(self.child, b"pos")
        self.animMsnPosition = QPropertyAnimation(self.msn, b"pos")
        self.animSmileSize = QPropertyAnimation(self.child, b"size")

        self.animSmilePosition.setEndValue(QPoint(150, 1))
        self.animMsnPosition.setEndValue(QPoint(170, 10))
        self.animSmileSize.setEndValue(QSize(80, 80))

        self.animSmileSize.setDuration(100)
        self.animSmilePosition.setDuration(500)
        self.animMsnPosition.setDuration(200)

        self.anim_group = QSequentialAnimationGroup()

        self.anim_group.addAnimation(self.animSmileSize)
        self.anim_group.addAnimation(self.animMsnPosition)
        self.anim_group.addAnimation(self.animSmilePosition)

        self.anim_group.start()
        self.anim_group.finished.connect(self.setEnd(self.child))

    @property
    def myMsn(self):
        return self.myMsn_

    @myMsn.setter
    def myMsn(self, value):
        if value != self.myMsn_:
            if value != "":
                self.myMsn_ = value
                self.myMsnChanged.emit(value)
                print("Modifying the value")
                self.myMsn_ = value
            else:
                print("Error is empty")
