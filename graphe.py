# PyQt5 Matplotlib

import sys
import numpy as np
from GUI import*
from PyQt5 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class MiApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)

        self.graphe = Canvas_graphe()
        self.ui.verticalLayout_graphe.addWidget(self.graphe)

        self.ui.slider1.valueChanged.connect(self.slider_un)
        self.ui.slider2.valueChanged.connect(self.slider_deux)

    def slider_un(self, event):
        self.graphe.donnees1(event) 

    def slider_deux(self, event):
        self.graphe.donnees2(event) 


class Canvas_graphe(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(facecolor='gray')
        super().__init__(self.fig) 
        self.ax.grid()
        self.ax.margins(x=0)



        self.niveau1 = 10
        self.niveau2 = 1
        self.graphe_donnees()

    def donnees1(self, valeur1):
        self.niveau1 = valeur1*0.1

    def donnees2(self, valeur2):
        self.niveau2 = valeur2*0.05

    def graphe_donnees(self):
        plt.title("Courbes dans PyQt5 avec Matplotlib")
        #plt.xlim(-4, 32)
        #plt.ylim(-12, 12)

        x = np.arange(-np.pi, 10*np.pi, 0.01) 
        line, = self.ax.plot(x, self.niveau1*np.sin(self.niveau2*x), color='r',linewidth=2)
        self.draw()     
        line.set_ydata(np.sin(x)+24)             

        #print(self.niveau1, self.niveau2)
        QtCore.QTimer.singleShot(10, self.graphe_donnees)


if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())  

        #self.ax = plt.axes()        
        #self.ax=plt.gca()
        #plt.axis('off')        
        #self.fig.subplots_adjust(top=1.1 ,bottom=-0.1, left=-0.1, right=1.1)
        #self.ax.get_xaxis().set_visible(False)
        #self.ax.spines['right'].set_visible(False)
        #self.ax.spines['top'].set_visible(False)
        #self.ax.spines['bottom'].set_visible(False)
        #self.ax.spines['left'].set_visible(False)