# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TelaPaciente(object):
    def setupUi(self, TelaPaciente):
        TelaPaciente.setObjectName("TelaPaciente")
        TelaPaciente.setEnabled(True)
        TelaPaciente.resize(570, 500)
        TelaPaciente.setMinimumSize(QtCore.QSize(570, 500))
        TelaPaciente.setMaximumSize(QtCore.QSize(570, 500))

        # ÍCONE DA JANELA
        TelaPaciente.setWindowIcon(QtGui.QIcon("icon.png"))
        TelaPaciente.setIconSize(QtCore.QSize(24, 24))

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        TelaPaciente.setFont(font)

        TelaPaciente.setStyleSheet(
            "QMainWindow {\n"
            "    background-color:#F1F1F1;\n"
            "}"
        )

        self.centralwidget = QtWidgets.QWidget(TelaPaciente)
        self.centralwidget.setObjectName("centralwidget")

        # ------------------- Título -------------------
        self.Label_titulo = QtWidgets.QLabel(self.centralwidget)
        self.Label_titulo.setGeometry(QtCore.QRect(140, 30, 301, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.Label_titulo.setFont(font)
        self.Label_titulo.setObjectName("Label_titulo")

        # ------------------- Campos -------------------
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setGeometry(QtCore.QRect(40, 110, 311, 20))
        self.lineEdit_nome.setStyleSheet(
            "color: #333;\n"
            "background: transparent; \n"
            "border-radius: 4px;\n"
            "border: 1px solid #AAAAAA;\n"
            "padding-left: 4px;"
        )
        self.lineEdit_nome.setPlaceholderText("Digite o nome")
        self.lineEdit_nome.setCursorPosition(0)
        self.lineEdit_nome.setObjectName("lineEdit_nome")

        self.lineEdit_cpf = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cpf.setGeometry(QtCore.QRect(380, 110, 151, 20))
        self.lineEdit_cpf.setStyleSheet(
            "color:#333;\n"
            "background: transparent;\n"
            "border-radius: 4px;\n"
            "border: 1px solid #AAAAAA;\n"
            "padding-left: 4px;"
        )
        self.lineEdit_cpf.setInputMask("000.000.000-00;_")
        self.lineEdit_cpf.setObjectName("lineEdit_cpf")

        self.lineEdit_data = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_data.setGeometry(QtCore.QRect(40, 170, 151, 21))
        self.lineEdit_data.setStyleSheet(
            "color:#333;\n"
            "background: transparent;\n"
            "border-radius: 4px;\n"
            "border: 1px solid #AAAAAA;\n"
            "padding-left: 4px;"
        )
        self.lineEdit_data.setInputMask("00/00/0000;_")
        self.lineEdit_data.setObjectName("lineEdit_data")

        self.lineEdit_sexo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sexo.setGeometry(QtCore.QRect(210, 170, 41, 20))
        self.lineEdit_sexo.setStyleSheet(
            "color:#333;\n"
            "background: transparent;\n"
            "border-radius: 4px;\n"
            "border: 1px solid #AAAAAA;\n"
            "padding-left: 4px;"
        )
        self.lineEdit_sexo.setPlaceholderText("sexo")
        self.lineEdit_sexo.setObjectName("lineEdit_sexo")

        self.lineEdit_telefone = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_telefone.setGeometry(QtCore.QRect(260, 170, 121, 20))
        self.lineEdit_telefone.setStyleSheet(
            "color:#333;\n"
            "background: transparent;\n"
            "border-radius: 4px;\n"
            "border: 1px solid #AAAAAA;\n"
            "padding-left: 4px;"
        )
        self.lineEdit_telefone.setInputMask("(00) 0 0000-0000;_")
        self.lineEdit_telefone.setObjectName("lineEdit_telefone")

        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(390, 170, 141, 20))
        self.lineEdit_email.setStyleSheet(
            "color:#333;\n"
            "background: transparent;\n"
            "border-radius: 4px;\n"
            "border: 1px solid #AAAAAA;\n"
            "padding-left: 4px;"
        )
        self.lineEdit_email.setPlaceholderText("Digite o email")
        self.lineEdit_email.setObjectName("lineEdit_email")

        # ------------------- Botões -------------------
        button_style = (
            "QPushButton {\n"
            "background: #504B4B;\n"
            "color: #FFFFFF;\n"
            "border-radius: 4px;\n"
            "padding: 5px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "background-color: #5599ff;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "background-color: #2e5ea2;\n"
            "padding-top: 8px;\n"
            "padding-bottom: 4px;\n"
            "}"
        )

        self.pushButton_cadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cadastrar.setGeometry(QtCore.QRect(450, 270, 75, 23))
        self.pushButton_cadastrar.setStyleSheet(button_style)
        self.pushButton_cadastrar.setObjectName("pushButton_cadastrar")

        self.pushButtor_visu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtor_visu.setGeometry(QtCore.QRect(450, 300, 75, 23))
        self.pushButtor_visu.setStyleSheet(button_style)
        self.pushButtor_visu.setObjectName("pushButtor_visu")

        self.pushButton_editar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_editar.setGeometry(QtCore.QRect(450, 330, 75, 23))
        self.pushButton_editar.setStyleSheet(button_style)
        self.pushButton_editar.setObjectName("pushButton_editar")

        self.pushButton_excluir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_excluir.setGeometry(QtCore.QRect(450, 360, 75, 23))
        self.pushButton_excluir.setStyleSheet(button_style)
        self.pushButton_excluir.setObjectName("pushButton_excluir")


        self.pushButton_historico = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_historico.setGeometry(QtCore.QRect(450, 390, 75, 23))
        self.pushButton_historico.setStyleSheet(button_style)
        self.pushButton_historico.setObjectName("pushButton_historico")

        self.pushButton_retornar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_retornar.setGeometry(QtCore.QRect(450, 240, 75, 23))
        self.pushButton_retornar.setStyleSheet(button_style)
        self.pushButton_retornar.setObjectName("pushButton_retornar")
        self.pushButton_retornar.hide()
        # ------------------- Labels -------------------
        labels = [
            ("label_nome", 40, 90, "Nome:"),
            ("label_cpf", 380, 90, "CPF:"),
            ("label_data", 40, 148, "Data de Nasc.:"),
            ("label_sexo", 210, 150, "Sexo:"),
            ("label_telefone", 260, 148, "Telefone:"),
            ("label_email_2", 390, 150, "Email:"),
            
        ]

        for obj, x, y, text in labels:
            label = QtWidgets.QLabel(self.centralwidget)
            label.setGeometry(QtCore.QRect(x, y, 120, 16))
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            label.setFont(font)
            label.setObjectName(obj)
            label.setText(text)
            setattr(self, obj, label)

        # ------------------- ID -------------------
        self.lineEdit_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_id.setEnabled(False)
        self.lineEdit_id.setGeometry(QtCore.QRect(40, 230, 71, 20))
        self.lineEdit_id.setStyleSheet(
            "color:#333;\n"
            "background: transparent;\n"
            "border-radius: 4px;\n"
            "border: 1px solid #AAAAAA;\n"
            "padding-left: 4px;"
        )
        self.lineEdit_id.setPlaceholderText("Digite o ID")
        self.lineEdit_id.setObjectName("lineEdit_id")

        self.label_id = QtWidgets.QLabel(self.centralwidget)
        self.label_id.setGeometry(QtCore.QRect(40, 210, 21, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_id.setFont(font)
        self.label_id.setObjectName("label_id")
        self.label_id.setText("ID:")

        # ------------------- Tabela -------------------
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 270, 391, 181))
        self.tableWidget.setStyleSheet(
            "QTableWidget { background-color: #F5F5F5; alternate-background-color: #E0FFFF; }\n"
            "QHeaderView::section { background-color: #504B4B; color: white; font-weight: bold; }"
        )

        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels([
            "ID", "Nome", "CPF", "Data de Nasc.", "Sexo", "Telefone", "Email"
        ])

        self.tableWidget.setColumnWidth(0, 10)
        self.tableWidget.setColumnWidth(6, 100)

        TelaPaciente.setCentralWidget(self.centralwidget)

        # ------------------- Tabela do Trigger (Histórico) -------------------
        self.tableWidgetHistorico = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetHistorico.setGeometry(QtCore.QRect(40, 270, 500, 181))
        self.tableWidgetHistorico.setStyleSheet(
        "QTableWidget { background-color: #F5F5F5; alternate-background-color: #E0FFFF; }\n"
        "QHeaderView::section { background-color: #504B4B; color: white; font-weight: bold; }"
        )

        self.tableWidgetHistorico.setColumnCount(6)
        self.tableWidgetHistorico.setRowCount(0)
        self.tableWidgetHistorico.setHorizontalHeaderLabels([
        "ID Hist.", "ID Paciente", "Campo", "Valor Antigo", "Valor Novo", "Data"
        ])

        self.tableWidgetHistorico.setColumnWidth(0, 60)
        self.tableWidgetHistorico.setColumnWidth(1, 80)
        self.tableWidgetHistorico.setColumnWidth(2, 100)
        self.tableWidgetHistorico.setColumnWidth(3, 120)
        self.tableWidgetHistorico.setColumnWidth(4, 120)
        self.tableWidgetHistorico.setColumnWidth(5, 100)
        self.tableWidgetHistorico.hide()
        
        # Barra de status
        self.statusbar = QtWidgets.QStatusBar(TelaPaciente)
        self.statusbar.setObjectName("statusbar")
        TelaPaciente.setStatusBar(self.statusbar)
        TelaPaciente.setWindowIcon(QtGui.QIcon("hospital.png"))
        self.retranslateUi(TelaPaciente)
        QtCore.QMetaObject.connectSlotsByName(TelaPaciente)

    def retranslateUi(self, TelaPaciente):
        _translate = QtCore.QCoreApplication.translate
        TelaPaciente.setWindowTitle(_translate("TelaPaciente", "Sistema Hospitalar"))
        self.Label_titulo.setText(_translate("TelaPaciente", "Informações do Paciente"))
        self.pushButton_cadastrar.setText(_translate("TelaPaciente", "Cadastrar"))
        self.pushButtor_visu.setText(_translate("TelaPaciente", "Visualizar"))
        self.pushButton_editar.setText(_translate("TelaPaciente", "Editar"))
        self.pushButton_excluir.setText(_translate("TelaPaciente", "Excluir"))
       
        self.pushButton_historico.setText(_translate("TelaPaciente", "Histórico"))
        self.pushButton_retornar.setText(_translate("TelaPaciente", "Retornar"))
        self.tableWidget.setSortingEnabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaPaciente = QtWidgets.QMainWindow()
    ui = Ui_TelaPaciente()
    ui.setupUi(TelaPaciente)
    TelaPaciente.show()
    sys.exit(app.exec_())
