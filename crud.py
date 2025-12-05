from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from db import engine
from models import Base, Paciente, Medico, Internacao, Leito, Hospital, Cidade, Estado, Enfermeiro, Turno, Atendimento, Setor, Administrador, HistoricoPaciente, Arquivos, TurnoPresenca
from datetime import datetime
from db import SessionLocal, engine
from datetime import datetime 
from datetime import date
from sqlalchemy import text
session = SessionLocal()




#------------------------ CREATE --------------------------#
def obter_turno_atual():
    agora = datetime.now().time()

    with SessionLocal() as session:
        turnos = session.query(TurnoPresenca).all()

    for t in turnos:
        
        if t.hora_inicio > t.hora_fim:
            if agora >= t.hora_inicio or agora <= t.hora_fim:
                return t
        else:
            if t.hora_inicio <= agora <= t.hora_fim:
                return t

    return None

def criar_paciente(nome, cpf, data, sexo, telefone, email):
    
    sexo = sexo.capitalize()

    if not nome or not cpf:
        raise ValueError("Nome e CPF são obrigatórios!")

    # Usando sessão local
    with SessionLocal() as session:
        try:
            p = Paciente(
                nome_paciente=nome,
                cpf=cpf,
                data_nascimento=data,
                sexo_paciente=sexo,
                telefone_paciente=telefone,
                email_paciente=email
            )
            session.add(p)
            session.commit()
            print("✅ Paciente cadastrado com sucesso!")
        except SQLAlchemyError as e:
            session.rollback()
            print("❌ Erro ao cadastrar paciente:", e)
            raise

def criar_medico(crm,nome_medico,especialidade):
    
    if not nome_medico or not crm or not especialidade:
        raise ValueError("Nome, CRM  e especialidade são obrigatórios!")
    
    with SessionLocal() as session:
        try:
            m = Medico(
                crm = crm,
                nome_medico = nome_medico,
                especialidade = especialidade
            )
            session.add(m)
            session.commit()
            print("✅ Médico cadastrado com sucesso!")
        except SQLAlchemyError as e:
            session.rollback()
            print("❌ Erro ao cadastrar médico:", e)
            raise


def criar_enfermeiro(nome, coren, status):
    if not nome or not coren or not status:
        raise ValueError("Nome, Coren e Status são obrigatórios!")


    with SessionLocal() as session:
        try:
            session.execute(
                text("CALL insere_enfermeiro(:nome, :coren, :status)"),
                {"nome": nome, "coren": coren, "status": status}
            )
            session.commit()
            print("✅ Enfermeiro cadastrado com sucesso!")

        except SQLAlchemyError as e:
            session.rollback()
            print("❌ Erro ao cadastrar enfermeiro:")
            print("Motivo:", e)
            raise

def crir_administrador():
    session.add(Administrador)
    session.commit()

def criar_hospital(cnpj, nome, telefone, email, endereco, id_adm):
    
    with SessionLocal() as session:
        try:
            h = Hospital(
                cnpj=cnpj,
                nome=nome,
                telefone=telefone,
                email=email,       # corrigido
                endereco=endereco,
                id_adm=id_adm      # corrigido
            )
            session.add(h)
            session.commit()
            print("✅ Hospital cadastrado com sucesso!")
            return True
        except SQLAlchemyError as e:
            session.rollback()
            print("❌ Erro ao cadastrar hospital:", e)
            raise

   
def criar_setor():
    session.add(Setor)
    session.commit()

def criar_leito():
    session.add(Leito)
    session.commit()

def criar_turno():
    session.add(Turno)
    session.commit()

