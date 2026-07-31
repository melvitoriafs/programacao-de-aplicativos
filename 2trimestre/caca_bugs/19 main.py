import sqlite3 
 
def buscar_dados_dinamicos(nome_tabela, id_registro):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    tabelas_permitidas = ["alunos", "professores", "turmas"]

    if nome_tabela not in tabelas_permitidas:
        print("Tabela inválida!")
        return

    comando = f"SELECT * FROM {nome_tabela} WHERE id = ?"

    cursor.execute(comando, (id_registro,))

    print(cursor.fetchone())
    conexao.close()

    # Erro: O caractere ? não pode ser usado para nomes de tabela ou coluna. Ele serve apenas para valores