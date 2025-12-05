from sqlalchemy import Column, Integer, String, Text, Date, DateTime, Enum, Time, ForeignKey, event, Table
from sqlalchemy.orm import declarative_base, relationship
from datetime import date
from sqlalchemy import LargeBinary

Base = declarative_base()


class Hospital(Base):
    __tablename__ = "tb_hospital"
    id_hospital = Column(Integer, primary_key=True, autoincrement=True)
    cnpj = Column(String (18), nullable=False, unique=True)
    nome = Column(String(255), nullable=False)
    telefone = Column(String(50), nullable=False)
    email = Column(String(255))
    endereco = Column(Text, nullable=False)
    id_adm = Column(Integer, ForeignKey("tb_administrador.id_adm"), unique=False)


    cidade = relationship("Cidade", back_populates="hospitais")
    setores = relationship("Setor", back_populates="hospital")
    administrador = relationship("Administrador", back_populates="hospital")

class Estado(Base):
    __tablename__ = "tb_estado"
    id_estado = Column(Integer, primary_key=True, autoincrement=True)
    estado = Column(String(2), nullable=False)

    cidades = relationship("Cidade", back_populates="estado")

class Cidade(Base):
    __tablename__="tb_cidade"
    id_cidade = Column(Integer, primary_key=True, autoincrement=True)
    cidade = Column(String(100), nullable=False)

    id_estado = Column(Integer, ForeignKey("tb_estado.id_estado"), nullable=False)
    id_hospital = Column(Integer, ForeignKey("tb_hospital.id_hospital"), nullable=False)

    hospitais = relationship("Hospital", back_populates="cidade", cascade="all, delete")
    estado = relationship("Estado", back_populates="cidades")


class Medico(Base):
    __tablename__="tb_medico"
    id_medico = Column(Integer, primary_key=True, autoincrement=True)
    crm = Column(String(16), nullable=False, unique=True)
    nome_medico = Column(String(255), nullable=False)
    especialidade = Column(Text, nullable=False)


    atendimentos = relationship("Atendimento", back_populates="medico", cascade="all, delete-orphan")
    setores = relationship("Setor", back_populates="medico")
    turnos = relationship("Turno", back_populates="medico")

class Enfermeiro(Base):
    __tablename__= "tb_enfermeiro"
    id_enfermeiro = Column(Integer, primary_key=True, autoincrement=True)
    nome_enfermeiro = Column(String(255), nullable=False)
    coren = Column(String(20), nullable=False, unique=True)
    status = Column(Enum("Ativo", "Inativo"), default="Ativo")

    atendimentos = relationship("Atendimento", back_populates="enfermeiro")
    setores = relationship("Setor", back_populates="enfermeiro")
    turnos = relationship("Turno", back_populates="enfermeiro")

