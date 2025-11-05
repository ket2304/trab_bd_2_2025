from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from crud import criar_paciente, listar_pacientes, atualizar_paciente, deletar_paciente
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem
from janela_paciente import Ui_TelaMenu




class TelaPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TelaMenu()
        self.ui.setupUi(self)

        
        self.ui.pushButton_cadastrar.clicked.connect(self.botao_cadastrar_clicked)
        self.ui.pushButtor_visu.clicked.connect(self.botao_visualizar_clicked)
        self.ui.pushButton_atualizar.clicked.connect(self.botao_atualizar_clicked)
        self.ui.pushButton_excluir.clicked.connect(self.botao_excluir_clicked)
        self.ui.pushButton_editar.clicked.connect(self.botao_editar_clicked)
            
    def botao_cadastrar_clicked(self):
        self.ui.lineEdit_id.setEnabled(False)
        try:
            nome = self.ui.lineEdit_nome.text()
            cpf = self.ui.lineEdit_cpf.text()
            data_str = self.ui.lineEdit_data.text()
            sexo = self.ui.lineEdit_sexo.text()
            telefone = self.ui.lineEdit_telefone.text()
            email = self.ui.lineEdit_email.text()

            if sexo == "Selecione":
                sexo = None

            data = None
            if data_str:
                try:
                    data = datetime.strptime(data_str, "%d/%m/%Y").date()
                except ValueError:
                    QMessageBox.warning(self, "Erro", "Data inválida! Use dd/mm/aaaa.")
                    return

            criar_paciente(nome, cpf, data, sexo, telefone, email)
            QMessageBox.information(self, "Sucesso", "Paciente cadastrado com sucesso!")

            # Limpa os campos
            self.ui.lineEdit_nome.clear()
            self.ui.lineEdit_cpf.clear()
            self.ui.lineEdit_data.clear()
            self.ui.lineEdit_sexo.clear()
            self.ui.lineEdit_telefone.clear()
            self.ui.lineEdit_email.clear()

        except ValueError as ve:
            QMessageBox.warning(self, "Atenção", str(ve))
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Ocorreu um erro ao cadastrar o paciente:\n{e}")
            
    def botao_visualizar_clicked(self):
            self.ui.lineEdit_id.setEnabled(True)
            id = self.ui.lineEdit_id.text()
            lista = listar_pacientes(id)
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.verticalHeader().setVisible(False)
            
            self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
            for linha, registro in enumerate(lista):
                self.ui.tableWidget.insertRow(linha)
                for coluna_n, valor in enumerate(registro):
                    self.ui.tableWidget.setItem(linha, coluna_n, QTableWidgetItem(str(valor)))
            
            self.ui.lineEdit_id.clear()
            self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
                    
    def botao_atualizar_clicked(self):
        self.ui.lineEdit_id.setEnabled(True)
        self.ui.pushButton_editar.setEnabled(True)
        self.ui.pushButton_atualizar.lower()
    def botao_editar_clicked(self):
        id =  self.ui.lineEdit_id.text()
        nome = self.ui.lineEdit_nome.text()
        cpf = self.ui.lineEdit_cpf.text()
        sexo = self.ui.lineEdit_sexo.text()
        telefone = self.ui.lineEdit_telefone.text()
        email = self.ui.lineEdit_email.text()

        if sexo == "Selecione":
            sexo = None
        
        atualizar_paciente(id,nome, cpf, sexo, telefone, email)
        QMessageBox.information(self, "Sucesso", "Paciente atualizado com sucesso!")

        # Limpa os campos
        self.ui.lineEdit_nome.clear()
        self.ui.lineEdit_cpf.clear()
        self.ui.lineEdit_data.clear()
        self.ui.lineEdit_sexo.clear()
        self.ui.lineEdit_telefone.clear()
        self.ui.lineEdit_email.clear()

        self.ui.pushButton_editar.lower()
        self.ui.lineEdit_id.setEnabled(False)
    def botao_excluir_clicked(self):
        id = self.ui.lineEdit_id.text()

        try:
            deletar_paciente(id)
            QMessageBox.information(self, "Sucesso", "Paciente removido com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Ocorreu um erro ao tentar exluir o paciente:\n{e}")
    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    janela = TelaPrincipal()
    janela.show()
    sys.exit(app.exec_())

