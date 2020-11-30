import sys
import json
# from faker import Faker
from datetime import datetime
from PySide2.QtWidgets import QDialog
from vistas.Ui_tarea import Ui_QTarea


class Tarea(QDialog):
    def __init__(self):
        super(Tarea, self).__init__()
        self.datos = dict()
        self.ui = Ui_QTarea()
        self.ui.setupUi(self)
        self.ui.btnLimpiar.clicked.connect(self.limpiarCampos)
        self.ui.btnGuardar.clicked.connect(self.guardarDatos)
        self.ui.btnCancelar.clicked.connect(self.cancelar)
        self.ui.chqConFchaFin.stateChanged.connect(self.verificarCheck)
        self.iniciarCombo()
        self.limpiarCampos()
        self.auxdatefin = self.ui.tareaDiaFin.date()
        self.verificarCheck()
        self.tarea = dict()


    def cancelar(self):
        self.datos = None
        self.done(1) # no hay datos cargados

    def verificarCheck(self):
        print(f"Estado del checkbox: {self.ui.chqConFchaFin.isChecked()}")
        if self.ui.chqConFchaFin.isChecked():
            self.ui.tareaDiaFin.setReadOnly(False)
            self.ui.tareaDiaOrigen.setDate(self.auxdatefin)
        else:
            self.ui.tareaDiaFin.setReadOnly(True)



    def limpiarCampos(self):
        self.ui.editDescripcion.clear()
        self.ui.comboEstados.setCurrentIndex(0)
        self.ui.chqConFchaFin.checked = True
        self.ui.tareaDiaOrigen.setDate(datetime.today())
        self.ui.tareaDiaFin.setDate(datetime.today())
    
    def iniciarCombo(self):
        self.ui.comboEstados.addItems('Facil Normal Revisar Urgente'.split())


    def guardarDatos(self):
        self.datos['descripcion'] = self.ui.editDescripcion.text()
        self.datos['estado'] = self.ui.comboEstados.currentText()
        self.datos['fecha_inicio'] = self.ui.tareaDiaOrigen.date().toString('dd/MM/yyyy')
        self.datos['fecha_fin'] = self.ui.tareaDiaFin.date().toString('dd/MM/yyyy')
        self.done(0)