def criar_atendimento(tipo_atendimento, data_atendimento, status, id_paciente, id_medico, id_enfermeiro):

    if not tipo_atendimento or not data_atendimento or not status or not id_paciente or not id_medico or not id_enfermeiro:
        raise ValueError("Os campos Tipo de atendimento, data, status, ID Médico(a), ID paciente e ID enfermeiro(a) são obrigatórios!")
    
    with SessionLocal() as session:
        try:
            # Verificar paciente
            paciente = session.query(Paciente).filter_by(id_paciente=id_paciente).first()
            if not paciente:
                raise ValueError(f"Paciente com ID {id_paciente} não existe.")

            # Verificar médico
            medico = session.query(Medico).filter_by(id_medico=id_medico).first()
            if not medico:
                raise ValueError(f"Médico com ID {id_medico} não existe.")

            # Verificar enfermeiro
            enfermeiro = session.query(Enfermeiro).filter_by(id_enfermeiro=id_enfermeiro).first()

            if not enfermeiro:
                raise ValueError(f"Enfermeiro com ID {id_enfermeiro} não existe.")

            # Verificar se o enfermeiro está ativo
            if enfermeiro.status != "Ativo":
                raise ValueError(f"Enfermeiro com ID {id_enfermeiro} está INATIVO e não pode atender.")

            # Criar o atendimento
            atendimento = Atendimento(
                tipo_atendimento=tipo_atendimento,
                data_atendimento=data_atendimento,
                id_paciente=id_paciente,
                id_medico=id_medico,
                id_enfermeiro=id_enfermeiro,
                status=status
            )

            session.add(atendimento)
            session.commit()
            print("✅ Atendimento salvo com sucesso!")
        
        except SQLAlchemyError as e:
            session.rollback()
            print("❌ Erro ao salvar atendimento:", e)
            raise

def criar_internacao():
    session.add(Internacao)
    session.commit()


def criar_estado():
    session.add(Estado)
    session.commit()

def criar_cidade():
    session.add(Cidade)
    session.commit()

def criar_arquivo(caminho):
    with SessionLocal() as session:
        with open(caminho, "rb") as f:
            binario = f.read()

        arquivo = Arquivos(
            nome=caminho.split('/')[-1],  # pega só o nome do arquivo
            dados=binario
        )

        session.add(arquivo)
        session.commit()

#------------------------------- READ ---------------------------------#
def listar_pacientes(id_paciente = None):
    with SessionLocal() as session:
        if id_paciente is not None and id_paciente != "":
            pacientes = session.query(Paciente).filter_by(id_paciente = id_paciente).all()
            return[ 
         (
                p.id_paciente,
                p.nome_paciente,
                p.cpf, 
                p.data_nascimento,
                p.sexo_paciente,
                p.telefone_paciente,
                p.email_paciente
                
         )
            for p in pacientes]    
        else: 
            pacientes = session.query(Paciente).all()   
            return[ 
            (
                    p.id_paciente,
                    p.nome_paciente,
                    p.cpf, 
                    p.data_nascimento,
                    p.sexo_paciente,
                    p.telefone_paciente,
                    p.email_paciente
                    
            )
                for p in pacientes]
        
def listar_medicos(id_medico = None):
    with SessionLocal() as session:
        if id_medico is not None:
            medicos = session.query(Medico).filter_by(id_medico = id_medico).all()
        else:
            medicos = session.query(Medico).all()
        
        return [
            (m.id_medico, m.nome_medico, m.crm, m.especialidade)
            for m in medicos
        ]
    
def listar_enfermeiros(id_enfermeiro = None):
    with SessionLocal() as session:
        if id_enfermeiro is not None:
            enfermeiros = session.query(Enfermeiro).filter_by(id_enfermeiro=id_enfermeiro).all()
        else:
            enfermeiros = session.query(Enfermeiro).all()

        return [
            (e.id_enfermeiro, e.nome_enfermeiro, e.coren, e.status)
            for e in enfermeiros
        ]

def listar_administrador():
    return session.query(Administrador).all()

def listar_hospitais(id_hospital = None):
    
    with SessionLocal() as session:
        query = session.query(
            Hospital.id_hospital, 
            Hospital.nome, Hospital.cnpj, 
            Hospital.endereco, Hospital.telefone, 
            Hospital.email, 
            Administrador.nome_adm
            
        ).join(Administrador, Hospital.id_adm == Administrador.id_adm)
        

       
        if id_hospital:
            query = query.filter(Hospital.id_hospital == id_hospital)

        # Retorna o resultado
        return query.all()

def listar_setores():
    return session.query(Setor).all()

def listar_leitos():
    return session.query(Leito).all()


def listar_turnos():
    return session.query(Turno).all()

def listar_atendimentos(id_atendimento=None):
    
    
    with SessionLocal() as session:
        # Cria a query base — SEMPRE criada, com ou sem filtro
        query = session.query(
            Atendimento.id_atendimento,
            Atendimento.tipo_atendimento,
            Atendimento.data_atendimento,
            Atendimento.status,
            Medico.nome_medico,
            Paciente.nome_paciente,
            Enfermeiro.nome_enfermeiro
        ).join(Medico, Atendimento.id_medico == Medico.id_medico).join(Paciente, Atendimento.id_paciente == Paciente.id_paciente).join(Enfermeiro,Atendimento.id_enfermeiro == Enfermeiro.id_enfermeiro,isouter=True)  # JOIN opcional caso não tenha enfermeiro
        

        # Se o usuário digitou um ID, aplica o filtro
        if id_atendimento:
            query = query.filter(Atendimento.id_atendimento == id_atendimento)

        # Retorna o resultado
        return query.all()


