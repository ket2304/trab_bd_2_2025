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

CREATE TABLE IF NOT EXISTS tb_historico_paciente (
    id_historico INT AUTO_INCREMENT PRIMARY KEY,
    id_paciente INT NOT NULL,
    campo_alterado VARCHAR(100) NOT NULL,
    valor_antigo VARCHAR(255),
    valor_novo VARCHAR(255),
    data_modificacao DATETIME NOT NULL DEFAULT NOW(),

    FOREIGN KEY (id_paciente) REFERENCES tb_paciente(id_paciente)
);

SELECT * FROM tb_historico_paciente;
CREATE TABLE IF NOT EXISTS tb_atendimento(
	id_atendimento INT AUTO_INCREMENT PRIMARY KEY,
	tipo_atendimento VARCHAR(30) NOT NULL,
    data_atendimento DATETIME NOT NULL,
    
    id_paciente INT NOT NULL,
    id_medico INT NOT NULL,
    id_enfermeiro INT NOT NULL,
    
	status ENUM('Aberto', 'Concluído', 'Cancelado') DEFAULT 'Aberto',
    CONSTRAINT fk_paciente_atendimento 
		FOREIGN KEY (id_paciente) REFERENCES tb_paciente(id_paciente),
    CONSTRAINT fk_medico_atendimento
		FOREIGN KEY (id_medico) REFERENCES tb_medico(id_medico),
    CONSTRAINT fk_enfermeiro_atendimento
        FOREIGN KEY (id_enfermeiro) REFERENCES tb_enfermeiro(id_enfermeiro)
    
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
		FOREIGN KEY (id_medico) REFERENCES tb_medico (id_medico),
	
    CONSTRAINT fk_enfermeiro_setor
		FOREIGN KEY (id_enfermeiro) REFERENCES tb_enfermeiro (id_enfermeiro),
    
    CONSTRAINT fk_paciente_setor
		FOREIGN KEY (id_paciente) REFERENCES tb_paciente (id_paciente)
    
);

CREATE TABLE IF NOT EXISTS tb_turno (
    id_turno INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fim TIME NOT NULL,
    
    id_medico INT NOT NULL,
    id_enfermeiro INT NOT NULL,
    
    CONSTRAINT fk_medico_turno
        FOREIGN KEY (id_medico) REFERENCES tb_medico(id_medico),
    CONSTRAINT fk_enfermeiro_turno
        FOREIGN KEY (id_enfermeiro) REFERENCES tb_enfermeiro(id_enfermeiro)
);


