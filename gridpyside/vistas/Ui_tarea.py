# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tarea.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_QTarea(object):
    def setupUi(self, QTarea):
        if not QTarea.objectName():
            QTarea.setObjectName(u"QTarea")
        QTarea.setWindowModality(Qt.WindowModal)
        QTarea.resize(305, 289)
        QTarea.setStyleSheet(u"border-top-color: rgb(162, 10, 10);\n"
"border-color: rgb(121, 147, 81);\n"
"background-color: rgb(162, 10, 10);\n"
"color: rgb(246, 238, 201);")
        self.widget = QWidget(QTarea)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 220, 239, 25))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnGuardar = QPushButton(self.widget)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setStyleSheet(u"background-color: rgb(246, 238, 201);\n"
"color: rgb(162, 10, 10);")

        self.horizontalLayout.addWidget(self.btnGuardar)

        self.btnCancelar = QPushButton(self.widget)
        self.btnCancelar.setObjectName(u"btnCancelar")
        self.btnCancelar.setStyleSheet(u"background-color: rgb(246, 238, 201);\n"
"color: rgb(162, 10, 10);")

        self.horizontalLayout.addWidget(self.btnCancelar)

        self.btnLimpiar = QPushButton(self.widget)
        self.btnLimpiar.setObjectName(u"btnLimpiar")
        self.btnLimpiar.setStyleSheet(u"background-color: rgb(246, 238, 201);\n"
"color: rgb(162, 10, 10);")

        self.horizontalLayout.addWidget(self.btnLimpiar)

        self.widget1 = QWidget(QTarea)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(30, 30, 241, 172))
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.editDescripcion = QLineEdit(self.widget1)
        self.editDescripcion.setObjectName(u"editDescripcion")
        self.editDescripcion.setStyleSheet(u"background-color: rgb(246, 238, 201);\n"
"color: rgb(162, 10, 10);")

        self.verticalLayout.addWidget(self.editDescripcion)

        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboEstados = QComboBox(self.widget1)
        self.comboEstados.setObjectName(u"comboEstados")
        self.comboEstados.setStyleSheet(u"background-color: rgb(246, 238, 201);\n"
"color: rgb(162, 10, 10);")

        self.horizontalLayout_2.addWidget(self.comboEstados)

        self.chqConFchaFin = QCheckBox(self.widget1)
        self.chqConFchaFin.setObjectName(u"chqConFchaFin")
        self.chqConFchaFin.setLayoutDirection(Qt.LeftToRight)
        self.chqConFchaFin.setChecked(True)

        self.horizontalLayout_2.addWidget(self.chqConFchaFin)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.tareaDiaOrigen = QDateEdit(self.widget1)
        self.tareaDiaOrigen.setObjectName(u"tareaDiaOrigen")
        self.tareaDiaOrigen.setLayoutDirection(Qt.LeftToRight)
        self.tareaDiaOrigen.setStyleSheet(u"background-color: rgb(246, 238, 201);\n"
"color: rgb(162, 10, 10);")
        self.tareaDiaOrigen.setAlignment(Qt.AlignCenter)
        self.tareaDiaOrigen.setCalendarPopup(True)

        self.verticalLayout.addWidget(self.tareaDiaOrigen)

        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.tareaDiaFin = QDateEdit(self.widget1)
        self.tareaDiaFin.setObjectName(u"tareaDiaFin")
        self.tareaDiaFin.setLayoutDirection(Qt.LeftToRight)
        self.tareaDiaFin.setStyleSheet(u"background-color: rgb(246, 238, 201);\n"
"color: rgb(162, 10, 10);")
        self.tareaDiaFin.setAlignment(Qt.AlignCenter)
        self.tareaDiaFin.setCalendarPopup(True)

        self.verticalLayout.addWidget(self.tareaDiaFin)


        self.retranslateUi(QTarea)

        QMetaObject.connectSlotsByName(QTarea)
    # setupUi

    def retranslateUi(self, QTarea):
        QTarea.setWindowTitle(QCoreApplication.translate("QTarea", u"Tarea", None))
        self.btnGuardar.setText(QCoreApplication.translate("QTarea", u"Guardar", None))
        self.btnCancelar.setText(QCoreApplication.translate("QTarea", u"Cancelar", None))
        self.btnLimpiar.setText(QCoreApplication.translate("QTarea", u"Limpiar", None))
        self.label.setText(QCoreApplication.translate("QTarea", u"Descripcion", None))
        self.label_2.setText(QCoreApplication.translate("QTarea", u"Estado", None))
        self.chqConFchaFin.setText(QCoreApplication.translate("QTarea", u"Con fecha fin", None))
        self.label_3.setText(QCoreApplication.translate("QTarea", u"Fecha Creacion", None))
        self.tareaDiaOrigen.setDisplayFormat(QCoreApplication.translate("QTarea", u"d/M/yyyy", None))
        self.label_4.setText(QCoreApplication.translate("QTarea", u"Fecha finalizacion", None))
        self.tareaDiaFin.setDisplayFormat(QCoreApplication.translate("QTarea", u"d/M/yyyy", None))
    # retranslateUi

