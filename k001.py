#!/usr/bin/python
#...GIT?

from PyQt4 import QtGui, QtCore
import sys

import UImainwindow

class ImageViewer(QtGui.QMainWindow, UImainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.setupUi(self)

    def main(self):
        self.show()

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    imageViewer = ImageViewer()
    imageViewer.main()
    app.exec_()
