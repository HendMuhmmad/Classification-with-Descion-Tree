# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Mainf.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(525, 475)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.TrainModel = QtWidgets.QWidget()
        self.TrainModel.setAccessibleName("")
        self.TrainModel.setObjectName("TrainModel")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.TrainModel)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeImg = QtWidgets.QLabel(self.TrainModel)
        self.treeImg.setAlignment(QtCore.Qt.AlignCenter)
        self.treeImg.setObjectName("treeImg")
        self.horizontalLayout.addWidget(self.treeImg)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.indicator = QtWidgets.QLabel(self.TrainModel)
        self.indicator.setAlignment(QtCore.Qt.AlignCenter)
        self.indicator.setObjectName("indicator")
        self.horizontalLayout_5.addWidget(self.indicator)
        self.label_2 = QtWidgets.QLabel(self.TrainModel)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.execTime = QtWidgets.QLabel(self.TrainModel)
        self.execTime.setObjectName("execTime")
        self.horizontalLayout_5.addWidget(self.execTime)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.trainBtn = QtWidgets.QPushButton(self.TrainModel)
        self.trainBtn.setObjectName("trainBtn")
        self.verticalLayout_2.addWidget(self.trainBtn)
        self.tabWidget.addTab(self.TrainModel, "")
        self.Accuracy = QtWidgets.QWidget()
        self.Accuracy.setObjectName("Accuracy")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Accuracy)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.accuracyTable = QtWidgets.QTableWidget(self.Accuracy)
        self.accuracyTable.setObjectName("accuracyTable")
        self.accuracyTable.setColumnCount(0)
        self.accuracyTable.setRowCount(0)
        self.verticalLayout_3.addWidget(self.accuracyTable)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.Accuracy)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.accuracy = QtWidgets.QLabel(self.Accuracy)
        self.accuracy.setAlignment(QtCore.Qt.AlignCenter)
        self.accuracy.setObjectName("accuracy")
        self.horizontalLayout_2.addWidget(self.accuracy)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.accuracyBtn = QtWidgets.QPushButton(self.Accuracy)
        self.accuracyBtn.setObjectName("accuracyBtn")
        self.verticalLayout_3.addWidget(self.accuracyBtn)
        self.tabWidget.addTab(self.Accuracy, "")
        self.UserInput = QtWidgets.QWidget()
        self.UserInput.setObjectName("UserInput")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.UserInput)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.UserInput)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.Input = QtWidgets.QTextEdit(self.UserInput)
        self.Input.setObjectName("Input")
        self.verticalLayout_5.addWidget(self.Input)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.UserInput)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.prediction = QtWidgets.QLabel(self.UserInput)
        self.prediction.setAlignment(QtCore.Qt.AlignCenter)
        self.prediction.setObjectName("prediction")
        self.horizontalLayout_3.addWidget(self.prediction)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.enterBtn = QtWidgets.QPushButton(self.UserInput)
        self.enterBtn.setObjectName("enterBtn")
        self.verticalLayout_5.addWidget(self.enterBtn)
        self.tabWidget.addTab(self.UserInput, "")
        self.Prediction = QtWidgets.QWidget()
        self.Prediction.setObjectName("Prediction")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Prediction)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.predictFile = QtWidgets.QTableWidget(self.Prediction)
        self.predictFile.setObjectName("predictFile")
        self.predictFile.setColumnCount(0)
        self.predictFile.setRowCount(0)
        self.verticalLayout_6.addWidget(self.predictFile)
        self.predictBtn = QtWidgets.QPushButton(self.Prediction)
        self.predictBtn.setObjectName("predictBtn")
        self.verticalLayout_6.addWidget(self.predictBtn)
        self.tabWidget.addTab(self.Prediction, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Decision Tree Classifier"))
        self.treeImg.setText(_translate("MainWindow", "Tree Representation"))
        self.indicator.setText(_translate("MainWindow", "_______"))
        self.label_2.setText(_translate("MainWindow", "Execution time :"))
        self.execTime.setText(_translate("MainWindow", "_______"))
        self.trainBtn.setText(_translate("MainWindow", "Start Model Trainig"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TrainModel), _translate("MainWindow", "Train Model"))
        self.label_3.setText(_translate("MainWindow", "Calculate Accuracy Based on evaluation data"))
        self.accuracy.setText(_translate("MainWindow", "0.0"))
        self.accuracyBtn.setText(_translate("MainWindow", "Calculate accuracy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Accuracy), _translate("MainWindow", "Accuracy"))
        self.label_4.setText(_translate("MainWindow", "Enter Text Review:"))
        self.label_6.setText(_translate("MainWindow", "Result :"))
        self.prediction.setText(_translate("MainWindow", "__________"))
        self.enterBtn.setText(_translate("MainWindow", "Enter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.UserInput), _translate("MainWindow", "User input"))
        self.predictBtn.setText(_translate("MainWindow", "View Prediction File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Prediction), _translate("MainWindow", "Prediction"))
