import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject

import pyopenms

from GUI_EXAMPLE_BASE import GUI_EXAMPLE_BASE
sys.path.insert(0, '../view')
from TICWidget import TICWidget

# mock object to test the mouse click signal by TICWidget
class TestMouseClick(QObject):
    def __init__(self):
        QObject.__init__(self)

    def printRT(self, rt):
        print("Mouse clicked at RT=" + str(rt))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GUI_EXAMPLE_BASE() # plain QMainWindow with basic layout and menu bar

    # load spectra and add example widget to window
    exp = pyopenms.MSExperiment()
    pyopenms.MzMLFile().load("../data/190509_Ova_native_25ngul_R.mzML", exp)
    example_widget = TICWidget(ex)
    example_widget.setTIC(exp.getTIC())
    mouse_click_test = TestMouseClick()
    example_widget.sigRTClicked.connect(mouse_click_test.printRT)
    ex.setExampleWidget(example_widget)
    ex.show()
    sys.exit(app.exec_())