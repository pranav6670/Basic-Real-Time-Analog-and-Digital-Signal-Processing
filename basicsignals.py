from PyQt5 import QtGui,QtCore
import sys
import bsui
import numpy as np
import pylab
import time
import pyqtgraph
from scipy import signal

class ExampleApp(QtGui.QMainWindow, bsui.Ui_MainWindow):
    def __init__(self, parent=None):
        pyqtgraph.setConfigOption('background', 'w') #before loading widget
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.updatebtn.clicked.connect(self.update)
        self.plotter.plotItem.showGrid(True, True, 0.7)
        self.npoints.setMinimum(1)
        self.npoints.setMaximum(10)
        self.points = 1000 #number of data points
        self.X = np.arange(self.points)


    def update(self):
        X = self.X
        t1 = time.clock()
        Y = self.sine()
        C = pyqtgraph.hsvColor(time.time() / 5%1, alpha=.5)
        pen = pyqtgraph.mkPen(color=C, width=5)
        self.plotter.plot(X,Y,pen=pen,clear=True)
        print("Update took %.02f ms"%((time.clock() - t1) * 1000))
        if self.updatcheckbox.isChecked():
            QtCore.QTimer.singleShot(1, self.update) # QUICKLY repeat

    def sine(self):
        self.c = self.npoints.value()
        Y = np.sin(np.arange(self.points) / self.points * self.c * np.pi + time.time())
        return Y

    def exponential(self):
        self.c = self.npoints.value()
        Y = np.exp()



if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    form.update() #start with something
    app.exec_()
    print("DONE")