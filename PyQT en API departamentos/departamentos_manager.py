import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QComboBox, QTableView, QHeaderView, QAbstractItemView, QHBoxLayout, QVBoxLayout, QSizePolicy
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from libreria_modelo import TablaModelo
from libreria_datos_departamentos import ClienteDepartamentos 
import pandas as pd

class VentanaInformacionDepartamentos(QWidget):

    def __init__(self):
        super().__init__() 
        self.inicializarUI() 

    def inicializarUI(self):
        self.setMinimumSize(1000, 600)
        self.setWindowTitle("Gestionar departamentos de Colombia")
        self.crearModelo()
        self.configurarPantalla()
        self.show() 

    def crearModelo(self):
        """Configura el modelo y las cabeceras, y rellena el modelo."""
        datos = pd.DataFrame(ClienteDepartamentos.consultar_departamentos(), 
                columns=['Id', 'Nombre', 'Descripción', 'Capital ID', 'Municipios', 'Superficie', 'Población', 'Prefijo Telefónico', 'ID País'])
        self.model = TablaModelo(datos)

    def configurarPantalla(self):
        """Crear y organizar widgets en la pantalla principal"""
        icons_path = "icons"    

        title = QLabel("Gestor de Departamentos - ISF12A - Apl. Escr. I")
        title.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        title.setStyleSheet("font: bold 24px")

        boton_agregar_registro = QPushButton("Agregar departamento")
        boton_agregar_registro.setIcon(QIcon(os.path.join(icons_path, "agregar_estudiante.png")))
        boton_agregar_registro.setStyleSheet("padding: 10px")
        boton_agregar_registro.clicked.connect(self.agregarRegistro)

        boton_eliminar_registro = QPushButton("Eliminar departamento")
        boton_eliminar_registro.setIcon(QIcon(os.path.join(icons_path, "eliminar.png")))
        boton_eliminar_registro.setStyleSheet("padding: 10px")
        boton_eliminar_registro.clicked.connect(self.eliminarRegistro)

        sorting_options = ["Ordenar por ID", 
                           "Ordenar por nombre",
                           "Ordenar por descripción"]
        sort_combo = QComboBox()
        sort_combo.addItems(sorting_options)

        buttons_h_box = QHBoxLayout()
        buttons_h_box.addWidget(boton_agregar_registro)
        buttons_h_box.addWidget(boton_eliminar_registro)
        buttons_h_box.addStretch()
        buttons_h_box.addWidget(sort_combo)

        edit_container = QWidget()
        edit_container.setLayout(buttons_h_box)

        self.table_view = QTableView()
        self.table_view.setModel(self.model)

        horizontal = self.table_view.horizontalHeader()
        horizontal.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        vertical = self.table_view.verticalHeader()
        vertical.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.table_view.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        main_v_box = QVBoxLayout()
        main_v_box.addWidget(title, Qt.AlignmentFlag.AlignLeft)
        main_v_box.addWidget(edit_container)
        main_v_box.addWidget(self.table_view)
        self.setLayout(main_v_box)

    def agregarRegistro(self):
        """Agregar un registro a la última fila de la tabla"""
        last_row = self.model.rowCount()
        self.model.insertRow(last_row)
        

    def eliminarRegistro(self):
        current_item = self.table_view.selectedIndexes()
        for index in current_item:
            self.model.removeRow(index.row())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaInformacionDepartamentos()
    sys.exit(app.exec())
    
def manejar_datos_departamentos():
    datos_departamentos = ClienteDepartamentos.consultar_departamentos()
    for departamento in datos_departamentos[:5]:
        print(departamento)

