import sys
import unittest

from PySide6.QtWidgets import QApplication, QWidget

from smilerating import SmileRating


class Testing(unittest.TestCase):

    def test_component(self):
        app = QApplication.instance()
        if app == None:
            app = QApplication([])
        window = QWidget()  
        result = SmileRating("Thanks for your rating.")
        self.assertEqual(result.myMsn_, "Thanks for your rating.")

    def test_setValue(self):

        result_b = SmileRating("Thanks for your rating.")
        result_b.setValue(1)
        aux_num = result_b.listLabel.index(result_b.smileVeryBad)
        self.assertEqual(result_b.smileVeryBad.styleSheet(), (
            u"\n""QLabel\n""{ \n""border-radius:30%;\n""background:" + result_b.colorList[aux_num]+";\n""}"))

    def test_transparentAllAbove(self):

        result_i = SmileRating("Thanks for your rating.")
        result_i.transparentAllAbove(result_i.smileVeryBad)
        aux_num = result_i.listLabel.index(result_i.smileVeryBad)
        self.assertEqual(result_i.smileVeryBad.styleSheet(), (
            u"\n""QLabel\n""{ \n""border-radius:30%;\n""background:" + result_i.colorList[aux_num]+";\n""}"))

    def test_valueConfirm_called(self):
        result_c = SmileRating("Thanks for your rating.")
        result_c.valueConfirm(1)
        aux_num_c = result_c.listLabel.index(result_c.smileVeryBad)
        self.assertEqual(result_c.smileVeryBad.styleSheet(), (
            u"\n""QLabel\n""{ \n""border-radius:30%;\n""background:" + result_c.colorList[aux_num_c]+";\n""}"))
        self.assertEqual(result_c.smileBad.isVisible(), False)
        self.assertEqual(result_c.smileRegular.isVisible(), False)
        self.assertEqual(result_c.smileGood.isVisible(), False)
        self.assertEqual(result_c.smileVeryGood.isVisible(), False)

    def test_hideAllExcept(self):
        result_j = SmileRating("Thanks for your rating.")
        result_j.hideAllExcept(result_j.smileVeryBad)
        aux_num_j = result_j.listLabel.index(result_j.smileVeryBad)
        self.assertEqual(result_j.smileVeryBad.styleSheet(), (
            u"\n""QLabel\n""{ \n""border-radius:30%;\n""background:" + result_j.colorList[aux_num_j]+";\n""}"))
        self.assertEqual(result_j.smileBad.isVisible(), False)
        self.assertEqual(result_j.smileRegular.isVisible(), False)
        self.assertEqual(result_j.smileGood.isVisible(), False)
        self.assertEqual(result_j.smileVeryGood.isVisible(), False)

    def test_myMsn_property(self):
        result_d = SmileRating("Thanks for your rating.")
        result_d.myMsn = "test"
        self.assertEqual(result_d.myMsn, "test")

    def test_animation(self):
        app = QApplication.instance()
        if app == None:
            app = QApplication([])
        window = QWidget()
        result_g = SmileRating("Thanks for your rating.")
        result_g.child = result_g.smileVeryGood
        result_g.animationStart()
        self.assertEqual(result_g.end, True)

    def test_setEnd(self):
        result_h = SmileRating("Thanks for your rating.")
        result_h.child = result_h.smileVeryGood
        result_h.setEnd(result_h.child)
        self.assertTrue(result_h.end)


if __name__ == '__main__':
    unittest.main()
