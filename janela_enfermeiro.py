from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaEnfermeiro(object):
    def setupUi(self, TelaEnfermeiro):
        TelaEnfermeiro.setObjectName("TelaEnfermeiro")
        TelaEnfermeiro.setEnabled(True)
        TelaEnfermeiro.resize(570, 500)
        TelaEnfermeiro.setMinimumSize(QtCore.QSize(570, 500))
        TelaEnfermeiro.setMaximumSize(QtCore.QSize(570, 500))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        TelaEnfermeiro.setFont(font)
        TelaEnfermeiro.setStyleSheet("QMainWindow {\n    background-color:#F1F1F1;\n}")
        TelaEnfermeiro.setIconSize(QtCore.QSize(24, 24))

        # central widget
        self.centralwidget = QtWidgets.QWidget(TelaEnfermeiro)
        self.centralwidget.setObjectName("centralwidget")

        # title
        self.Label_titulo = QtWidgets.QLabel(self.centralwidget)
        self.Label_titulo.setGeometry(QtCore.QRect(120, 30, 331, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.Label_titulo.setFont(font)
        self.Label_titulo.setObjectName("Label_titulo")

        # name
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setGeometry(QtCore.QRect(40, 110, 311, 20))
        self.lineEdit_nome.setStyleSheet("color: #333;\nbackground: transparent; \nborder-radius: 4px; \nborder: 1px solid #AAAAAA;  \npadding-left: 4px;")
        self.lineEdit_nome.setText("")
        self.lineEdit_nome.setPlaceholderText("Digite o nome")
        self.lineEdit_nome.setObjectName("lineEdit_nome")

        # coren
        self.lineEdit_coren = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_coren.setGeometry(QtCore.QRect(380, 110, 151, 20))
        self.lineEdit_coren.setStyleSheet("color:#333;\nbackground: transparent; \nborder-radius: 4px; \nborder: 1px solid #AAAAAA;  \npadding-left: 4px;")
        self.lineEdit_coren.setText("")
        self.lineEdit_coren.setPlaceholderText("Digite o Coren")
        self.lineEdit_coren.setObjectName("lineEdit_coren")

        # --- ComboStatus (corrigido) ---
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(40, 150, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_status.setFont(font)
        self.label_status.setObjectName("label_status")

        # cria a combo com parent (centralwidget)
        self.combo_status = QtWidgets.QComboBox(self.centralwidget)
        self.combo_status.setGeometry(QtCore.QRect(40, 170, 151, 22))
        self.combo_status.addItems(["Ativo", "Inativo"])

        # força usar QListView como view para o popup (mais controle no Windows)
        view = QtWidgets.QListView(self.combo_status)
        self.combo_status.setView(view)

        # stylesheet só para o campo fechado (opcional)
        self.combo_status.setStyleSheet("""
            QComboBox {
                background: transparent;
                border: 1px solid #AAAAAA;
                border-radius: 4px;
                padding-left: 6px;
                color: #333;
            }
        """)

        # stylesheet e atributos para o popup (QListView)
        view.setStyleSheet("""
            QListView {
                background-color: #FFFFFF;
                color: #000000;
                outline: 0;
            }
            QListView::item {
                background-color: #FFFFFF;
                color: #000000;
            }
            QListView::item:selected {
                background-color: #5599ff;
                color: #ffffff;
            }
        """)
        view.setAttribute(QtCore.Qt.WA_StyledBackground, True)

        # garantir paleta (fallback caso o QSS seja ignorado)
        pal = view.palette()
        pal.setColor(QtGui.QPalette.Base, QtGui.QColor("#FFFFFF"))
        pal.setColor(QtGui.QPalette.Text, QtGui.QColor("#000000"))
        pal.setColor(QtGui.QPalette.Highlight, QtGui.QColor("#5599ff"))
        pal.setColor(QtGui.QPalette.HighlightedText, QtGui.QColor("#FFFFFF"))
        view.setPalette(pal)
        # --- fim combo ---


        # buttons
        self.pushButton_cadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cadastrar.setGeometry(QtCore.QRect(450, 270, 75, 23))
        self.pushButton_cadastrar.setStyleSheet("QPushButton {\nbackground: #504B4B;\ncolor: #FFFFFF;\nborder-radius: 4px;\npadding: 5px;\n}\nQPushButton:hover {\n    background-color: #5599ff;\n}\nQPushButton:pressed {\n    background-color: #2e5ea2;\n}")
        self.pushButton_cadastrar.setObjectName("pushButton_cadastrar")

        self.pushButton_visu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_visu.setGeometry(QtCore.QRect(450, 300, 75, 23))
        self.pushButton_visu.setStyleSheet("QPushButton {\nbackground: #504B4B;\ncolor: #FFFFFF;\nborder-radius: 4px;\npadding: 5px;\n}\nQPushButton:hover {\n    background-color: #5599ff;\n}\nQPushButton:pressed {\n    background-color: #2e5ea2;\n}")
        self.pushButton_visu.setObjectName("pushButton_visu")

        self.pushButton_editar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_editar.setGeometry(QtCore.QRect(450, 330, 75, 23))
        self.pushButton_editar.setStyleSheet("QPushButton {\nbackground: #504B4B;\ncolor: #FFFFFF;\nborder-radius: 4px;\npadding: 5px;\n}\nQPushButton:hover {\n    background-color: #5599ff;\n}\nQPushButton:pressed {\n    background-color: #2e5ea2;\n}")
        self.pushButton_editar.setObjectName("pushButton_editar")

        self.pushButton_excluir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_excluir.setGeometry(QtCore.QRect(450, 360, 75, 23))
        self.pushButton_excluir.setStyleSheet("QPushButton {\nbackground: #504B4B;\ncolor: #FFFFFF;\nborder-radius: 4px;\npadding: 5px;\n}\nQPushButton:hover {\n    background-color: #5599ff;\n}\nQPushButton:pressed {\n    background-color: #2e5ea2;\n}")
        self.pushButton_excluir.setObjectName("pushButton_excluir")

        # labels
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setGeometry(QtCore.QRect(40, 90, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_nome.setFont(font)
        self.label_nome.setObjectName("label_nome")

        self.label_coren = QtWidgets.QLabel(self.centralwidget)
        self.label_coren.setGeometry(QtCore.QRect(380, 90, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_coren.setFont(font)
        self.label_coren.setObjectName("label_coren")



        # id
        self.lineEdit_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_id.setEnabled(False)
        self.lineEdit_id.setGeometry(QtCore.QRect(40, 230, 71, 20))
        self.lineEdit_id.setStyleSheet("color:#333;\nbackground: transparent; \nborder-radius: 4px; \nborder: 1px solid #AAAAAA;  \npadding-left: 4px;")
        self.lineEdit_id.setText("")
        self.lineEdit_id.setPlaceholderText("Digite o ID")
        self.lineEdit_id.setObjectName("lineEdit_id")

        self.label_id_enfer = QtWidgets.QLabel(self.centralwidget)
        self.label_id_enfer.setGeometry(QtCore.QRect(40, 210, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_id_enfer.setFont(font)
        self.label_id_enfer.setObjectName("label_id_enfer")

        # table
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 270, 391, 181))
        self.tableWidget.setStyleSheet("""
QTableWidget {
    background-color: #F5F5F5;
    alternate-background-color: #E0FFFF;
}
QHeaderView::section {
    background-color: #504B4B;
    color: white;
    font-weight: bold;
}
""")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        
        self.tableWidget.horizontalHeader().setDefaultSectionSize(66)
        self.tableWidget.setColumnWidth(0, 10)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 120)
        self.tableWidget.setColumnWidth(3, 80)
        
        # set central widget and statusbar
        TelaEnfermeiro.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TelaEnfermeiro)
        self.statusbar.setObjectName("statusbar")
        TelaEnfermeiro.setStatusBar(self.statusbar)
        TelaEnfermeiro.setWindowIcon(QtGui.QIcon("hospital.png"))

        self.retranslateUi(TelaEnfermeiro)
        QtCore.QMetaObject.connectSlotsByName(TelaEnfermeiro)

    def retranslateUi(self, TelaEnfermeiro):
        _translate = QtCore.QCoreApplication.translate
        TelaEnfermeiro.setWindowTitle(_translate("TelaEnfermeiro", "Sistema Hospitalar"))
        self.Label_titulo.setText(_translate("TelaEnfermeiro", "Informações do Enfermeiro"))
        self.pushButton_cadastrar.setText(_translate("TelaEnfermeiro", "Cadastrar"))
        self.pushButton_visu.setText(_translate("TelaEnfermeiro", "Visualizar"))
        self.pushButton_editar.setText(_translate("TelaEnfermeiro", "Editar"))
        self.pushButton_excluir.setText(_translate("TelaEnfermeiro", "Excluir"))
        self.label_nome.setText(_translate("TelaEnfermeiro", "Nome:"))
        self.label_coren.setText(_translate("TelaEnfermeiro", "COREN:"))
        self.label_status.setText(_translate("TelaEnfermeiro", "Status"))
        self.label_id_enfer.setText(_translate("TelaEnfermeiro", "ID:"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("TelaEnfermeiro", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("TelaEnfermeiro", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("TelaEnfermeiro", "Coren"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("TelaEnfermeiro", "Status"))
        item = self.tableWidget.horizontalHeaderItem(4)
       

if __name__ == "__main__":
    import sys
    # Opcional: forçar estilo Fusion para testar consistência em Windows
    # QtWidgets.QApplication.setStyle("Fusion")
    app = QtWidgets.QApplication(sys.argv)
    TelaEnfermeiro = QtWidgets.QMainWindow()
    ui = Ui_TelaEnfermeiro()
    ui.setupUi(TelaEnfermeiro)
    TelaEnfermeiro.show()
    sys.exit(app.exec_())