def listar_internacoes():
    return session.query(Internacao).all()

def listar_estado():
    return  session.query(Estado).all()

def listar_cidades():
    return session.query(Cidade).all()

def listar_historico_paciente():
    with SessionLocal() as session:
        hist_pacientes = session.query(HistoricoPaciente).all()   
        return[(       
        hp.id_historico,
        hp.id_paciente,
        hp.campo_alterado,
        hp.valor_antigo,
        hp.valor_novo,
        hp.data_modificacao                    
        )for hp in hist_pacientes]

def listar_arquivo():
    with SessionLocal() as session:
        return session.query(Arquivos).all()
#----------------------------- UPDATE --------------------------#
def atualizar_paciente(id_paciente, novo_nome = None, cpf_novo=None, data_nova = None,sexo_novo = None, novo_telefone = None, novo_email = None):
    paciente = session.query(Paciente).filter_by(id_paciente = id_paciente).first()
    sexo_novo = sexo_novo.capitalize()

    if paciente:
        
                # === CPF ===
        if paciente.cpf == "..-" and cpf_novo != "..-":
            paciente.cpf = cpf_novo

        elif paciente.cpf != "..-" and cpf_novo == "..-":
            paciente.cpf = paciente.cpf   # mantém

        elif paciente.cpf != "..-" and cpf_novo != "..-":
            paciente.cpf = cpf_novo


        # === NOME ===
        if paciente.nome_paciente == "" and novo_nome != "":
            paciente.nome_paciente = novo_nome

        elif paciente.nome_paciente != "" and novo_nome == "":
            paciente.nome_paciente = paciente.nome_paciente   # mantém

        elif paciente.nome_paciente != "" and novo_nome != "":
            paciente.nome_paciente = novo_nome


        # === SEXO ===
        if paciente.sexo_paciente == "" and sexo_novo != "":
            paciente.sexo_paciente = sexo_novo

        elif paciente.sexo_paciente != "" and sexo_novo == "":
            paciente.sexo_paciente = paciente.sexo_paciente   # mantém

        elif paciente.sexo_paciente != "" and sexo_novo != "":
            paciente.sexo_paciente = sexo_novo


        # === EMAIL ===
        if paciente.email_paciente == "" and novo_email != "":
            paciente.email_paciente = novo_email

        elif paciente.email_paciente != "" and novo_email == "":
            paciente.email_paciente = paciente.email_paciente

        elif paciente.email_paciente != "" and novo_email != "":
            paciente.email_paciente = novo_email


        # === TELEFONE ===
        if paciente.telefone_paciente == "()  -" and novo_telefone != "()  -":
            paciente.telefone_paciente = novo_telefone

        elif paciente.telefone_paciente != "()  -" and novo_telefone == "()  -":
            paciente.telefone_paciente = paciente.telefone_paciente   # mantém

        elif paciente.telefone_paciente != "()  -" and novo_telefone != "()  -":
            paciente.telefone_paciente = novo_telefone


        # === DATA DE NASCIMENTO ===
        if paciente.data_nascimento == "//" and data_nova != "//":
            paciente.data_nascimento = datetime.strptime(data_nova, "%d/%m/%Y").date()

        elif paciente.data_nascimento != "//" and data_nova == "//":
            paciente.data_nascimento = paciente.data_nascimento   # mantém

        elif paciente.data_nascimento != "//" and data_nova != "//":
            paciente.data_nascimento = datetime.strptime(data_nova, "%d/%m/%Y").date()

        # Caso especial: se BOTH forem "//", inserir data do computador
        elif paciente.data_nascimento == "//" and data_nova == "//":
            paciente.data_nascimento = date.today()



        session.commit()

        return True
    else:
        return False 
    
def atualizar_medico(id_medico, novo_crm = None,novo_nome = None, nova_especialidade = None):
    medico = session.query(Medico).filter_by(id_medico = id_medico).first()
    
    if medico:
        if novo_nome:
            medico.nome_medico = novo_nome
        if nova_especialidade:
            medico.especialidade = nova_especialidade
        if novo_crm:
            medico.crm = novo_crm
        session.commit()
        return True
    
    else:
        return False
    
