import sys
import json
# from faker import Faker
import qtawesome as qta
# https://qtawesome.readthedocs.io/en/latest/usage.html
from datetime import datetime
from PySide2.QtWidgets import QApplication, QDialog , QMainWindow, QTableWidgetItem, QAbstractItemView, QMessageBox#, QtWidget
from vistas.Ui_principal import Ui_QPrincipal
from aplicacion.tarea import Tarea


class Principal(QMainWindow):
    def __init__(self):
        super(Principal, self).__init__()
        self.tareas = list()
        self.item = None
        self.ui = Ui_QPrincipal()
        self.ui.setupUi(self)
        iconAgregar = qta.icon('fa.plus')
        self.ui.btnAdd.clicked.connect(self.agregar)
        self.ui.btnEliminar.clicked.connect(self.eliminar)
        self.ui.btnAdd.setIcon(qta.icon('mdi.plus-circle'))
        self.ui.btnModificar.setIcon(qta.icon('mdi.pencil-circle'))
        self.ui.btnEliminar.setIcon(qta.icon('mdi.delete-circle'))
        self.formatearTabla(self.tareas)
        self.ui.tablaDatos.clicked.connect(self.recuperarData)

    

    def agregar(self):
        task = Tarea()
        task.exec_()
        if task.datos:
            self.tareas.append(task.datos)    
            print(task.datos)
            self.formatearTabla(self.tareas)
        else:
            print('Se cancelo el agregar')

    def crearDialogo(self,icono , titulo, texto, botones): return QMessageBox(icono,titulo, texto,botones)

    def formatearTabla(self,data: list):
        self.ui.tablaDatos.setColumnCount(4)
        self.ui.tablaDatos.setSelectionBehavior(QAbstractItemView.SelectRows) 
        # ⬆⬆⬆ Permite la seleccion de toda la fila ⬆⬆⬆
        self.ui.tablaDatos.setRowCount(len(self.tareas))
        self.ui.tablaDatos.setHorizontalHeaderLabels('Descripcion Estado FInicio FFin'.split())
        for i, row in enumerate(data):
            self.ui.tablaDatos.takeVerticalHeaderItem(i)
            for j, value in enumerate(row.values()):
                self.ui.tablaDatos.setItem(i , j, QTableWidgetItem(value))
    def recuperarData(self): 
            self.item = self.ui.tablaDatos.currentRow()
            print(f"En Recuperar Item es {self.item}")

    def eliminar(self):
        if self.item != None:
            msg = self.crearDialogo(QMessageBox.Warning, 'Atencion', 'Esta accion eliminara una tarea. Esta de acuerdo?', QMessageBox.Ok | QMessageBox.Cancel)
            resp = msg.exec_()
            if resp ==  QMessageBox.Ok:
                self.ui.tablaDatos.removeRow(self.item)
                self.formatearTabla(self.tareas)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = Principal()
    myapp.show()
    sys.exit(app.exec_())        