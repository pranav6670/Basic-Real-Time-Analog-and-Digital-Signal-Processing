from PyQt5 import QtGui,QtCore
import sys
import bsui
import numpy as np
import pylab
import time
import pyqtgraph

class ExampleApp(QtGui.QMainWindow, bsui.Ui_MainWindow):
    def __init__(self, parent=None):
        pyqtgraph.setConfigOption('background', 'w') #before loading widget
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.updatebtn.clicked.connect(self.update)
        self.plotter.plotItem.showGrid(True, True, 0.7)
        self.npoints.setMinimum(1)
        self.npoints.setMaximum(10)

    def update(self):
        t1=time.clock()
        points, X, Y = self.sine()
        C=pyqtgraph.hsvColor(time.time()/5%1,alpha=.8)
        pen=pyqtgraph.mkPen(color=C,width=10)
        self.plotter.plot(X,Y,pen=pen,clear=True)
        print("update took %.02f ms"%((time.clock()-t1)*1000))
        if self.updatcheckbox.isChecked():
            QtCore.QTimer.singleShot(1, self.update) # QUICKLY repeat

    def sine(self):
        points=1000 #number of data points
        X=np.arange(points)
        c = self.npoints.value()
        Y=np.sin(np.arange(points)/points*c*np.pi+time.time())
        return points, X, Y



if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    form.update() #start with something
    app.exec_()
    print("DONE")