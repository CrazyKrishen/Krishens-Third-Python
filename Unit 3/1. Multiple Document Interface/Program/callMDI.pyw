import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea
from mdidemo import *

class MyForm(QMainWindow):
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.mdiArea.addSubWindow(self.ui.subwindow1)
        self.ui.mdiArea.addSubWindow(self.ui.subwindow2)
        
        self.ui.showNextButton.clicked.connect(self.displayNext)
        self.ui.showPreviousButton.clicked.connect(self.displayPrevious)
        self.ui.closeAllButton.clicked.connect(self.closeAll)
        self.ui.cascadeButton.clicked.connect(self.cascadeButton)
        self.ui.tileButton.clicked.connect(self.tileArrange)
        self.ui.SubWindowButton.clicked.connect(self.subWindowView)
        self.ui.TabbedViewButton.clicked.connect(self.tabbedView)

        self.ui.actionFirst_Window.triggered.connect(self.displayNext)
        self.ui.actionSecond_Window.triggered.connect(self.displayPrevious)

    def displayNext(self):
        self.ui.mdiArea.activateNextSubWindow()

    def displayPrevious(self):
        self.ui.mdiArea.activatePreviousSubWindow()

    def closeAll(self):
        self.ui.mdiArea.closeAllSubWindows()

    def cascadeButton(self):
        self.ui.mdiArea.cascadeSubWindows()

    def tileArrange(self):
        self.ui.mdiArea.tileSubWindows()

    def subWindowView(self):
        self.ui.mdiArea.setViewMode(0)

    def tabbedView(self):
        self.ui.mdiArea.setViewMode(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())


        
