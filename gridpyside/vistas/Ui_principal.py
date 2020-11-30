# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_QPrincipal(object):
    def setupUi(self, QPrincipal):
        if not QPrincipal.objectName():
            QPrincipal.setObjectName(u"QPrincipal")
        QPrincipal.resize(474, 299)
        QPrincipal.setLayoutDirection(Qt.LeftToRight)
        QPrincipal.setAutoFillBackground(False)
        QPrincipal.setStyleSheet(u"border-top-color: rgb(162, 10, 10);\n"
"border-color: rgb(121, 147, 81);\n"
"background-color: rgb(162, 10, 10);\n"
"color: rgb(246, 238, 201);")
        QPrincipal.setTabShape(QTabWidget.Triangular)
        self.centralwidget = QWidget(QPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(376, 30, 75, 23))
        self.pushButton.setStyleSheet(u"background-color: rgb(246, 238, 201);\n"
"color: rgb(162, 10, 10);")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 30, 281, 20))
        self.lineEdit.setStyleSheet(u"background-color: rgb(246, 238, 201);\n"
"color: rgb(162, 10, 10);")
        self.tablaDatos = QTableWidget(self.centralwidget)
        self.tablaDatos.setObjectName(u"tablaDatos")
        self.tablaDatos.setGeometry(QRect(20, 61, 441, 211))
        self.tablaDatos.setStyleSheet(u"background-color: rgb(246, 238, 201);\n"
"color: rgb(0, 0, 0);")
        self.tablaDatos.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.tablaDatos.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tablaDatos.setTextElideMode(Qt.ElideNone)
        self.tablaDatos.setGridStyle(Qt.DashDotDotLine)
        self.tablaDatos.setCornerButtonEnabled(False)
        self.tablaDatos.horizontalHeader().setCascadingSectionResizes(True)
        self.tablaDatos.verticalHeader().setVisible(False)
        self.btnAdd = QPushButton(self.centralwidget)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setGeometry(QRect(20, 30, 61, 23))
        self.btnAdd.setToolTipDuration(3)
        self.btnAdd.setStyleSheet(u"background-color: rgb(246, 238, 201);\n"
"color: rgb(162, 10, 10);\n"
"selection-color: rgb(162, 10, 10);\n"
"selection-background-color: rgb(246, 238, 201);")
        QPrincipal.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(QPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        QPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(QPrincipal)

        QMetaObject.connectSlotsByName(QPrincipal)
    # setupUi

    def retranslateUi(self, QPrincipal):
        QPrincipal.setWindowTitle(QCoreApplication.translate("QPrincipal", u"Inicio", None))
        self.pushButton.setText(QCoreApplication.translate("QPrincipal", u"Buscar", None))
#if QT_CONFIG(tooltip)
        self.btnAdd.setToolTip(QCoreApplication.translate("QPrincipal", u"Ctrl + A", None))
#endif // QT_CONFIG(tooltip)
        self.btnAdd.setText(QCoreApplication.translate("QPrincipal", u"Agregar", None))
#if QT_CONFIG(shortcut)
        self.btnAdd.setShortcut(QCoreApplication.translate("QPrincipal", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

