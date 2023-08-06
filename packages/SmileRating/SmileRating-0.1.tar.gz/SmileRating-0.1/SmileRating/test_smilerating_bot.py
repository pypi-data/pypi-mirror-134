import unittest
from PySide6 import QtWidgets
from PySide6.QtCore import QSize
import pytest

from PySide6.QtWidgets import QApplication, QLabel, QWidget

from smilerating import SmileRating


class AnimatedToggleTestCase(unittest.TestCase):
    def test_bot_sizeHint(self):
        app = QApplication([])
        window = QWidget()
        result = SmileRating("Thanks for your rating.").sizeHint()
        self.assertEqual(result, QSize(350, 74))


@pytest.fixture
def smilerating_color_on(qtbot):
    test_smilerating = SmileRating("Thanks for your rating.")
    qtbot.addWidget(test_smilerating)
    return test_smilerating


def test_setValue(smilerating_color_on):
    smilerating_color_on.setValue(1)
    aux_num = smilerating_color_on.listLabel.index(
        smilerating_color_on.smileVeryBad)
    assert smilerating_color_on.smileVeryBad.styleSheet( ), (u"\n""QLabel\n""{ \n""border-radius:30%;\n""background:" + smilerating_color_on.colorList[aux_num]+";\n""}")

@pytest.fixture
def smilerating_cofirm(qtbot):
    test_smilerating_b = SmileRating("Thanks for your rating.")
    qtbot.addWidget(test_smilerating_b)
    return test_smilerating_b

def test_valueConfirm_called(smilerating_cofirm): 
    smilerating_cofirm.valueConfirm(1)
    aux_num_c = smilerating_cofirm.listLabel.index(smilerating_cofirm.smileVeryBad)
    assert smilerating_cofirm.smileVeryBad.styleSheet(),(u"\n""QLabel\n""{ \n""border-radius:30%;\n""background:" +smilerating_cofirm.colorList[aux_num_c]+";\n""}")
    assert smilerating_cofirm.smileBad.isVisible(), False
    assert smilerating_cofirm.smileRegular.isVisible(), False
    assert smilerating_cofirm.smileGood.isVisible(), False
    assert smilerating_cofirm.smileVeryGood.isVisible(), False


if __name__ == '__main__':
    unittest.main()