class Paciente(Base):
    __tablename__ = "tb_paciente"
    id_paciente = Column(Integer, primary_key=True, autoincrement=True)
    cpf = Column(String(14), nullable=False, unique=True)
    nome_paciente = Column(String(255), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    sexo_paciente = Column(String(1), nullable=False)
    email_paciente = Column(String(255), nullable=False)
    telefone_paciente = Column(String(50), nullable = False)

    
    atendimentos = relationship("Atendimento", back_populates="paciente", cascade="all, delete-orphan")
    internacoes = relationship("Internacao", back_populates="paciente", cascade="all, delete-orphan")
    setores = relationship("Setor", back_populates="paciente")

class Administrador(Base):
    __tablename__ = "tb_administrador"
    id_adm = Column(Integer, primary_key=True, autoincrement=True)
    nome_adm = Column(String(255), nullable=False)
    email_adm = Column(String(255), nullable=False)

    hospital = relationship("Hospital", back_populates="administrador", uselist=False)

class Atendimento(Base):
    __tablename__="tb_atendimento"
    id_atendimento = Column(Integer, primary_key=True, autoincrement=True)
    tipo_atendimento = Column(String(30), nullable=True)
    data_atendimento = Column(DateTime, nullable=False, default=date.today)
    status = Column(Enum("Aberto", "Concluído", "Cancelado"), default="Aberto")


    id_paciente = Column(Integer, ForeignKey("tb_paciente.id_paciente", ondelete="CASCADE"), nullable=False)
    id_medico = Column(Integer, ForeignKey("tb_medico.id_medico", ondelete="CASCADE"), nullable=False)
    id_enfermeiro = Column(Integer, ForeignKey("tb_enfermeiro.id_enfermeiro"), nullable=False)


    paciente = relationship("Paciente", back_populates="atendimentos")
    medico = relationship("Medico", back_populates="atendimentos")
    enfermeiro = relationship("Enfermeiro", back_populates="atendimentos")

class Setor(Base):
    __tablename__ = "tb_setor"
    id_setor = Column(Integer, primary_key=True, autoincrement=True)
    nome_setor = Column(String(30), nullable=True)


    id_hospital = Column(Integer, ForeignKey("tb_hospital.id_hospital"), nullable=False)
    id_paciente = Column(Integer, ForeignKey("tb_paciente.id_paciente"), nullable=False)
    id_medico = Column(Integer, ForeignKey("tb_medico.id_medico"), nullable=False)
    id_enfermeiro = Column(Integer, ForeignKey("tb_enfermeiro.id_enfermeiro"), nullable=False)

    hospital = relationship("Hospital", back_populates="setores")
    medico = relationship("Medico", back_populates="setores")
    enfermeiro = relationship("Enfermeiro", back_populates="setores")
    paciente = relationship("Paciente", back_populates="setores")
    leitos = relationship("Leito", back_populates="setor")

class Leito(Base):
    __tablename__ = "tb_leito"
    id_leito =  Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(String (10), nullable=False)
    tipo = Column(String (10), nullable=False)
    capacidade = Column(Integer, nullable=False)
    status = Column(Enum("Ocupado", "Inativo", "Desocupado"), default="Desocupado")

    id_setor = Column(Integer, ForeignKey("tb_setor.id_setor", ondelete="CASCADE"), nullable=False)

    setor = relationship("Setor", back_populates="leitos")
    internacoes = relationship("Internacao", back_populates="leito")



class Internacao(Base):
    __tablename__ = "tb_internacoes"
    id_internacao = Column(Integer, primary_key=True, autoincrement=True)
    id_paciente = Column(Integer, ForeignKey("tb_paciente.id_paciente", ondelete="CASCADE"), nullable=False)
    id_leito = Column(Integer, ForeignKey("tb_leito.id_leito"), nullable=False)
    data_entrada = Column(DateTime, nullable=False)
    data_saida = Column(DateTime)
    status = Column(Enum("Ativo", "Alta", "Transferido", "Óbito"), default="Ativo")

    paciente = relationship("Paciente", back_populates="internacoes")
    leito = relationship("Leito", back_populates="internacoes")


class Turno(Base):
    __tablename__ = "tb_turnos"
    id_turno = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(50), nullable=False)
    hora_inicio = Column(Time, nullable=False)
    hora_fim = Column(Time, nullable=False)
    id_medico = Column(Integer, ForeignKey("tb_medico.id_medico"), nullable=False)
    id_enfermeiro = Column(Integer, ForeignKey("tb_enfermeiro.id_enfermeiro"), nullable=False)

    medico = relationship("Medico", back_populates="turnos")
    enfermeiro = relationship("Enfermeiro", back_populates="turnos")

class HistoricoPaciente(Base):
    __tablename__ = "tb_historico_paciente"

    id_historico = Column(Integer, primary_key=True, autoincrement=True)
    id_paciente = Column(Integer, ForeignKey("tb_paciente.id_paciente"))
    campo_alterado = Column(String(255))
    valor_antigo = Column(String(255))
    valor_novo = Column(String(255))
    data_modificacao = Column(DateTime)


class Arquivos(Base):
    __tablename__="arquivos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    dados = Column(LargeBinary)

class TurnoPresenca(Base):
    __tablename__ = "vw_turno_atual_com_presenca"
    id_turno = Column(Integer, primary_key=True)
    descricao = Column(String)
    hora_inicio = Column(Time)
    hora_fim = Column(Time)
    enfermeiro_ativo = Column(Integer)          # flag se existe enfermeiro ativo
    total_medicos_ativos = Column(Integer)      # quantidade total de médicos ativos
    total_enfermeiros_ativos = Column(Integer)  # quantidade total de enfermeiros ativos

    
def readonly(*args, **kwargs):
    raise Exception("VIEW é somente leitura.")

event.listen(TurnoPresenca, "before_insert", readonly)
event.listen(TurnoPresenca, "before_update", readonly)
event.listen(TurnoPresenca, "before_delete", readonly)