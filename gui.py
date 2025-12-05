from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from crud import criar_paciente, listar_pacientes, atualizar_paciente, deletar_paciente,criar_enfermeiro, listar_enfermeiros, atualizar_enfermeiro, deletar_enfermeiro,criar_medico, listar_medicos, atualizar_medico, deletar_medico, criar_atendimento, atualizar_atendimento, listar_atendimentos, listar_historico_paciente, criar_arquivo, listar_arquivo, deletar_atendimento, obter_turno_atual, criar_hospital, atualizar_hospital, listar_hospitais, deletar_hospital
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem
from janela_paciente import Ui_TelaPaciente
from janela_enfermeiro import Ui_TelaEnfermeiro
from janela_medico import Ui_TelaMedico
from janela_atendimento import Ui_TelaAtendimento
from datetime import date
from janela_telaMenu import Ui_TelaMenu
from telaArquivo import Ui_TelaArquivo
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QTimer
from tela_hospital import Ui_TelaHospital
from janela_setor import Ui_TelaSetor
from janela_internacao import Ui_TelaInternacao
from janela_estado import Ui_TelaEstado
from janela_cidade import Ui_TelaCidade
from janela_administrador import Ui_TelaAdministrador


class AnimatedWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.animation_duration = 350  # ms

    def showEvent(self, event):
        """Animação de entrada (slide from right)."""
        screen_geo = self.frameGeometry()
        start_x = screen_geo.x() + screen_geo.width()
        end_x = screen_geo.x()

        self.setGeometry(
            start_x, screen_geo.y(),
            screen_geo.width(), screen_geo.height()
        )

        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(self.animation_duration)
        self.anim.setStartValue(QRect(start_x, screen_geo.y(),
                                      screen_geo.width(), screen_geo.height()))
        self.anim.setEndValue(QRect(end_x, screen_geo.y(),
                                    screen_geo.width(), screen_geo.height()))
        self.anim.setEasingCurve(QEasingCurve.OutCubic)
        self.anim.start()
        super().showEvent(event)

    def closeEvent(self, event):
        """Animação de saída (slide to right)."""
        screen_geo = self.frameGeometry()
        end_x = screen_geo.x() + screen_geo.width()

        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(self.animation_duration)
        self.anim.setStartValue(screen_geo)
        self.anim.setEndValue(QRect(end_x, screen_geo.y(),
                                    screen_geo.width(), screen_geo.height()))
        self.anim.setEasingCurve(QEasingCurve.InCubic)
        self.anim.start()


    def _force_close(self):
        super().close()