def atualizar_enfermeiro(id_enfermeiro, novo_nome = None, novo_coren = None ,novo_status = None):
    enfermeiro = session.query(Enfermeiro).filter_by(id_enfermeiro = id_enfermeiro).first()

    if enfermeiro:
        if novo_nome:
            enfermeiro.nome_enfermeiro = novo_nome
        if novo_status:
            enfermeiro.status = novo_status
        if novo_coren:
            enfermeiro.coren = novo_coren
        session.commit()
        return True
    
    else:
        return False
    
def atualizar_administrador(id_administrador, novo_nome = None, novo_email = None):
    administrador = session.query(Administrador).filter_by(id_administrador = id_administrador).first()

    if administrador:
        if novo_nome:
            administrador.nome_adm = novo_nome
        if novo_email:
            administrador.email_adm = novo_email
        
        session.commit()
        return True
    else:
        return False
    

def atualizar_hospital(id_hospital, novo_cnpj = None, novo_nome = None, novo_telefone = None, novo_email = None, novo_endereco = None):
    hospital = session.query(Hospital).filter_by(id_hospital=id_hospital).first()

    if hospital:
        # === CNPJ ===
        if hospital.cnpj == "../" and novo_cnpj != "../":
            hospital.cnpj = novo_cnpj
        elif hospital.cnpj != "../" and novo_cnpj == "../":
            hospital.cnpj = hospital.cnpj  # mantém
        elif hospital.cnpj != "../" and novo_cnpj != "../":
            hospital.cnpj = novo_cnpj

        
        # === NOME ===
        if hospital.nome == "" and novo_nome != "":
            hospital.nome = novo_nome
        elif hospital.nome != "" and novo_nome == "":
            hospital.nome = hospital.nome  # mantém
        elif hospital.nome != "" and novo_nome != "":
            hospital.nome = novo_nome

        # === ENDEREÇO ===
        if hospital.endereco == "" and novo_endereco != "":
            hospital.endereco = novo_endereco
        elif hospital.endereco != "" and novo_endereco == "":
            hospital.endereco = hospital.endereco  # mantém
        elif hospital.endereco != "" and novo_endereco != "":
            hospital.endereco = novo_endereco

        # === TELEFONE ===
        if hospital.telefone == "()  -" and novo_telefone != "()  -":
            hospital.telefone = novo_telefone
        elif hospital.telefone != "()  -" and novo_telefone == "()  -":
            hospital.telefone = hospital.telefone  # mantém
        elif hospital.telefone != "()  -" and novo_telefone != "()  -":
            hospital.telefone = novo_telefone

        # === EMAIL ===
        if hospital.email == "" and novo_email != "":
            hospital.email = novo_email
        elif hospital.email != "" and novo_email == "":
            hospital.email = hospital.email  # mantém
        elif hospital.email != "" and novo_email != "":
            hospital.email = novo_email

        session.commit()
        return True
    

    else:
        return False

    
def atualizar_setor(id_setor, novo_nome = None):
    setor = session.query(Setor).filter_by(id_setor = id_setor).first()

    if setor:
        if novo_nome:
            setor.nome_setor = novo_nome
        session.commit()
        return True
    else:
        return False

def atualizar_leito(id_leito, novo_numero = None, novo_tipo = None, nova_capacidade = None):
    leito = session.query(Leito).filter_by(id_leito=id_leito).first()

    if leito:
        if novo_numero:
            leito.numero = novo_numero
        if novo_tipo:
            leito.tipo = novo_tipo
        if nova_capacidade:
            leito.capacidade = nova_capacidade
        session.commit()
        return True
    
    else:
        return False
    

def atualizar_internacao(id_internacao, novo_status = None):
    internacao = session.query(Internacao).filter_by(id_internacao = id_internacao).first()

    if internacao:
        if novo_status:
            internacao.status = novo_status

        session.commit()
        return True

    else:
        return False        

