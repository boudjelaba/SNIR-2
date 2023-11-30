#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Créé : Mar 26 08:40:44 2023

@author: KB
"""


from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as Navi
from matplotlib.figure import Figure
import seaborn as sns
import pandas as pd
import sip # Pour l'installer : pip install sip

import platform

op_sys = platform.system()

class MatplotlibCanvas(FigureCanvasQTAgg):
	def __init__(self,parent=None, dpi = 120):
		fig = Figure(dpi = dpi)
		self.axes = fig.add_subplot(111)
		super(MatplotlibCanvas,self).__init__(fig)
		fig.tight_layout()
		
		

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1440, 1000)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName("gridLayout")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setObjectName("label")
		self.horizontalLayout.addWidget(self.label)
		self.comboBox = QtWidgets.QComboBox(self.centralwidget)
		self.comboBox.setObjectName("comboBox")
		self.horizontalLayout.addWidget(self.comboBox)
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setObjectName("pushButton")
		self.horizontalLayout.addWidget(self.pushButton)
		spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		self.spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout.addItem(self.spacerItem1)
		self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
		
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
		self.menubar.setObjectName("menubar")
		self.menuFile = QtWidgets.QMenu(self.menubar)
		self.menuFile.setObjectName("menuFile")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.actionOpen_csv_file = QtWidgets.QAction(MainWindow)
		self.actionOpen_csv_file.setObjectName("actionOpen_csv_file")
		self.actionExit = QtWidgets.QAction(MainWindow)
		self.actionExit.setObjectName("actionExit")
		self.menuFile.addAction(self.actionOpen_csv_file)
		self.menuFile.addAction(self.actionExit)
		self.menubar.addAction(self.menuFile.menuAction())

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		
		self.filename = ''
		self.canv = MatplotlibCanvas(self)
		self.df = []
		
		self.toolbar = Navi(self.canv,self.centralwidget)
		self.horizontalLayout.addWidget(self.toolbar)
		
		self.themes = ['bmh', 'classic', 'dark_background', 'fast', 
		'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-bright',
		 'seaborn-colorblind', 'seaborn-dark-palette', 'seaborn-dark', 
		 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook',
		 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk',
		 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'seaborn',
		 'Solarize_Light2', 'tableau-colorblind10']
		 
		self.comboBox.addItems(self.themes)
		
		self.pushButton.clicked.connect(self.getFile)
		self.comboBox.currentIndexChanged['QString'].connect(self.Update)
		self.actionExit.triggered.connect(MainWindow.close)
		self.actionOpen_csv_file.triggered.connect(self.getFile)
		
	def Update(self,value):
		print("Valeur de la liste déroulante :",value)
		plt.clf()
		plt.style.use(value)
		try:
			self.horizontalLayout.removeWidget(self.toolbar)
			self.verticalLayout.removeWidget(self.canv)
			
			sip.delete(self.toolbar)
			sip.delete(self.canv)
			self.toolbar = None
			self.canv = None
			self.verticalLayout.removeItem(self.spacerItem1)
		except Exception as e:
			print(e)
			pass
		self.canv = MatplotlibCanvas(self)
		self.toolbar = Navi(self.canv,self.centralwidget)
		
		self.horizontalLayout.addWidget(self.toolbar)
		self.verticalLayout.addWidget(self.canv)
		
		self.canv.axes.cla()
		ax = self.canv.axes
		self.df.plot(ax = self.canv.axes)
		legend = ax.legend()
		legend.set_draggable(True)
		
		ax.set_xlabel('Axe des X')
		ax.set_ylabel('Axe des Y')
		ax.set_title(self.Title)
		
		self.canv.draw()
		
		
		
		
	
	def getFile(self):
		""" Cette fonction obtiendra l'adresse de l'emplacement du fichier csv
		et appelle également une fonction readData 
		"""
		self.filename = QFileDialog.getOpenFileName(filter = "csv (*.csv)")[0]
		print("Fichier :", self.filename)
		self.readData()
	
	def readData(self):
		""" Cette fonction lira les données à l'aide de pandas et appellera 
		la fonction de mise à jour pour tracer
		"""
		import os
		base_name = os.path.basename(self.filename)
		self.Title = os.path.splitext(base_name)[0]
		print('Fichier',self.Title )
		self.df = pd.read_csv(self.filename,encoding = 'utf-8').fillna(0)
		self.Update(self.themes[0]) # Le thème 0 est le thème par défaut : bmh
	

	
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Courbe avec PyQt5"))
		self.label.setText(_translate("MainWindow", "Sélectionner le thème"))
		self.pushButton.setText(_translate("MainWindow", "Ouvrir"))
		self.menuFile.setTitle(_translate("MainWindow", "Fichier"))
		self.actionOpen_csv_file.setText(_translate("MainWindow", "Ouvrir un fichier CSV"))
		self.actionExit.setText(_translate("MainWindow", "Fermer"))

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	
	MainWindow.show()
	sys.exit(app.exec_())

