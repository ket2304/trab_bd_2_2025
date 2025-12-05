CREATE DATABASE IF NOT EXISTS  db_sistema_hospital;

USE db_sistema_hospital;


CREATE TABLE IF NOT EXISTS tb_hospital(
	id_hospital  INT AUTO_INCREMENT PRIMARY KEY,
    cnpj VARCHAR(18) NOT NULL UNIQUE,
	nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(50),
    email VARCHAR(100),
    endereco TEXT NOT NULL,
    id_adm INT UNIQUE,
    
    CONSTRAINT fk_hospital_adm FOREIGN KEY (id_adm) REFERENCES tb_administrador(id_adm)
);

CREATE TABLE IF NOT EXISTS tb_paciente(
	id_paciente INT AUTO_INCREMENT PRIMARY KEY,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    nome_paciente VARCHAR(255) NOT NULL,
    sexo_paciente CHAR(1) NOT NULL,
    data_nascimento_paciente DATE NOT NULL,
    email_paciente VARCHAR(255) NOT NULL
); 



CREATE TABLE IF NOT EXISTS tb_atendimento(
	id_atendimento INT AUTO_INCREMENT PRIMARY KEY,
	tipo_atendimento VARCHAR(30) NOT NULL,
    data_atendimento DATETIME NOT NULL,
    
    id_paciente INT NOT NULL,
    id_medico INT NOT NULL,
    id_enfermeiro INT NOT NULL,
    
	status ENUM('Aberto', 'Concluído', 'Cancelado') DEFAULT 'Aberto',
    CONSTRAINT fk_paciente_atendimento 
		FOREIGN KEY (id_paciente) REFERENCES tb_pacientes(id_paciente),
    CONSTRAINT fk_medico_atendimento
		FOREIGN KEY (id_medico) REFERENCES tb_medicos(id_medico),
    CONSTRAINT fk_enfermeiro_atendimento
        FOREIGN KEY (id_enfermeiro) REFERENCES tb_enfermeiros(id_enfermeiro)
    
);

CREATE TABLE IF NOT EXISTS tb_medico(
	id_medico INT AUTO_INCREMENT PRIMARY KEY,
    crm VARCHAR (16) NOT NULL UNIQUE,
    nome_medico VARCHAR(255) NOT NULL,
	especialidade_medico TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_enfermeiro (
    id_enfermeiro INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL,
    coren VARCHAR(20) UNIQUE NOT NULL,
    status ENUM('Ativo', 'Inativo') DEFAULT 'Ativo'
);

CREATE TABLE IF NOT EXISTS tb_setor(
	id_setor INT AUTO_INCREMENT PRIMARY KEY,
	tipo VARCHAR(100) NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    
    id_hospital INT NOT NULL,
    id_medico INT NOT NULL,
    id_enfermeiro INT NOT NULL,
    id_paciente INT NOT NULL,
    
    
    CONSTRAINT fk_hospital_setor
		FOREIGN KEY (id_hospital) REFERENCES tb_hospital (id_hospital),
	
    CONSTRAINT fk_medico_setor
		FOREIGN KEY (id_medico) REFERENCES tb_medicos (id_medico),
	
    CONSTRAINT fk_enfermeiro_setor
		FOREIGN KEY (id_enfermeiro) REFERENCES tb_enfermeiros (id_enfermeiro),
    
    CONSTRAINT fk_paciente_setor
		FOREIGN KEY (id_paciente) REFERENCES tb_pacientes (id_paciente)
    
);

CREATE TABLE IF NOT EXISTS tb_turnos (
    id_turno INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fim TIME NOT NULL,
    
    id_medico INT NOT NULL,
    id_enfermeiro INT NOT NULL,
    
    CONSTRAINT fk_medico_turno
        FOREIGN KEY (id_medico) REFERENCES tb_medicos(id_medico),
    CONSTRAINT fk_enfermeiro_turno
        FOREIGN KEY (id_enfermeiro) REFERENCES tb_enfermeiros(id_enfermeiro)
);


CREATE TABLE IF NOT EXISTS tb_leitos (
    id_leito INT AUTO_INCREMENT PRIMARY KEY,
    numero VARCHAR(10) NOT NULL,
    tipo VARCHAR(50) NOT NULL, 
    capacidade INT NOT NULL,
    id_setor INT NOT NULL,
    CONSTRAINT fk_setor_leito FOREIGN KEY (id_setor) REFERENCES tb_setor(id_setor)
);

CREATE TABLE IF NOT EXISTS tb_internacoes (
    id_internacao INT AUTO_INCREMENT PRIMARY KEY,
    id_paciente INT NOT NULL,
    id_leito INT NOT NULL,
    data_entrada DATETIME NOT NULL,
    data_saida DATETIME NOT NULL,
    status ENUM('Ativo','Alta','Transferido','Óbito') DEFAULT 'Ativo',
    CONSTRAINT fk_paciente_internacao FOREIGN KEY (id_paciente) REFERENCES tb_pacientes(id_paciente),
    CONSTRAINT fk_leito_internacao FOREIGN KEY (id_leito) REFERENCES tb_leitos(id_leito)
);



CREATE TABLE  IF NOT EXISTS tb_estado(
	id_estado INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	estado CHAR(2)
);

CREATE TABLE IF NOT EXISTS tb_cidade(
	id_cidade INT AUTO_INCREMENT PRIMARY KEY,
    cidade VARCHAR (100) NOT NULL,
    
    id_estado INT NOT NULL,
    id_hospital INT NOT NULL,
    
    CONSTRAINT fk_estado_cidade
		FOREIGN KEY (id_estado) REFERENCES tb_estado(id_estado),
    CONSTRAINT fk_hospital_cidade
		FOREIGN KEY (id_hospital) REFERENCES tb_hospital(id_hospital)
        
);

CREATE TABLE IF NOT EXISTS tb_administrador(
	id_adm INT PRIMARY KEY AUTO_INCREMENT,
    nome_adm VARCHAR(255) NOT NULL,
    email_adm VARCHAR(255) NOT NULL
);

ALTER TABLE tb_pacientes ADD COLUMN telefone_paciente VARCHAR(50) NOT NULL;
