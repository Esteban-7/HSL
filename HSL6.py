from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class creacion_listas(QMainWindow):
    ##la funcion __init__ define los elementos básicos que debe tener la clase Window, hereda características del paquete mismo, agrega el tamaño el nombre de la app, así como las funciones de interacción con los elementos.
    def __init__(self):
        super(creacion_listas,self).__init__()
        self.setWindowTitle("HSL")
        self.setGeometry(500,100,950,730)
        self.initUI()
    
    ##la función initUI define todos los elementos que tendrá la interfaz
    def initUI(self): 
        #label,  bienvenida inicial
        self.label_bienvenida=QtWidgets.QLabel(self)
        self.label_bienvenida.setText("Herramienta de Solicitud de Listas V-0.5")
        self.label_bienvenida.move(5,5)
        self.label_bienvenida.adjustSize()

        #label,texto: crea el campo en el cual se edita la ruta en la cual debe crearse la solicitud
        self.label_ruta = QtWidgets.QLabel(self)
        self.label_ruta.setGeometry(QtCore.QRect(20, 25, 181, 16))
        self.label_ruta.setText("Directorio de la lista:")
        
        self.ruta=QtWidgets.QLineEdit(self)
        self.ruta_inicial="A:/2019/Esteban/Solicitudes/" #este es el path predeterminado en el cual quedan las listas.
        self.ruta.setText(self.ruta_inicial)
        self.ruta.setGeometry(QtCore.QRect(20, 50, 300, 20))

        #texto: campo en donde se crea el nombre de la lista
        self.label_nombre_lista = QtWidgets.QLabel(self)
        self.label_nombre_lista.setGeometry(QtCore.QRect(330, 25, 181, 16))
        self.label_nombre_lista.setText("Nombre de la lista:")
        self.nombre_lista=QtWidgets.QLineEdit(self)
        self.nombre_lista.setGeometry(330,50,300,20)
    
        #botón revisar: al hacer click se llama a una función (definida más abajo) la cual lee todos los campos en la aplicación y crea una lista con los parámetros que debe tener la lista.
        self.revisar=QtWidgets.QPushButton(self)
        self.revisar.setText("Revisar")
        self.revisar.move(708,500)
        self.revisar.clicked.connect(self.revisar_lista)

        #botón solicitar: llama a una función (definida más abajo) que crea el archivo de la solicitud según los parámetros definidos
        self.solicitar=QtWidgets.QPushButton(self)
        self.solicitar.setText("Solicitar")
        self.solicitar.move(708,545)
        self.solicitar.clicked.connect(self.solicitar_l)

        #botón solicitar: llama a una función (definida más abajo) que hace un reset de todos los campos disponibles para poder definir los parámetros de una nueva lista
        self.nueva=QtWidgets.QPushButton(self)
        self.nueva.setText("Nueva Lista")
        self.nueva.move(708,590)
        self.nueva.clicked.connect(self.nueva_l)

        #label: texto el cual muestr el estado de la solicitud. 
        self.lista=QtWidgets.QLabel(self)
        self.lista.setText("No se ha solicitado ninguna lista.")
        self.lista.move(708,630)
        self.lista.adjustSize()
        
        #region Creacion group_box 
        # esta region crea todos los recuadros en donde se ubican los diferentes botones y selectores. Se definen títulos de los cuadros, el tamaño y la posición
        self.box_portafolio = QtWidgets.QGroupBox(self)
        self.box_portafolio.setGeometry(QtCore.QRect(20, 90, 182, 170))
        self.box_portafolio.setTitle("Portafolio")

        self.tipo_gestion = QtWidgets.QGroupBox(self)
        self.tipo_gestion.setGeometry(QtCore.QRect(207, 90, 170, 80))
        self.tipo_gestion.setTitle("Tipo Gestión")
        
        self.segmento_reintegra = QtWidgets.QGroupBox(self)
        self.segmento_reintegra.setGeometry(QtCore.QRect(207, 170, 170, 90))
        self.segmento_reintegra.setTitle("Segmento Reintegra")
        
        self.tamano_lista = QtWidgets.QGroupBox(self)
        self.tamano_lista.setGeometry(QtCore.QRect(400, 90, 545, 170))
        self.tamano_lista.setTitle("Tamaño: Última Gestión")

        self.box_avanzado = QtWidgets.QGroupBox(self)
        self.box_avanzado.setGeometry(QtCore.QRect(20, 270, 760, 190))
        self.box_avanzado.setTitle("Avanzado")

        self.resumen=QtWidgets.QGroupBox(self)
        self.resumen.setGeometry(QtCore.QRect(20,470,683,250))
        self.resumen.setTitle("Resumen Lista")

        self.reciente=QtWidgets.QGroupBox(self)
        self.reciente.setGeometry(QtCore.QRect(785,270,155,150))
        self.reciente.setTitle("Reciente")
        #endregion

        #region Check_tipo_gestion
        #en esta región, dentro del recuadro determinado para los tipos de gestion se crean los checkbox para escoger los tipo_gestion que debe tener la lista
        self.check_especial = QtWidgets.QCheckBox(self.tipo_gestion)
        self.check_especial.setGeometry(QtCore.QRect(10, 15, 111, 17))
        self.check_especial.setText("Especial")

        self.check_masivo = QtWidgets.QCheckBox(self.tipo_gestion)
        self.check_masivo.setGeometry(QtCore.QRect(10, 35, 91, 17))
        self.check_masivo.setText("Masivo")
        
        self.check_fng = QtWidgets.QCheckBox(self.tipo_gestion)
        self.check_fng.setGeometry(QtCore.QRect(10, 55, 131, 17))
        self.check_fng.setText("FNG")
        
        #endregion

        #region tamaño Segmentos Reintegra
        #Aquí se crean los campos numéricos los cuales definen el tamaño de las listas cuando estas son de cartera de Reintegra, dado que el tamaño de define por los segmentos definidos
        self.tamano_seg_1 = QtWidgets.QLabel(self.segmento_reintegra)
        self.tamano_seg_1.setGeometry(QtCore.QRect(5, 20, 61, 15))
        self.tamano_seg_1.setText("1")
        self.tamano_seg_1_numero = QtWidgets.QSpinBox(self.segmento_reintegra)
        self.tamano_seg_1_numero.setGeometry(QtCore.QRect(72, 20, 49, 18))
        self.tamano_seg_1_numero.setMinimum(1)
        self.tamano_seg_1_numero.setMaximum(100000)

        self.tamano_seg_2 = QtWidgets.QLabel(self.segmento_reintegra)
        self.tamano_seg_2.setGeometry(QtCore.QRect(5, 45, 61, 15))
        self.tamano_seg_2.setText("2")
        self.tamano_seg_2_numero = QtWidgets.QSpinBox(self.segmento_reintegra)
        self.tamano_seg_2_numero.setGeometry(QtCore.QRect(72, 45, 49, 18))
        self.tamano_seg_2_numero.setMinimum(1)
        self.tamano_seg_2_numero.setMaximum(100000)

        self.tamano_seg_3 = QtWidgets.QLabel(self.segmento_reintegra)
        self.tamano_seg_3.setGeometry(QtCore.QRect(5, 70, 61, 15))
        self.tamano_seg_3.setText("3")
        self.tamano_seg_3_numero = QtWidgets.QSpinBox(self.segmento_reintegra)
        self.tamano_seg_3_numero.setGeometry(QtCore.QRect(72, 70, 49, 18))
        self.tamano_seg_3_numero.setMinimum(1)
        self.tamano_seg_3_numero.setMaximum(100000)
        #endregion


        #region Scroll area portafolio
        #en este apartado se crea primero un espacio scroll dentro del cual se ponen todas las opciones de portafolios para que se puedan ver todos.
        self.verticalLayoutWidget = QtWidgets.QWidget(self.box_portafolio)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 12, 182, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_portafolio = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_portafolio.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_portafolio.setObjectName("verticalLayout_portafolio")
        self.scrollArea_portafolio = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea_portafolio.setWidgetResizable(True)
        self.scrollArea_portafolio.setFrameShadow(1)
        self.scrollArea_portafolio.setObjectName("scrollArea_portafolio")
        self.scrollAreaWidgetContents_portafolio = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_portafolio.setGeometry(QtCore.QRect(0, 0, 130, 173))
        self.scrollAreaWidgetContents_portafolio.setObjectName("scrollAreaWidgetContents_portafolio")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_portafolio)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea_portafolio.setWidget(self.scrollAreaWidgetContents_portafolio)
        self.verticalLayout_portafolio.addWidget(self.scrollArea_portafolio)

        #posteriormente se crean todos las opciones de portafolio. En caso de que lleguen nuevos portafolios se deben incluir en este apartado.
        self.check_NEW_CREDIT_1 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_NEW_CREDIT_1.setText('NEW_CREDIT_1')
        self.verticalLayout_2.addWidget(self.check_NEW_CREDIT_1)
        self.check_NEW_CREDIT_11_BBVA = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_NEW_CREDIT_11_BBVA.setText('NEW_CREDIT_11_BBVA')
        self.verticalLayout_2.addWidget(self.check_NEW_CREDIT_11_BBVA)
        self.check_NEW_CREDIT_12_BBVA = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_NEW_CREDIT_12_BBVA.setText('NEW_CREDIT_12_BBVA')
        self.verticalLayout_2.addWidget(self.check_NEW_CREDIT_12_BBVA)
        self.check_NEW_CREDIT_6 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_NEW_CREDIT_6.setText('NEW_CREDIT_6')
        self.verticalLayout_2.addWidget(self.check_NEW_CREDIT_6)
        self.check_NEW_CREDIT_7 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_NEW_CREDIT_7.setText('NEW_CREDIT_7')
        self.verticalLayout_2.addWidget(self.check_NEW_CREDIT_7)
        self.check_NEWCREDIT_10 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_NEWCREDIT_10.setText('NEWCREDIT_10')
        self.verticalLayout_2.addWidget(self.check_NEWCREDIT_10)
        self.check_NEWCREDIT_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_NEWCREDIT_4.setText('NEWCREDIT_4')
        self.verticalLayout_2.addWidget(self.check_NEWCREDIT_4)
        self.check_PLATAFORMA_1 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_PLATAFORMA_1.setText('PLATAFORMA_1')
        self.verticalLayout_2.addWidget(self.check_PLATAFORMA_1)
        self.check_PLATAFORMA_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_PLATAFORMA_2.setText('PLATAFORMA_2')
        self.verticalLayout_2.addWidget(self.check_PLATAFORMA_2)
        self.check_PLATAFORMA_4_BBVA = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_PLATAFORMA_4_BBVA.setText('PLATAFORMA_4_BBVA')
        self.verticalLayout_2.addWidget(self.check_PLATAFORMA_4_BBVA)
        self.check_PLATAFORMA_5_BBVA = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_PLATAFORMA_5_BBVA.setText('PLATAFORMA_5_BBVA')
        self.verticalLayout_2.addWidget(self.check_PLATAFORMA_5_BBVA)
        self.check_PLATAFORMA_6 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_PLATAFORMA_6.setText('PLATAFORMA_6')
        self.verticalLayout_2.addWidget(self.check_PLATAFORMA_6)
        self.check_PLATAFORMA_7_BBVA = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_PLATAFORMA_7_BBVA.setText('PLATAFORMA_7_BBVA')
        self.verticalLayout_2.addWidget(self.check_PLATAFORMA_7_BBVA)
        self.check_PLATAFORMA_8_COLP = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_PLATAFORMA_8_COLP.setText('PLATAFORMA_8_COLP')
        self.verticalLayout_2.addWidget(self.check_PLATAFORMA_8_COLP)
        self.check_PLATAFORMA_9 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_PLATAFORMA_9.setText('PLATAFORMA_9')
        self.verticalLayout_2.addWidget(self.check_PLATAFORMA_9)
        self.check_RCB = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_RCB.setText('RCB')
        self.verticalLayout_2.addWidget(self.check_RCB)
        self.check_RCB_1_CITIBANK = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_RCB_1_CITIBANK.setText('RCB_1_CITIBANK')
        self.verticalLayout_2.addWidget(self.check_RCB_1_CITIBANK)
        self.check_RCB_2_CITIBANK = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_RCB_2_CITIBANK.setText('RCB_2_CITIBANK')
        self.verticalLayout_2.addWidget(self.check_RCB_2_CITIBANK)
        self.check_RCB_1_BAN_OCCIDENTE = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_RCB_1_BAN_OCCIDENTE.setText('RCB_1_BAN_OCCIDENTE')
        self.verticalLayout_2.addWidget(self.check_RCB_1_BAN_OCCIDENTE)
        self.check_RCB_1_BBVA = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_RCB_1_BBVA.setText('RCB_1_BBVA')
        self.verticalLayout_2.addWidget(self.check_RCB_1_BBVA)
        self.check_RCB_10 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_RCB_10.setText('RCB_10')
        self.verticalLayout_2.addWidget(self.check_RCB_10)
        self.check_RCB_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_RCB_2.setText('RCB_2')
        self.verticalLayout_2.addWidget(self.check_RCB_2)
        self.check_RCB_2_BAN_OCCIDENTE = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_RCB_2_BAN_OCCIDENTE.setText('RCB_2_BAN_OCCIDENTE')
        self.verticalLayout_2.addWidget(self.check_RCB_2_BAN_OCCIDENTE)
        self.check_RCB_3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_RCB_3.setText('RCB_3')
        self.verticalLayout_2.addWidget(self.check_RCB_3)
        self.check_RCB_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_RCB_4.setText('RCB_4')
        self.verticalLayout_2.addWidget(self.check_RCB_4)
        self.check_RCB_5 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_RCB_5.setText('RCB_5')
        self.verticalLayout_2.addWidget(self.check_RCB_5)
        self.check_RCB_6 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_RCB_6.setText('RCB_6')
        self.verticalLayout_2.addWidget(self.check_RCB_6)
        self.check_RCB_7 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_RCB_7.setText('RCB_7')
        self.verticalLayout_2.addWidget(self.check_RCB_7)
        self.check_RCB_8 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_RCB_8.setText('RCB_8')
        self.verticalLayout_2.addWidget(self.check_RCB_8)
        self.check_RCB_9 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_RCB_9.setText('RCB_9')
        self.verticalLayout_2.addWidget(self.check_RCB_9)
        self.check_REINTEGRA_1 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_REINTEGRA_1.setText('REINTEGRA_1')
        self.verticalLayout_2.addWidget(self.check_REINTEGRA_1)
        self.check_REINTEGRA_10_BANCOL = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_REINTEGRA_10_BANCOL.setText('REINTEGRA_10_BANCOL')
        self.verticalLayout_2.addWidget(self.check_REINTEGRA_10_BANCOL)
        self.check_REINTEGRA_11 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_REINTEGRA_11.setText('REINTEGRA_11')
        self.verticalLayout_2.addWidget(self.check_REINTEGRA_11)
        self.check_REINTEGRA_12 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_REINTEGRA_12.setText('REINTEGRA_12')
        self.verticalLayout_2.addWidget(self.check_REINTEGRA_12)
        self.check_REINTEGRA_13 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_REINTEGRA_13.setText('REINTEGRA_13')
        self.verticalLayout_2.addWidget(self.check_REINTEGRA_13)
        self.check_REINTEGRA_14 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_REINTEGRA_14.setText('REINTEGRA_14')
        self.verticalLayout_2.addWidget(self.check_REINTEGRA_14)
        self.check_REINTEGRA_15 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_REINTEGRA_15.setText('REINTEGRA_15')
        self.verticalLayout_2.addWidget(self.check_REINTEGRA_15)
        self.check_REINTEGRA_16 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_REINTEGRA_16.setText('REINTEGRA_16')
        self.verticalLayout_2.addWidget(self.check_REINTEGRA_16)
        self.check_REINTEGRA_17 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_REINTEGRA_17.setText('REINTEGRA_17')
        self.verticalLayout_2.addWidget(self.check_REINTEGRA_17)
        self.check_REINTEGRA_18 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_REINTEGRA_18.setText('REINTEGRA_18')
        self.verticalLayout_2.addWidget(self.check_REINTEGRA_18)
        self.check_REINTEGRA_19 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_REINTEGRA_19.setText('REINTEGRA_19')
        self.verticalLayout_2.addWidget(self.check_REINTEGRA_19)
        self.check_REINTEGRA_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_REINTEGRA_2.setText('REINTEGRA_2')
        self.verticalLayout_2.addWidget(self.check_REINTEGRA_2)
        self.check_REINTEGRA_20 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_REINTEGRA_20.setText('REINTEGRA_20')
        self.verticalLayout_2.addWidget(self.check_REINTEGRA_20)
        self.check_REINTEGRA_21 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_REINTEGRA_21.setText('REINTEGRA_21')
        self.verticalLayout_2.addWidget(self.check_REINTEGRA_21)
        self.check_REINTEGRA_21A = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_REINTEGRA_21A.setText('REINTEGRA_21A')
        self.verticalLayout_2.addWidget(self.check_REINTEGRA_21A)
        self.check_REINTEGRA_3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_REINTEGRA_3.setText('REINTEGRA_3')
        self.verticalLayout_2.addWidget(self.check_REINTEGRA_3)
        self.check_REINTEGRA_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_REINTEGRA_4.setText('REINTEGRA_4')
        self.verticalLayout_2.addWidget(self.check_REINTEGRA_4)
        self.check_REINTEGRA_5 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_REINTEGRA_5.setText('REINTEGRA_5')
        self.verticalLayout_2.addWidget(self.check_REINTEGRA_5)
        self.check_REINTEGRA_6 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_REINTEGRA_6.setText('REINTEGRA_6')
        self.verticalLayout_2.addWidget(self.check_REINTEGRA_6)
        self.check_REINTEGRA_7 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_REINTEGRA_7.setText('REINTEGRA_7')
        self.verticalLayout_2.addWidget(self.check_REINTEGRA_7)
        self.check_REINTEGRA_8_BANCO = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_REINTEGRA_8_BANCO.setText('REINTEGRA_8_BANCO')
        self.verticalLayout_2.addWidget(self.check_REINTEGRA_8_BANCO)
        self.check_REINTEGRA_9 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_portafolio)
        self.check_REINTEGRA_9.setText('REINTEGRA_9')
        self.verticalLayout_2.addWidget(self.check_REINTEGRA_9)


        
        
        #endregion

        #region tamaño lista
        #en esta región se crean los contadores que definen el tamaño de las listas cuando la cartera no incluye Reintegra. 
        #Se crearon diferentes recuadros anteriormente los cuales incluyen la mejor gestión (accion), dentro de estos recuadros se agregan los contadores para la gestion del mes (la mejor accion de la gestión en este mes). De manera que el tamaño de la lista se define como: "X registros que tengan mejor gestion 'tal' y que en este mes vengan de 'tal'"
        self.contacto_box=QtWidgets.QGroupBox(self.tamano_lista)
        self.contacto_box.setGeometry(QtCore.QRect(5,15,130,150))
        self.contacto_box.setTitle("Contacto")

        self.tamano_contacto_contacto = QtWidgets.QLabel(self.contacto_box)
        self.tamano_contacto_contacto.setGeometry(QtCore.QRect(5, 20, 61, 15))
        self.tamano_contacto_contacto.setText("Contacto")
        self.tamano_contacto_contacto_numero = QtWidgets.QSpinBox(self.contacto_box)
        self.tamano_contacto_contacto_numero.setGeometry(QtCore.QRect(72, 20, 49, 18))
        self.tamano_contacto_contacto_numero.setMinimum(1)
        self.tamano_contacto_contacto_numero.setMaximum(100000)
        
        self.no_contacto_box=QtWidgets.QGroupBox(self.tamano_lista)
        self.no_contacto_box.setGeometry(QtCore.QRect(140,15,130,150))
        self.no_contacto_box.setTitle("No contacto")

        self.tamano_nocontacto_contacto = QtWidgets.QLabel(self.no_contacto_box)
        self.tamano_nocontacto_contacto.setGeometry(QtCore.QRect(5, 20, 61, 15))
        self.tamano_nocontacto_contacto.setText("Contacto")
        self.tamano_nocontacto_contacto_numero = QtWidgets.QSpinBox(self.no_contacto_box)
        self.tamano_nocontacto_contacto_numero.setGeometry(QtCore.QRect(72, 20, 49, 18))
        self.tamano_nocontacto_contacto_numero.setMinimum(1)
        self.tamano_nocontacto_contacto_numero.setMaximum(100000)
        self.tamano_nocontacto_nocontacto = QtWidgets.QLabel(self.no_contacto_box)
        self.tamano_nocontacto_nocontacto.setGeometry(QtCore.QRect(5, 45, 61, 15))
        self.tamano_nocontacto_nocontacto.setText("No contacto")
        self.tamano_nocontacto_nocontacto_numero = QtWidgets.QSpinBox(self.no_contacto_box)
        self.tamano_nocontacto_nocontacto_numero.setGeometry(QtCore.QRect(72, 45, 49, 18))
        self.tamano_nocontacto_nocontacto_numero.setMinimum(1)
        self.tamano_nocontacto_nocontacto_numero.setMaximum(100000)

        self.ilocalizado_box=QtWidgets.QGroupBox(self.tamano_lista)
        self.ilocalizado_box.setGeometry(QtCore.QRect(275,15,130,150))
        self.ilocalizado_box.setTitle("Ilocalizado")

        self.tamano_ilocalizado_contacto = QtWidgets.QLabel(self.ilocalizado_box)
        self.tamano_ilocalizado_contacto.setGeometry(QtCore.QRect(5, 20, 61, 15))
        self.tamano_ilocalizado_contacto.setText("Contacto")
        self.tamano_ilocalizado_contacto_numero = QtWidgets.QSpinBox(self.ilocalizado_box)
        self.tamano_ilocalizado_contacto_numero.setGeometry(QtCore.QRect(72, 20, 49, 18))
        self.tamano_ilocalizado_contacto_numero.setMinimum(1)
        self.tamano_ilocalizado_contacto_numero.setMaximum(100000)
        self.tamano_ilocalizado_nocontacto = QtWidgets.QLabel(self.ilocalizado_box)
        self.tamano_ilocalizado_nocontacto.setGeometry(QtCore.QRect(5, 45, 61, 15))
        self.tamano_ilocalizado_nocontacto.setText("No Contacto")
        self.tamano_ilocalizado_nocontacto_numero = QtWidgets.QSpinBox(self.ilocalizado_box)
        self.tamano_ilocalizado_nocontacto_numero.setGeometry(QtCore.QRect(72, 45, 49, 18))
        self.tamano_ilocalizado_nocontacto_numero.setMinimum(1)
        self.tamano_ilocalizado_nocontacto_numero.setMaximum(100000)
        self.tamano_ilocalizado_ilocalizado = QtWidgets.QLabel(self.ilocalizado_box)
        self.tamano_ilocalizado_ilocalizado.setGeometry(QtCore.QRect(5, 70, 61, 15))
        self.tamano_ilocalizado_ilocalizado.setText("Ilocalizado")
        self.tamano_ilocalizado_ilocalizado_numero = QtWidgets.QSpinBox(self.ilocalizado_box)
        self.tamano_ilocalizado_ilocalizado_numero.setGeometry(QtCore.QRect(72, 70, 49, 18))
        self.tamano_ilocalizado_ilocalizado_numero.setMinimum(1)
        self.tamano_ilocalizado_ilocalizado_numero.setMaximum(100000)

        self.nogestion_box=QtWidgets.QGroupBox(self.tamano_lista)
        self.nogestion_box.setGeometry(QtCore.QRect(410,15,130,150))
        self.nogestion_box.setTitle("No Gestión")

        self.tamano_nogestion_contacto = QtWidgets.QLabel(self.nogestion_box)
        self.tamano_nogestion_contacto.setGeometry(QtCore.QRect(5, 20, 61, 15))
        self.tamano_nogestion_contacto.setText("Contacto")
        self.tamano_nogestion_contacto_numero = QtWidgets.QSpinBox(self.nogestion_box)
        self.tamano_nogestion_contacto_numero.setGeometry(QtCore.QRect(72, 20, 49, 18))
        self.tamano_nogestion_contacto_numero.setMinimum(1)
        self.tamano_nogestion_contacto_numero.setMaximum(100000)
        self.tamano_nogestion_nocontacto = QtWidgets.QLabel(self.nogestion_box)
        self.tamano_nogestion_nocontacto.setGeometry(QtCore.QRect(5, 45, 61, 15))
        self.tamano_nogestion_nocontacto.setText("No Contacto")
        self.tamano_nogestion_nocontacto_numero = QtWidgets.QSpinBox(self.nogestion_box)
        self.tamano_nogestion_nocontacto_numero.setGeometry(QtCore.QRect(72, 45, 49, 18))
        self.tamano_nogestion_nocontacto_numero.setMinimum(1)
        self.tamano_nogestion_nocontacto_numero.setMaximum(100000)
        self.tamano_nogestion_ilocalizado = QtWidgets.QLabel(self.nogestion_box)
        self.tamano_nogestion_ilocalizado.setGeometry(QtCore.QRect(5, 70, 61, 15))
        self.tamano_nogestion_ilocalizado.setText("Ilocalizado")
        self.tamano_nogestion_ilocalizado_numero = QtWidgets.QSpinBox(self.nogestion_box)
        self.tamano_nogestion_ilocalizado_numero.setGeometry(QtCore.QRect(72, 70, 49, 18))
        self.tamano_nogestion_ilocalizado_numero.setMinimum(1)
        self.tamano_nogestion_ilocalizado_numero.setMaximum(100000)
        self.tamano_nogestion_nogestion = QtWidgets.QLabel(self.nogestion_box)
        self.tamano_nogestion_nogestion.setGeometry(QtCore.QRect(5, 95, 61, 15))
        self.tamano_nogestion_nogestion.setText("No Gestión")
        self.tamano_nogestion_nogestion_numero = QtWidgets.QSpinBox(self.nogestion_box)
        self.tamano_nogestion_nogestion_numero.setGeometry(QtCore.QRect(72, 95, 49, 18))
        self.tamano_nogestion_nogestion_numero.setMinimum(1)
        self.tamano_nogestion_nogestion_numero.setMaximum(100000)

        #endregion

        #region recientes
        #en esta region se crean el check para definir si la lista debe incluir deudores que han sido recientemente llamados o no (incluyendo también el resultado de la gestión reciente)
        #la definición de estas categorías se da en la ruta de Modeler que genera las listas
        self.check_no_reciente = QtWidgets.QCheckBox(self.reciente)
        self.check_no_reciente.setGeometry(QtCore.QRect(10,20,120,15))
        self.check_no_reciente.setText("No Reciente")

        self.check_reciente_directo = QtWidgets.QCheckBox(self.reciente)
        self.check_reciente_directo.setGeometry(QtCore.QRect(10,45,120,15))
        self.check_reciente_directo.setText("Reciente Directo")
        
        self.check_reciente_indirecto = QtWidgets.QCheckBox(self.reciente)
        self.check_reciente_indirecto.setGeometry(QtCore.QRect(10,70,120,15))
        self.check_reciente_indirecto.setText("Reciente Indirecto")

        self.check_reciente_no_contacto = QtWidgets.QCheckBox(self.reciente)
        self.check_reciente_no_contacto.setGeometry(QtCore.QRect(10,95,125,15))
        self.check_reciente_no_contacto.setText("Reciente No Contacto")

        self.check_reciente_ilocalizado = QtWidgets.QCheckBox(self.reciente)
        self.check_reciente_ilocalizado.setGeometry(QtCore.QRect(10,120,120,15))
        self.check_reciente_ilocalizado.setText("Reciente Ilocalizado")

        #endregion

        #region avanzado
        #En esta región se crean parámetros adicionales para la lista

        #campo para definir si se incluyen o no deudores judicializados
        self.label_judicializado = QtWidgets.QLabel(self.box_avanzado)
        self.label_judicializado.setGeometry(QtCore.QRect(10, 20, 75, 16))
        self.label_judicializado.setText("Estado Judicial:")
        self.pick_judicializado = QtWidgets.QComboBox(self.box_avanzado)
        self.pick_judicializado.setGeometry(QtCore.QRect(110, 20, 201, 21))
        self.pick_judicializado.addItem("No Judicializado")
        self.pick_judicializado.addItem("Judicializado")
        self.pick_judicializado.addItem("Todo")
                    
        #campo para definir si se incluyen o no deudores judicializados
        self.label_garantias = QtWidgets.QLabel(self.box_avanzado)
        self.label_garantias.setGeometry(QtCore.QRect(10, 50, 71, 16))
        self.label_garantias.setText("Garantías:")
        self.pick_garantias = QtWidgets.QComboBox(self.box_avanzado)
        self.pick_garantias.setGeometry(QtCore.QRect(110, 50, 201, 21))
        self.pick_garantias.addItem("Sin garantías")
        self.pick_garantias.addItem("Con garantías")
        self.pick_garantias.addItem("Todo")

        #campo para determinar el número total máximo de llamadas que puede tener un deudor en la lista POR  AHORA NO SE USA.
        self.label_max_llamadas = QtWidgets.QLabel(self.box_avanzado)
        self.label_max_llamadas.setGeometry(QtCore.QRect(10, 80, 81, 16))
        self.label_max_llamadas.setText("Máx. Llamadas:")
        self.llamadas_numero = QtWidgets.QSpinBox(self.box_avanzado)
        self.llamadas_numero.setGeometry(QtCore.QRect(110, 80, 45, 21))
        self.llamadas_numero.setMaximum(500)

        #Check box para determinar si en la lista salen deudores asignados o no 
        self.label_asignacion = QtWidgets.QLabel(self.box_avanzado)
        self.label_asignacion.setGeometry(QtCore.QRect(350, 20, 55, 13))
        self.label_asignacion.setText("Asignación:")
        self.check_sin_asesor = QtWidgets.QCheckBox(self.box_avanzado)
        self.check_sin_asesor.setGeometry(QtCore.QRect(430, 20, 85, 17))
        self.check_sin_asesor.setChecked(True)
        self.check_sin_asesor.setText("Sin asesor")
        self.check_asignado_interno = QtWidgets.QCheckBox(self.box_avanzado)
        self.check_asignado_interno.setGeometry(QtCore.QRect(520, 20, 120, 17))
        self.check_asignado_interno.setText("Asignado Interno")
        self.check_asignado_c_cobranza = QtWidgets.QCheckBox(self.box_avanzado)
        self.check_asignado_c_cobranza.setGeometry(QtCore.QRect(630, 20, 125, 17))
        self.check_asignado_c_cobranza.setText("Asignado C.Cobranza")


        #chechbox para determinar si en la lista deben salir deudores con acuerdos (así sean incumplidos)
        self.label_acuerdos = QtWidgets.QLabel(self.box_avanzado)
        self.label_acuerdos.setGeometry(QtCore.QRect(350, 45, 47, 13))
        self.label_acuerdos.setText("Acuerdos:")
        self.check_sin_acuerdos = QtWidgets.QCheckBox(self.box_avanzado)
        self.check_sin_acuerdos.setGeometry(QtCore.QRect(430, 45, 85, 17))
        self.check_sin_acuerdos.setText("Sin acuerdos")
        self.check_sin_acuerdos.setChecked(True)
        self.check_acuerdos_incumplidos = QtWidgets.QCheckBox(self.box_avanzado)
        self.check_acuerdos_incumplidos.setGeometry(QtCore.QRect(520, 45, 120, 17))
        self.check_acuerdos_incumplidos.setText("Acrds Incumplidos")    
        self.check_acuerdos = QtWidgets.QCheckBox(self.box_avanzado)
        self.check_acuerdos.setGeometry(QtCore.QRect(630, 45, 85, 17))
        self.check_acuerdos.setText("Con Acuerdos")

        
        #checkbox para determinar si salen deudores que estén marcados como que hayan realizado un pago
        self.label_pagos = QtWidgets.QLabel(self.box_avanzado)
        self.label_pagos.setGeometry(QtCore.QRect(350, 70, 47, 13))
        self.label_pagos.setText("Pagos:")
        self.check_sin_pago = QtWidgets.QCheckBox(self.box_avanzado)
        self.check_sin_pago.setGeometry(QtCore.QRect(430, 70, 70, 17))
        self.check_sin_pago.setChecked(True)
        self.check_sin_pago.setText("Sin pago")
        self.check_pago = QtWidgets.QCheckBox(self.box_avanzado)
        self.check_pago.setGeometry(QtCore.QRect(520, 70, 70, 17))
        self.check_pago.setText("Pago")

        #checkbox para determinar si salen deudores que estén marcados como fallecidos
        self.label_fallecido = QtWidgets.QLabel(self.box_avanzado)
        self.label_fallecido.setGeometry(QtCore.QRect(350, 95, 47, 13))
        self.label_fallecido.setText("Fallecidos:")
        self.check_no_fallecido = QtWidgets.QCheckBox(self.box_avanzado)
        self.check_no_fallecido.setGeometry(QtCore.QRect(430, 95, 81, 17))
        self.check_no_fallecido.setChecked(True)
        self.check_no_fallecido.setText("No Fallecido")
        self.check_fallecido = QtWidgets.QCheckBox(self.box_avanzado)
        self.check_fallecido.setGeometry(QtCore.QRect(520, 95, 70, 17))
        self.check_fallecido.setText("Fallecido")  

        #checkbox para determinar si salen deudores que estén marcados como insolutos
        self.label_insoluto = QtWidgets.QLabel(self.box_avanzado)
        self.label_insoluto.setGeometry(QtCore.QRect(350, 120, 47, 13))
        self.label_insoluto.setText("Insolutos:")
        self.check_no_insoluto = QtWidgets.QCheckBox(self.box_avanzado)
        self.check_no_insoluto.setGeometry(QtCore.QRect(430, 120, 81, 17))
        self.check_no_insoluto.setChecked(True)
        self.check_no_insoluto.setText("No Insoluto")
        self.check_insoluto = QtWidgets.QCheckBox(self.box_avanzado)
        self.check_insoluto.setGeometry(QtCore.QRect(520, 120, 81, 17))
        self.check_insoluto.setText("Insoluto")

        
        #checkbox para determinar si salen deudores que estén marcados como renuentes
        self.label_renuentes = QtWidgets.QLabel(self.box_avanzado)
        self.label_renuentes.setGeometry(QtCore.QRect(350, 145, 61, 16))
        self.label_renuentes.setText("Renuentes:")
        self.check_no_renuente = QtWidgets.QCheckBox(self.box_avanzado)
        self.check_no_renuente.setGeometry(QtCore.QRect(430, 145, 81, 17))
        self.check_no_renuente.setChecked(True)
        self.check_no_renuente.setText("No Renuente")
        self.check_renuente = QtWidgets.QCheckBox(self.box_avanzado)
        self.check_renuente.setGeometry(QtCore.QRect(520, 145, 81, 17))
        self.check_renuente.setText("Renuente") 

        #checkbox para determinar si salen deudores que estén marcados CON TELEFONO O SIN TELEFONO
        self.label_telefonos = QtWidgets.QLabel(self.box_avanzado)
        self.label_telefonos.setGeometry(QtCore.QRect(350, 170, 61, 16))
        self.label_telefonos.setText("Telefonos:")
        self.check_no_telefono = QtWidgets.QCheckBox(self.box_avanzado)
        self.check_no_telefono.setGeometry(QtCore.QRect(520, 170, 81, 17))
        self.check_no_telefono.setText("No Telefono")
        self.check_telefono = QtWidgets.QCheckBox(self.box_avanzado)
        self.check_telefono.setGeometry(QtCore.QRect(430, 170, 81, 17))
        self.check_telefono.setText("Telefono") 
        self.check_telefono.setChecked(True)

        #checkbox para determinar que la lista tenga deudores solamente de ciertos montos de UPB_Total
        self.label_montos = QtWidgets.QLabel(self.box_avanzado)
        self.label_montos.setGeometry(QtCore.QRect(10, 110, 71, 16))
        self.label_montos.setText("Montos:")
        self.check_montos_menores_500k = QtWidgets.QCheckBox(self.box_avanzado)
        self.check_montos_menores_500k.setGeometry(QtCore.QRect(10, 130, 101, 25))
        self.check_montos_menores_500k.setChecked(False)
        self.check_montos_menores_500k.setText("Menores a 500k")
        self.check_montos_menores_1M = QtWidgets.QCheckBox(self.box_avanzado)
        self.check_montos_menores_1M.setGeometry(QtCore.QRect(130, 130, 100, 25))
        self.check_montos_menores_1M.setChecked(True)
        self.check_montos_menores_1M.setText("Entre 500k y 1M")
        self.check_montos_1a3M = QtWidgets.QCheckBox(self.box_avanzado)
        self.check_montos_1a3M.setGeometry(QtCore.QRect(240, 130, 100, 25))
        self.check_montos_1a3M.setChecked(True)
        self.check_montos_1a3M.setText("Entre 1M y 3M")
        self.check_montos_3a7M = QtWidgets.QCheckBox(self.box_avanzado)
        self.check_montos_3a7M.setGeometry(QtCore.QRect(10, 160, 100, 25))
        self.check_montos_3a7M.setChecked(True)
        self.check_montos_3a7M.setText("Entre 3M y 7M")
        self.check_montos_mayores_7M = QtWidgets.QCheckBox(self.box_avanzado)
        self.check_montos_mayores_7M.setGeometry(QtCore.QRect(130, 160, 100, 25))
        self.check_montos_mayores_7M.setChecked(True)
        self.check_montos_mayores_7M.setTristate(False)
        self.check_montos_mayores_7M.setText("Mayores a 7M")
        #endregion


        #texto resumen
        #El texto resumen se inicializa en blanco para que una función pueda determinar todos los parámetros y concatenarlos
        self.label_resumen=QtWidgets.QLabel(self.resumen)
        self.label_resumen.setText("")
        self.label_resumen.move(10,18)
        self.label_resumen.adjustSize()

    #region funciones de interacción    
    # Región para declarar las funciones que se pueden realizar dentro de la aplicación

    #La primera función es "revisar_lista" la cual lee todos los campos y genera una lista de parámetros y un resumen de la solicitud
    # primero se inicializan todos los parámetros. Los que vienen de chechbox son listas vacías que se llenarán posteriormente, los campos numéricos recojen de una vez el valor incluido en el campo declarado      
    def revisar_lista(self):
        nombre=[self.nombre_lista.text()]
        tipo_gestion=[]
        portafolio=[]
        judicializado=[]
        garantias=[]
        asignacion=[]
        tamano=[self.tamano_contacto_contacto_numero.text(),
                self.tamano_nocontacto_contacto_numero.text(),
                self.tamano_nocontacto_nocontacto_numero.text(),
                self.tamano_ilocalizado_contacto_numero.text(),
                self.tamano_ilocalizado_nocontacto_numero.text(),
                self.tamano_ilocalizado_ilocalizado_numero.text(),
                self.tamano_nogestion_contacto_numero.text(),
                self.tamano_nogestion_nocontacto_numero.text(),
                self.tamano_nogestion_ilocalizado_numero.text(),
                self.tamano_nogestion_nogestion_numero.text()]
        max_llamadas=self.llamadas_numero.text()
        acuerdos=[]
        montos=[]
        pagos=[]
        fallecidos=[]
        insolutos=[]
        renuentes=[]
        recientes=[]
        telefonos = []
        tamano_segmentos = [self.tamano_seg_1_numero.text(),self.tamano_seg_2_numero.text(),self.tamano_seg_3_numero.text()]

        #   para todos los checkbox la lista se llena de la siguiente manera:
        #   se define un diccionario en donde las llaves son el checkbox de cada categoría y el valor corresponde a un campo String que contiene el equivalente a lo que representa la llave. Es decir, "self.check_especial" representa si se quiere o no el tipo_gestion "ESPECIAL".
        #Luego se realiza un loop a través de todas las llaves del diccionario creado, se revisa su estado (check o no check), si la llave está en estado check, es decir ".isChecked() == True", entonces el valor de dicha llave se agrega a la lista correspondiente. 

        
        tipo_gestion_l={self.check_especial: "ESPECIAL",
                        self.check_masivo: "MASIVO",
                        self.check_fng: "FNG"}
        for tipo in tipo_gestion_l:
            if tipo.isChecked()==True:
                tipo_gestion.append(tipo_gestion_l[tipo])

        portafolios_l={self.check_NEW_CREDIT_1: 'NEW CREDIT 1',
                        self.check_NEW_CREDIT_11_BBVA: 'NEW CREDIT 11 BBVA',
                        self.check_NEW_CREDIT_12_BBVA: 'NEW CREDIT 12 BBVA',
                        self.check_NEW_CREDIT_6: 'NEW CREDIT 6',
                        self.check_NEW_CREDIT_7: 'NEW CREDIT 7',
                        self.check_NEWCREDIT_10: 'NEWCREDIT 10',
                        self.check_NEWCREDIT_4: 'NEWCREDIT 4',
                        self.check_PLATAFORMA_1: 'PLATAFORMA 1',
                        self.check_PLATAFORMA_2: 'PLATAFORMA 2',
                        self.check_PLATAFORMA_4_BBVA: 'PLATAFORMA 4 - BBVA',
                        self.check_PLATAFORMA_5_BBVA: 'PLATAFORMA 5 - BBVA',
                        self.check_PLATAFORMA_6: 'PLATAFORMA 6',
                        self.check_PLATAFORMA_7_BBVA: 'PLATAFORMA 7 BBVA',
                        self.check_PLATAFORMA_8_COLP: 'PLATAFORMA 8 COLP',
                        self.check_PLATAFORMA_9: 'PLATAFORMA 9',
                        self.check_RCB: 'RCB',
                        self.check_RCB_1_CITIBANK: 'RCB  1 - CITIBANK',
                        self.check_RCB_2_CITIBANK: 'RCB  2 - CITIBANK',
                        self.check_RCB_1_BAN_OCCIDENTE: 'RCB 1 - BAN OCCIDENTE',
                        self.check_RCB_1_BBVA: 'RCB 1 - BBVA',
                        self.check_RCB_10: 'RCB 10',
                        self.check_RCB_2: 'RCB 2',
                        self.check_RCB_2_BAN_OCCIDENTE: 'RCB 2 - BAN OCCIDENTE',
                        self.check_RCB_3: 'RCB 3',
                        self.check_RCB_4: 'RCB 4',
                        self.check_RCB_5: 'RCB 5',
                        self.check_RCB_6: 'RCB 6',
                        self.check_RCB_7: 'RCB 7',
                        self.check_RCB_8: 'RCB 8',
                        self.check_RCB_9: 'RCB 9',
                        self.check_REINTEGRA_1: 'REINTEGRA 1',
                        self.check_REINTEGRA_10_BANCOL: 'REINTEGRA 10 BANCOL',
                        self.check_REINTEGRA_11: 'REINTEGRA 11',
                        self.check_REINTEGRA_12: 'REINTEGRA 12',
                        self.check_REINTEGRA_13: 'REINTEGRA 13',
                        self.check_REINTEGRA_14: 'REINTEGRA 14',
                        self.check_REINTEGRA_15: 'REINTEGRA 15',
                        self.check_REINTEGRA_16: 'REINTEGRA 16',
                        self.check_REINTEGRA_17: 'REINTEGRA 17',
                        self.check_REINTEGRA_18: 'REINTEGRA 18',
                        self.check_REINTEGRA_19: 'REINTEGRA 19',
                        self.check_REINTEGRA_2: 'REINTEGRA 2',
                        self.check_REINTEGRA_20: 'REINTEGRA 20',
                        self.check_REINTEGRA_21: 'REINTEGRA 21',
                        self.check_REINTEGRA_21A: 'REINTEGRA 21A',
                        self.check_REINTEGRA_3: 'REINTEGRA 3',
                        self.check_REINTEGRA_4: 'REINTEGRA 4',
                        self.check_REINTEGRA_5: 'REINTEGRA 5',
                        self.check_REINTEGRA_6: 'REINTEGRA 6',
                        self.check_REINTEGRA_7: 'REINTEGRA 7',
                        self.check_REINTEGRA_8_BANCO: 'REINTEGRA 8 BANCO',
                        self.check_REINTEGRA_9: 'REINTEGRA 9'}
        for porta in portafolios_l:
            if porta.isChecked()==True:
                portafolio.append(portafolios_l[porta])

        asesor_cobrador_l={self.check_asignado_c_cobranza: "ASIGNADO_C_COBRANZA",
                            self.check_asignado_interno: "ASIGNADO_INTERNO",
                            self.check_sin_asesor: "SIN ASESOR"}
        for asesor in asesor_cobrador_l:
            if asesor.isChecked()==True:
                asignacion.append(asesor_cobrador_l[asesor])

        if self.pick_judicializado.currentText()=="Judicializado":
            judicializado.append("JUDICIALIZADO")
        elif self.pick_judicializado.currentText()=="No Judicializado":
            judicializado.append("NO JUDICIALIZADO")
        else:
            judicializado.append("JUDICIALIZADO")
            judicializado.append("NO JUDICIALIZADO")

        if self.pick_garantias.currentText()=="Sin garantías":
            garantias.append("SIN GARANTIAS")
        elif self.pick_garantias.currentText()=="Con garantías":
            garantias.append("GARANTIAS")
        else:
            garantias.append("SIN GARANTIAS")
            garantias.append("GARANTIAS")

        montos_l={self.check_montos_menores_500k:"Menor a 500k", 
                    self.check_montos_menores_1M:"Entre 500k y 1M",
                    self.check_montos_1a3M:"Entre 1M y 3M",
                    self.check_montos_3a7M: "Entre 3M y 7M",
                    self.check_montos_mayores_7M: "Mayor a 7M"}
        for monto in montos_l:
            if monto.isChecked()==True:
                montos.append(montos_l[monto])
        
        acuerdos_l={self.check_sin_acuerdos:"SIN ACUERDOS",self.check_acuerdos_incumplidos: "ACUERDO_INCUMPLIDO",self.check_acuerdos:"ACUERDO"}
        for acuerdo in acuerdos_l:
            if acuerdo.isChecked()==True:
                acuerdos.append(acuerdos_l[acuerdo])

        pagos_l={self.check_sin_pago:"SIN PAGO",self.check_pago:"PAGO"}
        for pago in pagos_l:
            if pago.isChecked()==True:
                pagos.append(pagos_l[pago])

        fallecidos_l={self.check_no_fallecido:"NO FALLECIDO",self.check_fallecido:"FALLECIDO"}
        for fallecido in fallecidos_l:
            if fallecido.isChecked()==True:
                fallecidos.append(fallecidos_l[fallecido])

        insolutos_l={self.check_no_insoluto:"NO INSOLUTO",self.check_insoluto:"INSOLUTO"}
        for insoluto in insolutos_l:
            if insoluto.isChecked()==True:
                insolutos.append(insolutos_l[insoluto])

        renuentes_l={self.check_no_renuente:"NO RENUENTE",self.check_renuente:"RENUENTE"}
        for renuente in renuentes_l:
            if renuente.isChecked()==True:
                renuentes.append(renuentes_l[renuente])

        telefonos_l = {self.check_telefono: "CON TELEFONO", self.check_no_telefono: "SIN TELEFONO"}
        for telefono in telefonos_l:
            if telefono.isChecked()== True:
                telefonos.append(telefonos_l[telefono])

        recientes_l={self.check_no_reciente:"NO_RECIENTE",
                     self.check_reciente_directo:"RECIENTE_DIRECTO",
                     self.check_reciente_indirecto:"RECIENTE_INDIRECTO",
                     self.check_reciente_no_contacto:"RECIENTE_NO CONTACTO",
                     self.check_reciente_ilocalizado:"RECIENTE_ILOCALIZADO"}
        for reciente in recientes_l:
            if reciente.isChecked()==True:
                recientes.append(recientes_l[reciente])

        #Una vez todas las listas que conforman los parámetros están completas, se crea una lista llamada "parametros" la cual incluye todas las listas anteriores
        self.parametros=[nombre,tipo_gestion,portafolio,asignacion,
                         tamano[0],tamano[1],tamano[2],tamano[3],tamano[4],tamano[5],
                         tamano[6],tamano[7],tamano[8],tamano[9],
                         judicializado,garantias,max_llamadas,acuerdos,
                         montos,pagos,fallecidos,insolutos,renuentes,recientes,telefonos,tamano_segmentos[0],
                         tamano_segmentos[1],tamano_segmentos[2]]    
        
        #se crea una variable String llamada "resumen" la cual concatena todos los elementos de texto presentes en la lista de parametros
        resumen=str("Nombre:"+str(nombre[0])+"\nTipo Gestion:"+str([a for a in tipo_gestion])+"\nPortafolio:"+str([a for a in portafolio])+"\nAsignación:"+str([a for a in asignacion])
            +"\nTamaño:"+str([a for a in tamano])+"\nRecientes:"+str([a for a in recientes])+"\nEstado Judicial:"+str([a for a in judicializado])+"\nGarantías:"+str([a for a in garantias])+"\nMáx.Llamadas:"+str(max_llamadas[0])
            +"\nAcuerdos:"+str([a for a in acuerdos])+"\nMontos:"+str([a for a in montos])+"\nPagos:"+str([a for a in pagos])+"\nFallecidos:"+str([a for a in fallecidos])+"\nInsolutos:"+str([a for a in insolutos])
            +"\nRenuentes:"+str([a for a in renuentes]) + "\nTelefonos: " + str([a for a in telefonos])+"\nTamaño_seg_Rein:"+str([a for a in tamano_segmentos]))
        
        #posteriormente se remplazan algunos caracteres en la variable de resumen y declara que este resumen será el que se presente en la variable self.resumen declarada anteriormente
        resumen=resumen.replace("[","").replace("'","").replace("]"," ").replace("_"," ")
        self.label_resumen.setText(resumen)
        self.update(self.label_resumen)

    #la función update ajusta automáticamente los campos label
    def update(self,x):
        x.adjustSize()
    
    #la función solicitar_l toma la lista parámetros generada en la función revisar y genera el archivo con la nueva solicitud
    def solicitar_l(self):
        self.lista.setText("Se ha creado la soliciud.")
        self.update(self.lista)
        lista=self.ruta.text()+"/"+self.nombre_lista.text()+".txt"
        with open(lista, mode="w") as outfile:
            for parametro in self.parametros:
                outfile.write("%s \n" % parametro)

    
    #la función nueva lista hace un reset de todos los campos creados a su valor predeterminado para poder hacer una nueva solicitud
    def nueva_l(self):
        self.lista.setText("No se ha solicitado ninguna lista.")
        self.update(self.lista)
        self.nombre_lista.setText("")
        self.ruta.setText(self.ruta_inicial)
        self.label_resumen.setText("")
        self.llamadas_numero.setValue(0)
        self.tamano_contacto_contacto_numero.setValue(1)
        self.tamano_nocontacto_contacto_numero.setValue(1)
        self.tamano_nocontacto_nocontacto_numero.setValue(1)
        self.tamano_ilocalizado_contacto_numero.setValue(1)
        self.tamano_ilocalizado_nocontacto_numero.setValue(1)
        self.tamano_ilocalizado_ilocalizado_numero.setValue(1)
        self.tamano_nogestion_contacto_numero.setValue(1)
        self.tamano_nogestion_nocontacto_numero.setValue(1)
        self.tamano_nogestion_ilocalizado_numero.setValue(1)
        self.tamano_nogestion_nogestion_numero.setValue(1)
        self.tamano_seg_1_numero.setValue(1)
        self.tamano_seg_2_numero.setValue(1)
        self.tamano_seg_3_numero.setValue(1)
        
        reset_check=[self.check_especial,self.check_masivo,self.check_fng,
                self.check_sin_asesor,self.check_asignado_c_cobranza,self.check_asignado_interno,self.check_no_reciente,self.check_reciente_directo,self.check_reciente_indirecto,self.check_reciente_no_contacto,self.check_reciente_ilocalizado,
                self.check_NEW_CREDIT_1,self.check_NEW_CREDIT_11_BBVA,self.check_NEW_CREDIT_12_BBVA,
                self.check_NEW_CREDIT_6,self.check_NEW_CREDIT_7,self.check_NEWCREDIT_10,self.check_NEWCREDIT_4,self.check_PLATAFORMA_1,
                self.check_PLATAFORMA_2,self.check_PLATAFORMA_4_BBVA,self.check_PLATAFORMA_5_BBVA,self.check_PLATAFORMA_6,self.check_PLATAFORMA_7_BBVA,
                self.check_PLATAFORMA_8_COLP,self.check_PLATAFORMA_9,self.check_RCB,self.check_RCB_1_CITIBANK,self.check_RCB_2_CITIBANK,self.check_RCB_1_BAN_OCCIDENTE,
                self.check_RCB_1_BBVA,self.check_RCB_10,self.check_RCB_2,self.check_RCB_2_BAN_OCCIDENTE,self.check_RCB_3,self.check_RCB_4,
                self.check_RCB_5,self.check_RCB_6,self.check_RCB_7,self.check_RCB_8,self.check_RCB_9,self.check_REINTEGRA_1,
                self.check_REINTEGRA_10_BANCOL,self.check_REINTEGRA_11,self.check_REINTEGRA_12,self.check_REINTEGRA_13,self.check_REINTEGRA_14,
                self.check_REINTEGRA_15,self.check_REINTEGRA_16,self.check_REINTEGRA_17,self.check_REINTEGRA_18,self.check_REINTEGRA_19,self.check_REINTEGRA_2,
                self.check_REINTEGRA_20,self.check_REINTEGRA_21,self.check_REINTEGRA_21A,self.check_REINTEGRA_3,self.check_REINTEGRA_4,self.check_REINTEGRA_5,self.check_REINTEGRA_6,self.check_REINTEGRA_7,
                self.check_REINTEGRA_8_BANCO,self.check_REINTEGRA_9]
        for check in reset_check:
            check.setChecked(False)

    #endregion
    
#se crea una función que llama a la clase anteriormente generada
def crear_listas():
    app=QApplication(sys.argv)
    win=creacion_listas()
    win.show()
    sys.exit(app.exec_())

#se llama la función para abrir la aplicación
crear_listas()
    