class TelaSetor(AnimatedWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TelaSetor()
        self.ui.setupUi(self)
    
        

class TelaEstado(AnimatedWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TelaEstado()
        self.ui.setupUi(self)
    
        

class TelaCidade(AnimatedWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TelaCidade()
        self.ui.setupUi(self)
    
        

class TelaAdministrador(AnimatedWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TelaAdministrador()
        self.ui.setupUi(self)
    
class TelaInternacao(AnimatedWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TelaInternacao()
        self.ui.setupUi(self)
    
        



class TelaHospital(AnimatedWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TelaHospital()
        self.ui.setupUi(self)
    
        self.ui.pushButton_cadastrar.clicked.connect(self.botao_cadastrar_hospital_clicked)
        self.ui.pushButton_editar.clicked.connect(self.botao_atualizar_hospital_clicked)
        self.ui.pushButton_visu.clicked.connect(self.botao_visualizar_hospital_clicked)
        self.ui.pushButton_excluir.clicked.connect(self.botao_excluir_hospital_clicked)

    def botao_excluir_hospital_clicked(self):
        id = self.ui.lineEdit_id.text()

        try:
            deletar_hospital(id)
            QMessageBox.information(self,"Sucesso!","Hospital excluído")
        except Exception as e:
            QMessageBox.warning(self,"Erro!",f"Não foi possível excluir hospital{e}")


    def botao_visualizar_hospital_clicked(self):
        id = self.ui.lineEdit_id.text()
        listaHospitais = listar_hospitais(id)
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.verticalHeader().setVisible(False)
            
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        for linha, registro in enumerate(listaHospitais):
            self.ui.tableWidget.insertRow(linha)
            for coluna_n, valor in enumerate(registro):
                self.ui.tableWidget.setItem(linha, coluna_n, QTableWidgetItem(str(valor)))
        
        self.ui.lineEdit_id.clear()
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)



    def botao_atualizar_hospital_clicked(self):
        id = self.ui.lineEdit_id.text()
        cnpj = self.ui.lineEdit_cnpj.text()
        nome = self.ui.lineEdit_nome.text()
        telefone = self.ui.lineEdit_telefone.text()
        email = self.ui.lineEdit_email.text()
        end = self.ui.lineEdit_endereco
        
        try:
            atualizar_hospital(id,cnpj, nome, telefone, email, end)
            QMessageBox.information(self, "Sucesso!", "Dados do hospital atualizados!")
        except Exception as e:
            QMessageBox.warning(self, "Erro", f"Não foi possível atualizar hospital:{e}.")

    def botao_cadastrar_hospital_clicked(self):
        cnpj = self.ui.lineEdit_cnpj.text()
        nome = self.ui.lineEdit_nome.text()
        telefone = self.ui.lineEdit_telefone.text()
        email = self.ui.lineEdit_email.text()
        end = self.ui.lineEdit_endereco.text()
        id_adm = self.ui.lineEdit_id_admin.text()

        try:
            criar_hospital(cnpj, nome, telefone,email, end, id_adm)
            QMessageBox.information(self, "Sucesso!", "Hospital cadastrado com sucesso")
        except Exception as e:
            QMessageBox.warning(self, "Erro", f"Não foi possível cadastrar hospital: {e}")

class TelaPaciente(AnimatedWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TelaPaciente()
        self.ui.setupUi(self)

        
        self.ui.pushButton_cadastrar.clicked.connect(self.botao_cadastrar_clicked)
        self.ui.pushButtor_visu.clicked.connect(self.botao_visualizar_clicked)
        self.ui.pushButton_excluir.clicked.connect(self.botao_excluir_clicked)
        self.ui.pushButton_editar.clicked.connect(self.botao_editar_clicked)
        self.ui.pushButton_historico.clicked.connect(self.botao_historico_clicked)
        self.ui.pushButton_retornar.clicked.connect(self.botao_retornar_clicked)


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

           

            criar_paciente(nome, cpf, data_str, sexo, telefone, email)
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
   
        
    def botao_editar_clicked(self):
        id =  self.ui.lineEdit_id.text()
        nome = self.ui.lineEdit_nome.text()
        cpf = self.ui.lineEdit_cpf.text()
        sexo = self.ui.lineEdit_sexo.text()
        telefone = self.ui.lineEdit_telefone.text()
        email = self.ui.lineEdit_email.text()
        data_st = self.ui.lineEdit_data.text()
        
        if sexo == "Selecione":
            sexo = None
        
        
        atualizar_paciente(id,nome, cpf, data_st,sexo, telefone, email)
        QMessageBox.information(self, "Sucesso", "Paciente atualizado com sucesso!")

        # Limpa os campos
        self.ui.lineEdit_nome.clear()
        self.ui.lineEdit_cpf.clear()
        self.ui.lineEdit_data.clear()
        self.ui.lineEdit_sexo.clear()
        self.ui.lineEdit_telefone.clear()
        self.ui.lineEdit_email.clear()
        self.ui.lineEdit_data.clear()
        self.ui.pushButton_editar.lower()
        self.ui.lineEdit_id.setEnabled(False)

    def botao_excluir_clicked(self):
        id = self.ui.lineEdit_id.text()

        try:
            deletar_paciente(id)
            QMessageBox.information(self, "Sucesso", "Paciente removido com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Ocorreu um erro ao tentar exluir o paciente:\n{e}")

    def botao_historico_clicked(self):
        
        self.ui.tableWidget.hide()
        self.ui.tableWidgetHistorico.show()
        self.ui.pushButton_retornar.show()
        lista_historicos = listar_historico_paciente()
        self.ui.tableWidgetHistorico.setRowCount(0)
        self.ui.tableWidgetHistorico.verticalHeader().setVisible(False)
        
        self.ui.tableWidgetHistorico.horizontalHeader().setStretchLastSection(True)
        for linha, registro in enumerate(lista_historicos):
            self.ui.tableWidgetHistorico.insertRow(linha)
            for coluna_n, valor in enumerate(registro):
                self.ui.tableWidgetHistorico.setItem(linha, coluna_n, QTableWidgetItem(str(valor)))

    
    def botao_retornar_clicked(self):
        self.ui.tableWidget.show()
        self.ui.tableWidgetHistorico.hide()
        self.ui.pushButton_retornar.hide()

class TelaEnfermeiro(AnimatedWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TelaEnfermeiro()
        self.ui.setupUi(self)

        
        self.ui.pushButton_cadastrar.clicked.connect(self.botao_cadastrar_enfermeiro_clicked)
        self.ui.pushButton_visu.clicked.connect(self.botao_visualizar_enfermeiro_clicked)
        self.ui.pushButton_editar.clicked.connect(self.botao_atualizar_enfermeiro_clicked)
        self.ui.pushButton_excluir.clicked.connect(self.botao_excluir_enfermeiro_clicked)    
        
    def botao_cadastrar_enfermeiro_clicked(self):
        self.ui.lineEdit_id.setEnabled(False)
        try:
            nome = self.ui.lineEdit_nome.text()
            coren = self.ui.lineEdit_coren.text()
            status = self.ui.combo_status.currentText()


            

            criar_enfermeiro(nome, coren, status)
            QMessageBox.information(self, "Sucesso", "Enfermeiro cadastrado com sucesso!")

            # Limpa os campos
            self.ui.lineEdit_nome.clear()
            self.ui.lineEdit_coren.clear()
            
            

        except ValueError as ve:
            QMessageBox.warning(self, "Atenção", str(ve))
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Ocorreu um erro ao cadastrar enfermeiro:\n{e}")
            

    def botao_visualizar_enfermeiro_clicked(self):
        self.ui.lineEdit_id.setEnabled(True)
        id_enferm = self.ui.lineEdit_id.text()

        if id_enferm == "":
            id_enferm = None
        else:
            id_enferm = int(id_enferm)

        listaEnferms = listar_enfermeiros(id_enferm)
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.verticalHeader().setVisible(False)
        
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        for linha, registro in enumerate(listaEnferms):
            self.ui.tableWidget.insertRow(linha)
            for coluna_n, valor in enumerate(registro):
                self.ui.tableWidget.setItem(linha, coluna_n, QTableWidgetItem(str(valor)))
        
            self.ui.lineEdit_id.clear()
            self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
    
    def botao_atualizar_enfermeiro_clicked(self):
        id = self.ui.lineEdit_id.text()
        novo_nome = self.ui.lineEdit_nome.text()
        novo_coren = self.ui.lineEdit_coren.text()
        novo_status = self.ui.combo_status.currentText()

        atualizar_enfermeiro(id, novo_nome, novo_coren, novo_status)
        QMessageBox.information(self, "Sucesso", "Enfermeiro atualizado com sucesso!")

        # Limpa os campos
        self.ui.lineEdit_nome.clear()
        self.ui.lineEdit_coren.clear()
    
    def botao_excluir_enfermeiro_clicked(self):
        id = self.ui.lineEdit_id.text()

        
        try:
            deletar_enfermeiro(id)
            QMessageBox.information(self, "Sucesso", "Enfermeiro removido com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Ocorreu um erro ao tentar exluir o enfermeiro:\n{e}")


class TelaMedico(AnimatedWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TelaMedico()
        self.ui.setupUi(self)

        self.ui.pushButton_cadastrar.clicked.connect(self.botao_cadastrar_medico_clicked)
        self.ui.pushButtor_visu.clicked.connect(self.botao_visualizar_medico_clicked)
        self.ui.pushButton_editar.clicked.connect(self.botao_atualizar_medico_clicked)
        self.ui.pushButton_excluir.clicked.connect(self.botao_deletar_medico_clicked)

    def botao_cadastrar_medico_clicked(self):
        
        try:
            nome_medico = self.ui.lineEdit_nome.text()
            crm = self.ui.lineEdit_crm.text()
            esp = self.ui.lineEdit_especialidade.text()

            criar_medico(crm, nome_medico,esp)
            QMessageBox.information(self, "Sucesso", "Médico cadastrado com sucesso!")
            self.ui.lineEdit_nome.clear()
            self.ui.lineEdit_crm.clear()
            self.ui.lineEdit_especialidade.clear()


        except ValueError as ve:
            QMessageBox.warning(self, "Atenção", str(ve))
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Ocorreu um erro ao cadastrar o Médico:\n{e}")

    def botao_visualizar_medico_clicked(self):
      
        self.ui.lineEdit_id.setEnabled(True)
        id_medico = self.ui.lineEdit_id.text()

        if id_medico == "":
            id_medico = None
        else:
            id_medico = int(id_medico)

        listaMedicos = listar_medicos(id_medico)
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.verticalHeader().setVisible(False)
        
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        for linha, registro in enumerate(listaMedicos):
            self.ui.tableWidget.insertRow(linha)
            for coluna_n, valor in enumerate(registro):
                self.ui.tableWidget.setItem(linha, coluna_n, QTableWidgetItem(str(valor)))
        
            self.ui.lineEdit_id.clear()
            self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
    
    def botao_atualizar_medico_clicked(self):
        id_medico = self.ui.lineEdit_id.text()
        novo_nome = self.ui.lineEdit_nome.text()
        novo_crm = self.ui.lineEdit_crm.text()
        nova_esp = self.ui.lineEdit_especialidade.text()

        
        atualizar_medico(id_medico,novo_crm, novo_nome,nova_esp)
        QMessageBox.information(self, "Sucesso", "Médico atualizado com sucesso!")
        self.ui.lineEdit_nome.clear()
        self.ui.lineEdit_crm.clear()
        self.ui.lineEdit_especialidade.clear()
    
    def botao_deletar_medico_clicked(self):
        id_medico = self.ui.lineEdit_id.text()

        try:
            deletar_medico(id_medico)
            QMessageBox.information(self, "Sucesso", "Medico removido com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Ocorreu um erro ao tentar exluir médico:\n{e}")

class TelaAtendimento(AnimatedWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TelaAtendimento()
        self.ui.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.atualizar_turno)
        self.timer.start(60000) 
        self.atualizar_turno()

        self.ui.pushButton_salvar.clicked.connect(self.botao_salvar_atendimento_clicked)
        self.ui.pushButtor_visu.clicked.connect(self.botao_visualizar_atendimento_clicked)
        self.ui.pushButton_editar.clicked.connect(self.botao_editar_atendimentos_clicked)
        self.ui.pushButton_excluir.clicked.connect(self.botao_excluir_atendimento_clicked)
        
    def atualizar_turno(self):
        turno = obter_turno_atual()

        if turno is None:
            self.ui.lineEdit_qtd_medicos.setText("0")
            self.ui.lineEdit_qtd_enfermeiros.setText("0")
            return

        self.ui.lineEdit_qtd_medicos.setText(str(turno.total_medicos_ativos))
        self.ui.lineEdit_qtd_enfermeiros.setText(str(turno.total_enfermeiros_ativos))



    def botao_salvar_atendimento_clicked(self):
        

        tipo_atend = self.ui.lineEdit_tipoAten.text()   
        data_atend = self.ui.lineEdit_data.text()
        id_paciente = self.ui.lineEdit_id_pacien.text()
        id_medico = self.ui.lineEdit_id_medico.text()
        id_enfer = self.ui.lineEdit_id_enferm.text()
        status = self.ui.comboBox_status.currentText()
        
        data = None
        if data_atend:
            try:
                data = datetime.strptime(data_atend, "%d/%m/%Y").date()
            except ValueError:
                QMessageBox.warning(self, "Erro", "Data inválida! Use dd/mm/aaaa.")
                return


        try:
            
            criar_atendimento(tipo_atendimento=tipo_atend,data_atendimento=data,status=status,id_paciente=id_paciente,id_medico=id_medico,id_enfermeiro=id_enfer)
            QMessageBox.information(self, "Sucesso", "Atendimento salvo com sucesso!")
            self.ui.lineEdit_tipoAten.clear()   
            self.ui.lineEdit_data.clear()
            self.ui.lineEdit_id_pacien.clear()
            self.ui.lineEdit_id_medico.clear()
            self.ui.lineEdit_id_enferm.clear()
            
        except Exception as e:
            QMessageBox.warning(self, "Erro!", f"Não foi possível salvar atendimento:\n{e}")

    def botao_visualizar_atendimento_clicked(self):
        id_atend = self.ui.lineEdit_id.text()
        listaAtendimentos = listar_atendimentos(id_atend)

        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.verticalHeader().setVisible(False)
            
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        for linha, registro in enumerate(listaAtendimentos):
            self.ui.tableWidget.insertRow(linha)
            for coluna_n, valor in enumerate(registro):
                self.ui.tableWidget.setItem(linha, coluna_n, QTableWidgetItem(str(valor)))
            
            self.ui.lineEdit_id.clear()
            self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)

    def botao_editar_atendimentos_clicked(self):
        id_atend = self.ui.lineEdit_id.text()
        novo_tipo_aten = self.ui.lineEdit_tipoAten.text()   
        nova_data_atend = self.ui.lineEdit_data.text()
        novo_status = self.ui.comboBox_status.currentText()
        novo_id_paciente = self.ui.lineEdit_id_pacien.text()
        novo_id_medico = self.ui.lineEdit_id_medico.text()
        novo_id_enfer = self.ui.lineEdit_id_enferm.text()
        
        
        
        if nova_data_atend =="//":
            nova_data_atend = date.today()

        try:
            
            atualizar_atendimento(id_atend, novo_tipo_aten,nova_data_atend,novo_id_paciente, novo_id_medico, novo_id_enfer, novo_status)
            QMessageBox.information(self, "Sucesso", "Atendimento atualizado com sucesso!")
            self.ui.lineEdit_tipoAten.clear()   
            self.ui.lineEdit_data.clear()
            self.ui.lineEdit_id_pacien.clear()
            self.ui.lineEdit_id_medico.clear()
            self.ui.lineEdit_id_enferm.clear()
            
        except Exception as e:
            QMessageBox.warning(self, "Erro!", f"Não foi possível salvar atendimento:\n{e}")


    def botao_excluir_atendimento_clicked(self):
        id = self.ui.lineEdit_id.text()

        try:
            deletar_atendimento(id)
            self.ui.lineEdit_id.clear()
            QMessageBox.information(self, "Sucesso!", "Atendimento deletado com êxito!")
        except Exception as e:
            QMessageBox.warning(self, "Erro!", f"Não foi possível deletar atendimento:\n{e}")
            
class TelaArquivo(AnimatedWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TelaArquivo()
        self.ui.setupUi(self)

        self.ui.pushButton_cadastrar.clicked.connect(self.botao_salvar_arquivo_clicked)
        self.ui.pushButtor_visu_2.clicked.connect(self.botao_buscar_arquivo_clicked)
        self.ui.pushButtor_visu.clicked.connect(self.botao_visualizar_arquivo_cliked)

    def botao_buscar_arquivo_clicked(self):
        caminho, _ = QFileDialog.getOpenFileName(self, "Escolher arquivo", "", "Todos os Arquivos (*)")
        if caminho:
            self.caminho = caminho
            QMessageBox.information(self, "Arquivo escolhido", f"Arquivo selecionado:\n{caminho}")

    def botao_salvar_arquivo_clicked(self):
        
        if not self.caminho:
            return 

        try:
            criar_arquivo(self.caminho)
            QMessageBox.information(self, "Sucesso!", "Arquivo salvo!")
        except Exception as e:
            QMessageBox.warning(self, "Erro", f"Não foi possível salvar arquivo\n{e}")

    def botao_visualizar_arquivo_cliked(self):
        listaArquivos = listar_arquivo()
        self.ui.tableWidget.setRowCount(0)

        self.ui.tableWidget.verticalHeader().setVisible(False)
        for linha, arq in enumerate(listaArquivos):
            self.ui.tableWidget.insertRow(linha)

            self.ui.tableWidget.setItem(linha, 0, QTableWidgetItem(str(arq.id)))
            self.ui.tableWidget.setItem(linha, 1, QTableWidgetItem(arq.nome))
            self.ui.tableWidget.setItem(linha, 2, QTableWidgetItem(f"{len(arq.dados)} bytes"))



class TelaMenuGUI(AnimatedWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TelaMenu()
        self.ui.setupUi(self)

        # Conectar botões às telas correspondentes
        self.ui.pushButton_paciente.clicked.connect(self.abrir_paciente)
        self.ui.pushButton_enfermeiro.clicked.connect(self.abrir_enfermeiro)
        self.ui.pushButton_medico.clicked.connect(self.abrir_medico)
        self.ui.pushButton_atendimento.clicked.connect(self.abrir_atendimento)
        self.ui.pushButton_hospital.clicked.connect(self.abrir_hospital)
        self.ui.pushButton_setor.clicked.connect(self.abrir_setor)
        self.ui.pushButton_estado.clicked.connect(self.abrir_estado)
        self.ui.pushButton_cidade.clicked.connect(self.abrir_cidade)
        self.ui.pushButton_internacoes.clicked.connect(self.abrir_internacao)
        self.ui.pushButton_arquivo.clicked.connect(self.abrir_arquivo)
        # Paginação
        self.ui.pushButton_proxPag.clicked.connect(self.proxima_pag)
        self.ui.pushButton_pagAnterior.clicked.connect(self.pagina_anterior)

        # Inicialmente, nenhuma tela aberta
        self.tela_paciente = None
        self.tela_enfermeiro = None
        self.tela_medico = None
        self.tela_atendimento = None
        self.tela_hospital = None
        self.tela_setor = None
        self.tela_estado = None
        self.tela_cidade = None
        self.tela_internacao = None
        self.tela_arquivo = None

    # =========================
    # Métodos para abrir telas
    # =========================
    def abrir_paciente(self):
        if self.tela_paciente is None:
            self.tela_paciente = TelaPaciente()
        self.tela_paciente.show()

    def abrir_enfermeiro(self):
        if self.tela_enfermeiro is None:
            self.tela_enfermeiro = TelaEnfermeiro()
        self.tela_enfermeiro.show()

    def abrir_medico(self):
        if self.tela_medico is None:
            self.tela_medico = TelaMedico()
        self.tela_medico.show()

    def abrir_atendimento(self):
        if self.tela_atendimento is None:
            self.tela_atendimento = TelaAtendimento()
        self.tela_atendimento.show()

    def abrir_hospital(self):
        if self.tela_hospital is None:
            self.tela_hospital = TelaHospital()
        self.tela_hospital.show()

    def abrir_setor(self):
        if self.tela_setor is None:
            self.tela_setor = TelaSetor()
        self.tela_setor.show()

    def abrir_estado(self):
        if self.tela_estado is None:
            self.tela_estado = TelaEstado()
        self.tela_estado.show()

    def abrir_cidade(self):
        if self.tela_cidade is None:
            self.tela_cidade = TelaCidade()
        self.tela_cidade.show()

    def abrir_internacao(self):
        if self.tela_internacao is None:
            self.tela_internacao = TelaInternacao()
        self.tela_internacao.show()

    def abrir_arquivo(self):
        if self.tela_arquivo is None:
            self.tela_arquivo = TelaArquivo()
        self.tela_arquivo.show()
    # =========================
    # Paginação
    # =========================
    def proxima_pag(self): 
        self.ui.pushButton_paciente.hide() 
        self.ui.pushButton_enfermeiro.hide() 
        self.ui.pushButton_medico.hide() 
        self.ui.pushButton_arquivo.hide() 
        self.ui.pushButton_atendimento.hide() 
        self.ui.pushButton_leito.hide() 
        self.ui.pushButton_setor.hide() 
        self.ui.pushButton_turno.hide() 
        self.ui.pushButton_proxPag.hide() 

        self.ui.pushButton_pagAnterior.show() 
        self.ui.pushButton_internacoes.show() 
        self.ui.pushButton_estado.show() 
        self.ui.pushButton_cidade.show() 
        self.ui.pushButton_hospital.show()

    def pagina_anterior(self): 
        self.ui.pushButton_pagAnterior.hide() 
        self.ui.pushButton_internacoes.hide() 
        self.ui.pushButton_estado.hide() 
        self.ui.pushButton_cidade.hide() 
        self.ui.pushButton_hospital.hide() 
        self.ui.pushButton_paciente.show() 
        self.ui.pushButton_enfermeiro.show() 
        self.ui.pushButton_medico.show() 
        self.ui.pushButton_arquivo.show() 
        self.ui.pushButton_atendimento.show() 
        self.ui.pushButton_leito.show() 
        self.ui.pushButton_setor.show() 
        self.ui.pushButton_turno.show() 
        self.ui.pushButton_proxPag.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    janela = TelaMenuGUI()
    janela.show()
    sys.exit(app.exec_())
    