def atualizar_atendimento(
        id_atendimento,
        novo_tipo_atendimento=None,
        nova_data=None,
        novo_id_paciente=None,
        novo_id_medico=None,
        novo_id_enfermeiro=None,
        novo_status=None):

    with SessionLocal() as session:
        atendimento = session.query(Atendimento).filter_by(id_atendimento=id_atendimento).first()
        data = None
        
        if not atendimento:
            raise ValueError("Atendimento não encontrado.")

        # Default para data
        if not nova_data or nova_data == "":
            data = datetime.strptime(nova_data, "%d/%m/%Y").date()
            nova_data = data
    
        
    

        # Aplica atualizações
        if novo_tipo_atendimento:
            atendimento.tipo_atendimento = novo_tipo_atendimento

        atendimento.data_atendimento = nova_data  # sempre atualizado

        if novo_status:
            atendimento.status = novo_status

        if novo_id_paciente:
            atendimento.id_paciente = novo_id_paciente

        if novo_id_medico:
            atendimento.id_medico = novo_id_medico

        if novo_id_enfermeiro:
            atendimento.id_enfermeiro = novo_id_enfermeiro

        session.commit()

    
#------------------------------------DELETE----------------------------------#
def deletar_paciente(id_paciente):
    paciente = session.query(Paciente).filter_by(id_paciente=id_paciente).first()

    # Verifica se o paciente existe
    if not paciente:
        return False

    # Verifica atendimentos abertos
    atendimentos_abertos = [at for at in paciente.atendimentos if at.status == "Aberto"]
    if atendimentos_abertos:
        print("Não é possível deletar: paciente possui atendimentos abertos")
        return False

    # Pode deletar
    session.delete(paciente)
    session.commit()
    return True


def deletar_medico(id_medico):
    medico = session.query(Medico).filter_by(id_medico=id_medico).first()

    if not medico:
        return False
    
    for setor in medico.setores:
        setor.id_medico = None

    for turno in medico.turnos:
        turno.id_medico = None

    atendimentos_abertos = [at for at in medico.atendimentos if at.status == "Aberto"]
    if atendimentos_abertos:
        print("Não é possível deletar: médico possui atendimentos abertos")
        return False

    session.delete(medico)
    session.commit()
    
    return True

def deletar_enfermeiro(id_enfermeiro):
    enfermeiro = session.query(Enfermeiro).filter_by(id_enfermeiro = id_enfermeiro).first()

    if not enfermeiro:
       return False
   
    for setor in enfermeiro.setores:
        setor.id_enfermeiro = None

    for turno in enfermeiro.turnos:
        turno.id_enfermeiro = None

    atendimentos_abertos = [at for at in enfermeiro.atendimentos if at.status == "Aberto"]
    if atendimentos_abertos:
        print("Não é possível deletar: enfermeiro possui atendimentos abertos")
        return False

    
    for atendimento in enfermeiro.atendimentos:
        atendimento.id_enfermeiro = None


    session.delete(enfermeiro)
    session.commit()
    return True

def deletar_administrador(id_administrador):
    administrador = session.query(Administrador).filter_by(id_administrador = id_administrador).first()

    if not administrador:
        return False
    
    if administrador.hospital:
        administrador.hospital.id_adm = None

    session.delete(administrador)
    session.commit()

    return True


def deletar_hospital(id_hospital):
    hospital = session.query(Hospital).filter_by(id_hospital=id_hospital).first()

    if not hospital:
        return False

    
    for setor in hospital.setores:
        session.delete(setor)

    session.delete(hospital)
    session.commit()
    return True

def deletar_setor(id_setor):
    setor = session.query(Setor).filter_by(id_setor = id_setor).first()

    if not setor:
        return False 
    
    leitos_ocupados = [leito for leito in setor.leitos if leito.status == "Ocupado"]
    if leitos_ocupados:
        print("Não é possível deletar: setor possui leitos ocupados.")
        return False



    for leito in setor.leitos:
        session.delete(leito)

    session.delete(setor)
    session.commit()

    return True

def deletar_atendimento(id_atendimento):
    atendimento = session.query(Atendimento).filter_by(id_atendimento = id_atendimento).first()

    if not atendimento:
        return False
    
    if atendimento.status == "Aberto":
        print("Não é possível deletar atendimento: atendimento está em aberto.")
        return False
    
    else:
        session.delete(atendimento)
        session.commit()
    return True

def deletar_leito(id_leito):
    leito = session.query(Leito).filter_by(id_leito = id_leito).first()

    if not leito:
        return False

    if leito.status == "Ocupado":
        print("Não é possível deletar: leito está ocupado.")
        return False
    
    session.delete(leito)
    session.commit()
    return True

def deletar_turno(id_turno):
    turno = session.query(Turno).filter_by(id_turno = id_turno).first()

    if turno:
        session.delete(turno)
        session.commit()
        return True 

    else:
        return False