CREATE TABLE IF NOT EXISTS tb_leito (
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
    CONSTRAINT fk_paciente_internacao FOREIGN KEY (id_paciente) REFERENCES tb_paciente(id_paciente),
    CONSTRAINT fk_leito_internacao FOREIGN KEY (id_leito) REFERENCES tb_leito(id_leito)
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


ALTER TABLE tb_setor ADD COLUMN nome_setor VARCHAR(100);



ALTER TABLE tb_atendimento 
DROP FOREIGN KEY fk_paciente_atendimento;
ALTER TABLE tb_atendimento
ADD CONSTRAINT fk_paciente_atendimento
FOREIGN KEY (id_paciente) REFERENCES tb_paciente(id_paciente);

ALTER TABLE tb_atendimento 
DROP FOREIGN KEY fk_medico_atendimento;

ALTER TABLE tb_atendimento
ADD CONSTRAINT fk_medico_atendimento
FOREIGN KEY (id_medico) REFERENCES tb_medico(id_medico);

ALTER TABLE tb_atendimento DROP FOREIGN KEY fk_enfermeiro_atendimento;

ALTER TABLE tb_atendimento
ADD CONSTRAINT fk_enfermeiro_atendimento
FOREIGN KEY (id_enfermeiro) REFERENCES tb_enfermeiro(id_enfermeiro);


SELECT * FROM tb_atendimento;
SELECT * FROM tb_enfermeiro;
SELECT * FROM tb_medico;
SELECT * FROM tb_paciente;


ALTER TABLE tb_atendimento 
MODIFY data_atendimento DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP;



UPDATE tb_paciente
SET  telefone_paciente = '(46) 9 8655-6456'
WHERE id_paciente = 4;

SELECT * FROM tb_historico_paciente;

DELIMITER $$

CREATE TRIGGER tg_historico_paciente
AFTER UPDATE ON tb_paciente
FOR EACH ROW
BEGIN
    -- Nome
    IF OLD.nome_paciente <> NEW.nome_paciente THEN
        INSERT INTO tb_historico_paciente
        (id_paciente, campo_alterado, valor_antigo, valor_novo, data_modificacao)
        VALUES
        (NEW.id_paciente, 'nome_paciente', OLD.nome_paciente, NEW.nome_paciente, NOW());
    END IF;

    -- Telefone
    IF OLD.telefone_paciente <> NEW.telefone_paciente THEN
        INSERT INTO tb_historico_paciente
        (id_paciente, campo_alterado, valor_antigo, valor_novo, data_modificacao)
        VALUES
        (NEW.id_paciente, 'telefone_paciente', OLD.telefone_paciente, NEW.telefone_paciente, NOW());
    END IF;

    -- Email
    IF OLD.email_paciente <> NEW.email_paciente THEN
        INSERT INTO tb_historico_paciente
        (id_paciente, campo_alterado, valor_antigo, valor_novo, data_modificacao)
        VALUES
        (NEW.id_paciente, 'email_paciente', OLD.email_paciente, NEW.email_paciente, NOW());
    END IF;
END$$

DELIMITER ;

DROP TABLE IF EXISTS tb_historico_paciente;

CREATE TABLE tb_historico_paciente (
    id_historico INT(11) NOT NULL AUTO_INCREMENT,
    id_paciente INT(11) NOT NULL,
    campo_alterado VARCHAR(100) NOT NULL,
    valor_antigo VARCHAR(255),
    valor_novo VARCHAR(255),
    data_modificacao DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    PRIMARY KEY (id_historico),
    KEY fk_paciente_idx (id_paciente),
    CONSTRAINT fk_paciente FOREIGN KEY (id_paciente)
        REFERENCES tb_paciente(id_paciente)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS tb_arquivo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    dados LONGBLOB
);




DELIMITER $$
CREATE PROCEDURE insere_enfermeiro(p_nome VARCHAR(255), p_coren VARCHAR(20), p_status ENUM('Ativo', 'Inativo'))
begin
	insert into tb_enfermeiro(nome_enfermeiro, coren, status)
	values(p_nome, p_coren, p_status);
end $$

	
DELIMITER ;

select * from tb_estado;

INSERT INTO tb_administrador (nome_adm, email_adm) VALUES
('Marcos Aurélio da Silva', 'marcos.silva@admin.com'),
('Patrícia Oliveira Santos', 'patricia.santos@admin.com'),
('Ricardo Menezes Almeida', 'ricardo.almeida@admin.com'),
('Fernanda Costa Ribeiro', 'fernanda.ribeiro@admin.com'),
('Gustavo Henrique Pereira', 'gustavo.pereira@admin.com');

INSERT INTO tb_hospital (cnpj, nome, telefone, email, endereco, id_adm) VALUES
('12.345.678/0001-90', 'Hospital Santa Maria', '(31) 3222-1188', 'contato@santamaria.com', 'Av. Afonso Pena, 1200 - Centro, Belo Horizonte - MG', 1),

('23.456.789/0001-01', 'Hospital Vida e Saúde', '(11) 3899-2200', 'atendimento@vidaesaude.com', 'Rua Augusta, 900 - Consolação, São Paulo - SP', 2),

('34.567.890/0001-12', 'Hospital São Lucas', '(21) 2444-3300', 'suporte@saolucas.com', 'Av. Atlântica, 4500 - Copacabana, Rio de Janeiro - RJ', 3),

('45.678.901/0001-23', 'Hospital Esperança', '(41) 3377-4411', 'contato@esperanca.com', 'Rua XV de Novembro, 210 - Centro, Curitiba - PR', 4),

('56.789.012/0001-34', 'Hospital Nossa Senhora da Paz', '(71) 3555-5522', 'faleconosco@pazhospital.com', 'Av. Sete de Setembro, 800 - Salvador - BA', 5);


select * from tb_hospital;

