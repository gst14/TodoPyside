import sys
import json
# from faker import Faker
from datetime import datetime
from PySide2.QtWidgets import QApplication, QDialog , QMainWindow, QTableWidgetItem, QAbstractItemView#, QtWidget
from vistas.Ui_principal import Ui_QPrincipal
from aplicacion.tarea import Tarea


class Principal(QMainWindow):
    def __init__(self):
        super(Principal, self).__init__()
        self.tareas = list()
        self.datos = dict()
        self.ui = Ui_QPrincipal()
        self.ui.setupUi(self)
        self.ui.btnAdd.clicked.connect(self.agregar)
        self.formatearTabla(self.tareas)


    def agregar(self):
        task = Tarea()
        task.exec_()
        self.tareas.append(task.datos)    
        print(task.datos)
        self.formatearTabla(self.tareas)

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


        # rowPosition = self.ui.tablaDatos.rowCount()
        # self.ui.tablaDatos.insertRow(rowPosition)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = Principal()
    myapp.show()
    sys.exit(app.exec_())        