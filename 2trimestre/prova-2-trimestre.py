import sqlite3 

def cadastrar_hospitais():
    conexao = sqlite3.connect('sistema_hospital.db')
    cursor = conexao.cursor()

    cursor.execute('''
                CREATE TABLE  IF NOT EXISTS hospitais (
                id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cidade TEXT NOT NULL
            )
          ''')
    try:
    nome_hospital = input("Digite o nome do hospital: ")
    nome_cidade = input("Digite o nome da cidade: ")

    comando_inserir = (f'''
                        (INSERT TO hospitais (nome, cidade))
                        VALUES ('{nome_hospital}', '{nome_cidade}')''')

    except ValueError as erro:
        print("Digite apenas o nome!")
     
    print("Hospital cadastrado!")
    conexao.commit() 
    
def cadastrar_medicos():
    conexao = sqlite3.connect('sistema_hospital.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
                CREATE TABLE  IF NOT EXISTS hospitais (
                id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                crm INTEGER UNIQUE NOT NULL,
                id_hospital INTEGER,
                FOREIGN KEY (id_hospitais) REFERENCES hospitais(id)
                )
                ''')
    try:
        nome_medico = input("Digite o nome dos hospitais: ")
        crm_medico = int(input("Digite o crm: "))
        id_hospital = int(input("Digite o id: "))

        comando_inserir = (f'''
                            (INSERT TO hospitais (nome, crm, id_hospital))
                            VALUES ('{nome_medico}', '{crm_medico}', '{id_hospital}')''')
        print("Médico cadastrado! ")
        conexao.commit

    except ValueError as erro:
        print("Digite apenas os números!")

    except sqlite3.IntegrityError as erro:
        print("Erro! Informações cadastradas")






